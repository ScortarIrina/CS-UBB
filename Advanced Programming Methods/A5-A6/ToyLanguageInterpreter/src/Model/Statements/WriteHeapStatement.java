package Model.Statements;

import Exceptions.ADTException;
import Exceptions.ExpressionEvaluationException;
import Exceptions.StatementExecutionException;
import Model.ADTs.IDictionary;
import Model.ADTs.IHeap;
import Model.Expressions.IExpression;
import Model.ProgramState.ProgramState;
import Model.Types.IType;
import Model.Types.ReferenceType;
import Model.Values.IValue;
import Model.Values.ReferenceValue;

public class WriteHeapStatement implements IStatement {
    private final String varName;   // the heap address
    private final IExpression expression;   // new value to be stored in the heap

    public WriteHeapStatement(String varName, IExpression expression) {
        this.varName = varName;
        this.expression = expression;
    }

    @Override
    public ProgramState execute(ProgramState state) throws StatementExecutionException, ExpressionEvaluationException, ADTException {
        IDictionary<String, IValue> symbolTable = state.getSymbolTable();
        IHeap heap = state.getHeap();

        // check is varName is defined in symbolTable
        if (!symbolTable.exists(varName)) {
            throw new StatementExecutionException(String.format("%s is not in the symbol table!", varName));
        }

        IValue value = symbolTable.search(varName);

        // check if varName is of ReferenceType
        if (!(value instanceof ReferenceValue)) {
            throw new StatementExecutionException(String.format("%s is not reference type!", value));
        }

        ReferenceValue referenceValue = (ReferenceValue) value;
        IValue evaluated = expression.evaluate(symbolTable, heap);

        // check if the type of the evaluated expression and of the referenceValue is the same
        if (!evaluated.getType().equals(referenceValue.getLocationType())) {
            throw new StatementExecutionException(String.format("%s  not of %s", evaluated, referenceValue.getLocationType()));
        }

        // the heap entry is updated to the result of the evaluated expression
        heap.update(referenceValue.getAddress(), evaluated);
        state.setHeap(heap);

        return null;
    }

    @Override
    public IDictionary<String, IType> typeCheck(IDictionary<String, IType> typeEnv) throws StatementExecutionException, ExpressionEvaluationException, ADTException {
        if (typeEnv.search(varName).equals(new ReferenceType(expression.typeCheck(typeEnv))))
            return typeEnv;
        else
            throw new StatementExecutionException("WriteHeap: right hand side and left hand side have different types.");
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
