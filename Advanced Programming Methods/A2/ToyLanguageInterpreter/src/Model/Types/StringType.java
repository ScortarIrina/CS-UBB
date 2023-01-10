package Model.Types;

import Model.Values.IValue;
import Model.Values.IntValue;
import Model.Values.StringValue;

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
