package com.example.a7gui.Model.Values;

import com.example.a7gui.Model.Types.IType;

public interface IValue {

    IType getType();

    IValue deepCopy();
}
