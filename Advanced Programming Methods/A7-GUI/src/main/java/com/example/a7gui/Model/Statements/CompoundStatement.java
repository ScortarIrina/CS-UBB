package com.example.a7gui.Model.Statements;

import com.example.a7gui.Exceptions.InterpreterException;
import com.example.a7gui.Model.ADTs.IDictionary;
import com.example.a7gui.Model.ADTs.IStack;
import com.example.a7gui.Model.ProgramState.ProgramState;
import com.example.a7gui.Model.Types.IType;

public class CompoundStatement implements IStatement {

    IStatement s1;
    IStatement s2;

    public CompoundStatement(IStatement s1, IStatement s2) {
        this.s1 = s1;
        this.s2 = s2;
    }

    @Override
    public ProgramState execute(ProgramState state) {
        // the top of the ExecutionStack is changed while SymbolTable and Output remain unchanged.
        IStack<IStatement> stack = state.getExecutionStack();
        stack.push(s2);
        stack.push(s1);
        state.setExecutionStack(stack);
        return null;
    }

    @Override
    public IDictionary<String, IType> typeCheck(IDictionary<String, IType> typeEnv) throws InterpreterException {
        return s2.typeCheck(s1.typeCheck(typeEnv));
    }

    @Override
    public IStatement deepCopy() {
        return new CompoundStatement(s1.deepCopy(), s2.deepCopy());
    }

    @Override
    public String toString() {
        return String.format("(%s | %s)", s1.toString(),s2.toString());
    }
}
