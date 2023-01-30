package com.example.a7gui.Model.Statements;

import com.example.a7gui.Exceptions.InterpreterException;
import com.example.a7gui.Model.Expressions.IExpression;
import com.example.a7gui.Model.ProgramState.ProgramState;
import com.example.a7gui.Model.Types.ReferenceType;
import com.example.a7gui.Model.Types.IType;
import com.example.a7gui.Model.ADTs.IDictionary;
import com.example.a7gui.Model.ADTs.IHeap;
import com.example.a7gui.Model.Values.ReferenceValue;
import com.example.a7gui.Model.Values.IValue;

public class NewStatement implements IStatement{
    private final String varName;
    private final IExpression expression;

    public NewStatement(String varName, IExpression expression) {
        this.varName = varName;
        this.expression = expression;
    }

    @Override
    public ProgramState execute(ProgramState state) throws InterpreterException {
        IDictionary<String, IValue> symbolTable = state.getSymbolTable();
        IHeap heap = state.getHeap();

        if (!symbolTable.exists(varName)) {
            throw new InterpreterException(String.format("%s is not in symbolTable", varName));
        }

        IValue varValue = symbolTable.search(varName);

        if (!(varValue.getType() instanceof ReferenceType)) {
            throw new InterpreterException(String.format("%s in not of ReferenceType", varName));
        }

        IValue evaluated = expression.evaluate(symbolTable, heap);
        IType locationType = ((ReferenceValue)varValue).getLocationType();

        if (!locationType.equals(evaluated.getType())) {
            throw new InterpreterException(String.format("%s not of %s", varName, evaluated.getType()));
        }

        int newPosition = heap.add(evaluated);
        symbolTable.put(varName, new ReferenceValue(newPosition, locationType));
        state.setSymbolTable(symbolTable);
        state.setHeap(heap);

        return null;
    }

    @Override
    public IDictionary<String, IType> typeCheck(IDictionary<String, IType> typeEnv) throws InterpreterException, InterpreterException {
        IType typeVar = typeEnv.search(varName);
        IType typeExpr = expression.typeCheck(typeEnv);
        if (typeVar.equals(new ReferenceType(typeExpr)))
            return typeEnv;
        else
            throw new InterpreterException("NEW statement: right hand side and left hand side have different types.");
    }

    @Override
    public IStatement deepCopy() {
        return new NewStatement(varName, expression.deepCopy());
    }

    @Override
    public String toString() {
        return String.format("New(%s, %s)", varName, expression);
    }
}
