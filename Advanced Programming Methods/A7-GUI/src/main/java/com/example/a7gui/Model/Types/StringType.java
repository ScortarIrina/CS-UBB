package com.example.a7gui.Model.Types;

import com.example.a7gui.Model.Values.IValue;
import com.example.a7gui.Model.Values.IntValue;
import com.example.a7gui.Model.Values.StringValue;

public class StringType implements IType {
    @Override
    public boolean equals(IType t) {
        return t instanceof StringType;
    }

    @Override
    public IValue defaultValue() {
        return new StringValue("");
    }

    @Override
    public IType deepCopy() {
        return new StringType();
    }

    @Override
    public String toString() {
        return "string";
    }
}
