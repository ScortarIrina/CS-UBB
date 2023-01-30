package com.example.a7gui.Model.Statements;

import com.example.a7gui.Exceptions.InterpreterException;
import com.example.a7gui.Model.ADTs.IDictionary;
import com.example.a7gui.Model.ProgramState.ProgramState;
import com.example.a7gui.Model.Types.IType;

public class NOPStatement implements IStatement
{
    @Override
    public ProgramState execute(ProgramState state) {
        return null;
    }

    @Override
    public IDictionary<String, IType> typeCheck(IDictionary<String, IType> typeEnv) throws InterpreterException {
        return typeEnv;
    }

    @Override
    public IStatement deepCopy() {
        return new NOPStatement();
    }

    @Override
    public String toString() {
        return "NOP statement";
    }
}
