package com.example.a7gui.Model.Statements;

import com.example.a7gui.Model.ADTs.IDictionary;
import com.example.a7gui.Model.ProgramState.ProgramState;
import com.example.a7gui.Model.Types.IType;
import com.example.a7gui.Exceptions.InterpreterException;

public interface IStatement {
    ProgramState execute(ProgramState state) throws InterpreterException;

    IDictionary<String, IType> typeCheck(IDictionary<String, IType> typeEnv) throws InterpreterException;

    IStatement deepCopy();
}
