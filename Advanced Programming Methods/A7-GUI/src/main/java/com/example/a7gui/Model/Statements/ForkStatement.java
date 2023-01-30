package com.example.a7gui.Model.Statements;

import com.example.a7gui.Exceptions.InterpreterException;
import com.example.a7gui.Model.ADTs.IDictionary;
import com.example.a7gui.Model.ADTs.IStack;
import com.example.a7gui.Model.ADTs.MyDictionary;
import com.example.a7gui.Model.ADTs.MyStack;
import com.example.a7gui.Model.ProgramState.ProgramState;
import com.example.a7gui.Model.Types.IType;
import com.example.a7gui.Model.Values.IValue;
import java.util.Map;

public class ForkStatement implements IStatement {

    private final IStatement statement;

    public ForkStatement(IStatement statement ){
        this.statement = statement;
    }

    @Override
    public ProgramState execute(ProgramState state) throws InterpreterException {
        IStack<IStatement> newStack = new MyStack<>();
        newStack.push(statement);
        IDictionary<String, IValue> newSymTable = new MyDictionary<>();
        for (Map.Entry<String, IValue> entry: state.getSymbolTable().getContent().entrySet()) {
            newSymTable.put(entry.getKey(), entry.getValue().deepCopy());
        }

        return new ProgramState(newStack, newSymTable, state.getOutput(), state.getFileTable(), state.getHeap());
    }

    @Override
    public IDictionary<String, IType> typeCheck(IDictionary<String, IType> typeEnv) throws InterpreterException {
        statement.typeCheck(typeEnv.deepCopy());
        return typeEnv;
    }

    @Override
    public IStatement deepCopy() {
        return new ForkStatement(statement.deepCopy());
    }

    @Override
    public String toString() {
        return String.format("Fork(%s)", statement.toString());
    }
}
