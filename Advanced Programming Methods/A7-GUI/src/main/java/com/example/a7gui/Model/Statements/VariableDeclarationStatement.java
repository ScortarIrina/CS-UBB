package com.example.a7gui.Model.Statements;

import com.example.a7gui.Model.ADTs.IDictionary;
import com.example.a7gui.Model.Statements.IStatement;
import com.example.a7gui.Model.ProgramState.ProgramState;
import com.example.a7gui.Model.Values.IValue;
import com.example.a7gui.Model.Types.IType;
import com.example.a7gui.Exceptions.InterpreterException;

public class VariableDeclarationStatement implements IStatement {
    String name;
    IType type;

    public VariableDeclarationStatement(String n, IType t) {
        this.name = n;
        this.type = t;
    }

    @Override
    public ProgramState execute(ProgramState state) throws InterpreterException {
        IDictionary<String, IValue> symTable = state.getSymbolTable();

        if(symTable.exists(this.name)) {
            throw new InterpreterException("Variable " + this.name + " is already declared");
        }

        symTable.put(this.name,this.type.defaultValue());
        state.setSymbolTable(symTable);

        return null;
    }

    @Override
    public IDictionary<String, IType> typeCheck(IDictionary<String, IType> typeEnv) throws InterpreterException {
        typeEnv.put(name, type);
        return typeEnv;
    }

    @Override
    public IStatement deepCopy() {
        return new VariableDeclarationStatement(name, type);
    }

    @Override
    public String toString() {
        return String.format("%s %s", type.toString(), name);
    }
}
