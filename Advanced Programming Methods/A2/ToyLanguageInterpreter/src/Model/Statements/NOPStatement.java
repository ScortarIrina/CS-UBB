package Model.Statements;

import Model.ProgramState.ProgramState;

public class NOPStatement implements IStatement
{
    @Override
    public ProgramState execute(ProgramState state) {
        return null;
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
