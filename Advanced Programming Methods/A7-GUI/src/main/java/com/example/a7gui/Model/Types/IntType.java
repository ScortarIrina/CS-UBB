package com.example.a7gui.Model.Types;

import com.example.a7gui.Model.Values.IValue;
import com.example.a7gui.Model.Values.IntValue;

public class IntType implements IType {

    @Override
    public boolean equals(IType t) {
        return t instanceof IntType;
    }

    @Override
    public IValue defaultValue() {
        return new IntValue(0);
    }

    @Override
    public IType deepCopy() {
        return new IntType();
    }

    @Override
    public String toString() {
        return "int";
    }
}
