package com.example.a7gui.Model.Expressions;

import com.example.a7gui.Model.ADTs.IDictionary;
import com.example.a7gui.Model.ADTs.IHeap;
import com.example.a7gui.Model.Types.IType;
import com.example.a7gui.Model.Values.IValue;
import com.example.a7gui.Exceptions.InterpreterException;

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
    public IType typeCheck(IDictionary<String, IType> typeEnv) throws InterpreterException {
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
