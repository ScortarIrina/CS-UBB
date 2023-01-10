package Model.Types;

import Model.Values.IValue;
import Model.Values.ReferenceValue;

public class ReferenceType implements IType {
    private final IType inner;

    public ReferenceType(IType inner) {
        this.inner = inner;
    }

    IType getInner() {
        return this.inner;
    }

    @Override
    public boolean equals(IType anotherType) {
        if (anotherType instanceof ReferenceType) {
            return inner.equals(((ReferenceType) anotherType).getInner());
        }
        else return false;
    }

    @Override
    public IValue defaultValue() {
        return new ReferenceValue(0, inner);
    }

    @Override
    public IType deepCopy() {
        return new ReferenceType(inner.deepCopy());
    }

    @Override
    public String toString() {
        return String.format("Ref(%s)", inner);
    }
}
