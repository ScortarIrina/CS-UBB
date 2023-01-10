package Model.Expressions;

import Model.ADTs.IDictionary;
import Model.ADTs.IHeap;
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

    public IExpression deepCopy() {
        return new ValueExpression(value);
    }

    @Override
    public String toString() {
        return this.value.toString();
    }
}
