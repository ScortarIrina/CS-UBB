package Model.Types;


import Model.Values.IValue;

public interface IType {
    boolean equals(IType t);

    IValue defaultValue();

    IType deepCopy();
}
