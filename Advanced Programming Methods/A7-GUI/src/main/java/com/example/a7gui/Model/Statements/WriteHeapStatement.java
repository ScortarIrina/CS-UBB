package com.example.a7gui.Model.Statements;

import com.example.a7gui.Exceptions.InterpreterException;
import com.example.a7gui.Model.ADTs.IDictionary;
import com.example.a7gui.Model.ADTs.IHeap;
import com.example.a7gui.Model.Expressions.IExpression;
import com.example.a7gui.Model.ProgramState.ProgramState;
import com.example.a7gui.Model.Types.IType;
import com.example.a7gui.Model.Types.ReferenceType;
import com.example.a7gui.Model.Values.IValue;
import com.example.a7gui.Model.Values.ReferenceValue;

public class WriteHeapStatement implements IStatement {
    private final String varName;   // the heap address
    private final IExpression expression;   // new value to be stored in the heap

    public WriteHeapStatement(String varName, IExpression expression) {
        this.varName = varName;
        this.expression = expression;
    }

    @Override
    public ProgramState execute(ProgramState state) throws InterpreterException {
        IDictionary<String, IValue> symbolTable = state.getSymbolTable();
        IHeap heap = state.getHeap();

        // check is varName is defined in symbolTable
        if (!symbolTable.exists(varName)) {
            throw new InterpreterException(String.format("%s is not in the symbol table!", varName));
        }

        IValue value = symbolTable.search(varName);

        // check if varName is of ReferenceType
        if (!(value instanceof ReferenceValue)) {
            throw new InterpreterException(String.format("%s is not reference type!", value));
        }

        ReferenceValue referenceValue = (ReferenceValue) value;
        IValue evaluated = expression.evaluate(symbolTable, heap);

        // check if the type of the evaluated expression and of the referenceValue is the same
        if (!evaluated.getType().equals(referenceValue.getLocationType())) {
            throw new InterpreterException(String.format("%s  not of %s", evaluated, referenceValue.getLocationType()));
        }

        // the heap entry is updated to the result of the evaluated expression
        heap.update(referenceValue.getAddress(), evaluated);
        state.setHeap(heap);

        return null;
    }

    @Override
    public IDictionary<String, IType> typeCheck(IDictionary<String, IType> typeEnv) throws InterpreterException {
        if (typeEnv.search(varName).equals(new ReferenceType(expression.typeCheck(typeEnv))))
            return typeEnv;
        else
            throw new InterpreterException("WriteHeap: right hand side and left hand side have different types.");
    }

    @Override
    public IStatement deepCopy() {
        return new WriteHeapStatement(varName, expression.deepCopy());
    }

    @Override
    public String toString() {
        return String.format("WriteHeap(%s, %s)", varName, expression);
    }
}
