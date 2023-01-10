package Model.Expressions;

import Exceptions.ExpressionEvaluationException;
import Model.ADTs.IDictionary;
import Model.ADTs.IHeap;
import Model.Types.IType;
import Model.Values.IValue;

public class ValueExpression implements IExpression {
    IValue value;

    public ValueExpression(IValue v) {
        this.value = v;
    }

    @Override
    public IValue evaluate(IDictionary<String, IValue> symTable, IHeap heap) {
        return this.value;
    }

    @Override
    public IType typeCheck(IDictionary<String, IType> typeEnv) throws ExpressionEvaluationException {
        return value.getType();
    }

    public IExpression deepCopy() {
        return new ValueExpression(value);
    }

    @Override
    public String toString() {
        return this.value.toString();
    }
}
