package com.example.a7gui.Model.Values;

import com.example.a7gui.Model.Types.IType;
import com.example.a7gui.Model.Types.IntType;

public class IntValue implements IValue {

    private final int value;

    public IntValue(int value) {
        this.value = value;
    }

    public int getValue() {
        return value;
    }

    @Override
    public boolean equals(Object obj) {
        if (!(obj instanceof IntValue copy))
            return false;
        return this.value == copy.getValue();
    }

    @Override
    public String toString() {
        return String.format("%d",this.value);
    }

    @Override
    public IType getType() {
        return new IntType();
    }

    @Override
    public IValue deepCopy() {
        return new IntValue((value));
    }
}
