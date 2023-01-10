package Model.Expressions;

import Exceptions.ADTException;
import Model.ADTs.IDictionary;
import Model.ADTs.IHeap;
import Model.Values.IValue;

public class VariableExpression implements IExpression {
    String id;

    public VariableExpression(String id) {
        this.id = id;
    }

    @Override
    public IValue evaluate(IDictionary<String, IValue> symTable, IHeap heap) throws ADTException {
        return symTable.search(this.id);
    }

    @Override
    public IExpression deepCopy() {
        return new VariableExpression(id);
    }

    @Override
    public String toString() {
        return this.id;
    }
}
