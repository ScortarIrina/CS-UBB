package com.example.a7gui.Model.Values;

import com.example.a7gui.Model.Types.IType;
import com.example.a7gui.Model.Types.StringType;

public class StringValue implements  IValue {
    private String value;

    public StringValue(String v) {
        this.value = v;
    }

    @Override
    public IType getType() {
        return new StringType();
    }

    public String getValue() {
        return this.value;
    }

    @Override
    public boolean equals(Object v) {
        if(!(v instanceof StringValue)) {
            return false;
        }

        StringValue cast = (StringValue) v;
        return this.value.equals(cast.value);
    }

    @Override
    public IValue deepCopy() {
        return new StringValue(value);
    }

    @Override
    public String toString() {
        return this.value;
    }
}
