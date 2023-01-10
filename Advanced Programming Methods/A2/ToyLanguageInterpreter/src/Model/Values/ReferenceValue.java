package Model.Values;

import Model.Types.IType;
import Model.Types.ReferenceType;

public class ReferenceValue implements IValue {
    private final int address;
    private final IType locationType;

    public ReferenceValue(int address, IType locationType) {
        this.address = address;
        this.locationType = locationType;
    }

    @Override
    public IType getType() {
        return new ReferenceType(locationType);
    }

    public int getAddress() {
        return address;
    }

    public IType getLocationType() {
        return locationType;
    }

    @Override
    public IValue deepCopy() {
        return new ReferenceValue(address, locationType.deepCopy());
    }

    @Override
    public String toString() {
        return String.format("(%d, %s)", address, locationType);
    }
}
