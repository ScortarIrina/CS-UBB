package Model.Expressions;

import Exceptions.ADTException;
import Exceptions.ExpressionEvaluationException;
import Model.ADTs.IDictionary;
import Model.ADTs.IHeap;
import Model.Types.IType;
import Model.Types.ReferenceType;
import Model.Values.IValue;
import Model.Values.ReferenceValue;

public class ReadHeapExpression implements IExpression {
    private final IExpression expression;

    public ReadHeapExpression(IExpression expression) {
        this.expression = expression;
    }

    @Override
    public IValue evaluate(IDictionary<String, IValue> symbolTable, IHeap heap) throws ExpressionEvaluationException, ADTException {
        // the expression must be evaluated to a ReferenceValue
        IValue value = expression.evaluate(symbolTable, heap);
        if (!(value instanceof ReferenceValue)) {
            throw new ExpressionEvaluationException(String.format("%s not of type reference", value));
        }

        // take the address of the ReferenceValue and use it to access Heap table
        ReferenceValue refValue = (ReferenceValue) value;
        return heap.get(refValue.getAddress());
    }

    @Override
    public IType typeCheck(IDictionary<String, IType> typeEnv) throws ExpressionEvaluationException, ADTException {
        IType type = expression.typeCheck(typeEnv);
        if (type instanceof ReferenceType) {
            ReferenceType refType = (ReferenceType) type;
            return refType.getInner();
        } else
            throw new ExpressionEvaluationException("The readHeap argument is not a ReferenceType.");
    }

    @Override
    public String toString() {
        return String.format("ReadHeap(%s)", expression);
    }

    @Override
    public IExpression deepCopy() {
        return new ReadHeapExpression(expression.deepCopy());
    }
}
