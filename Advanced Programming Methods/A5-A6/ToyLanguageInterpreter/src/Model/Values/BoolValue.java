package Model.Values;

import Model.Types.IType;
import Model.Types.BoolType;

public class BoolValue implements IValue {
    private boolean value;

    public BoolValue(boolean v) {
        this.value = v;
    }

    public boolean getValue() {
        return this.value;
    }

    @Override
    public IType getType() {
        return new BoolType();
    }

    @Override
    public boolean equals(Object obj) {
        if(!(obj instanceof BoolValue copy))
            return false;
        return this.value == copy.getValue();
    }

    @Override
    public IValue deepCopy() {
        return new BoolValue(value);
    }

    @Override
    public String toString() {
        return this.value ? "true" : "false";
    }
}
