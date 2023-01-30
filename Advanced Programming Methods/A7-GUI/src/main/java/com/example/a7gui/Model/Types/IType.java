package com.example.a7gui.Model.Types;

import com.example.a7gui.Model.Values.IValue;

public interface IType {

    boolean equals(IType t);

    IValue defaultValue();

    IType deepCopy();
}
