package Model.Values;

import Model.Types.IType;
import Model.Types.IntType;

public class IntValue implements IValue {
    private int value;

    public IntValue(int v) {
        this.value = v;
    }

    public int getValue() {
        return this.value;
    }

    @Override
    public IType getType() {
        return new IntType();
    }

    @Override
    public boolean equals(Object obj) {
        if(!(obj instanceof IntValue copy))
            return false;
        return this.value == copy.getValue();
    }

   @Override
   public IValue deepCopy() {
       return new IntValue((value));
   }

    @Override
    public String toString() {
        return String.format("%d",this.value);
    }
}
