package Model.Types;

import Model.Values.IValue;
import Model.Values.BoolValue;

public class BoolType implements IType {

    @Override
    public boolean equals(IType t) {
        return t instanceof BoolType;
    }

    @Override
    public IValue defaultValue() {
        return new BoolValue(false);
    }

    @Override
    public IType deepCopy() {
        return new BoolType();
    }

    @Override
    public String toString() {
        return "bool";
    }
}
