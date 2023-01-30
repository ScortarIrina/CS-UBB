package com.example.a7gui.Model.Expressions;

import com.example.a7gui.Model.ADTs.IDictionary;
import com.example.a7gui.Model.ADTs.IHeap;
import com.example.a7gui.Model.Types.IType;
import com.example.a7gui.Model.Values.IValue;
import com.example.a7gui.Exceptions.InterpreterException;

public class VariableExpression implements IExpression {

    String id;

    public VariableExpression(String id) {
        this.id = id;
    }

    @Override
    public IValue evaluate(IDictionary<String, IValue> symTable, IHeap heap) throws InterpreterException {
        return symTable.search(this.id);
    }

    @Override
    public IType typeCheck(IDictionary<String, IType> typeEnv) throws InterpreterException {
        return typeEnv.search(id);
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
