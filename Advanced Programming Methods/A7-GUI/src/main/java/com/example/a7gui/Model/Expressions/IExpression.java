package com.example.a7gui.Model.Expressions;

import com.example.a7gui.Model.ADTs.IDictionary;
import com.example.a7gui.Model.ADTs.IHeap;
import com.example.a7gui.Model.Types.IType;
import com.example.a7gui.Model.Values.IValue;
import com.example.a7gui.Exceptions.InterpreterException;

import java.util.SplittableRandom;

public interface IExpression {

    IValue evaluate(IDictionary<String, IValue> symbolTable, IHeap heap) throws InterpreterException;

    IExpression deepCopy();

    IType typeCheck(IDictionary<String, IType> typeEnv) throws InterpreterException;
}
