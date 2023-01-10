package Model.Statements;

import Exceptions.ADTException;
import Exceptions.ExpressionEvaluationException;
import Exceptions.StatementExecutionException;
import Model.Expressions.IExpression;
import Model.ProgramState.ProgramState;
import Model.Types.ReferenceType;
import Model.Types.IType;
import Model.ADTs.IDictionary;
import Model.ADTs.IHeap;
import Model.Values.ReferenceValue;
import Model.Values.IValue;

public class NewStatement implements IStatement{
    private final String varName;
    private final IExpression expression;

    public NewStatement(String varName, IExpression expression) {
        this.varName = varName;
        this.expression = expression;
    }

    @Override
    public ProgramState execute(ProgramState state) throws StatementExecutionException, ExpressionEvaluationException, ADTException {
        IDictionary<String, IValue> symbolTable = state.getSymbolTable();
        IHeap heap = state.getHeap();

        if (!symbolTable.exists(varName)) {
            throw new StatementExecutionException(String.format("%s is not in symbolTable", varName));
        }

        IValue varValue = symbolTable.search(varName);

        if (!(varValue.getType() instanceof ReferenceType)) {
            throw new StatementExecutionException(String.format("%s in not of ReferenceType", varName));
        }

        IValue evaluated = expression.evaluate(symbolTable, heap);
        IType locationType = ((ReferenceValue)varValue).getLocationType();

        if (!locationType.equals(evaluated.getType())) {
            throw new StatementExecutionException(String.format("%s not of %s", varName, evaluated.getType()));
        }

        int newPosition = heap.add(evaluated);
        symbolTable.put(varName, new ReferenceValue(newPosition, locationType));
        state.setSymbolTable(symbolTable);
        state.setHeap(heap);

        return null;
    }

    @Override
    public IDictionary<String, IType> typeCheck(IDictionary<String, IType> typeEnv) throws StatementExecutionException, ExpressionEvaluationException, ADTException {
        IType typeVar = typeEnv.search(varName);
        IType typeExpr = expression.typeCheck(typeEnv);
        if (typeVar.equals(new ReferenceType(typeExpr)))
            return typeEnv;
        else
            throw new StatementExecutionException("NEW statement: right hand side and left hand side have different types.");
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
