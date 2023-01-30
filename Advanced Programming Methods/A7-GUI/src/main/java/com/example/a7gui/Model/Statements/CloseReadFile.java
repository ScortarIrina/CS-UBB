package com.example.a7gui.Model.Statements;

import com.example.a7gui.Exceptions.InterpreterException;
import com.example.a7gui.Model.ADTs.IDictionary;
import com.example.a7gui.Model.Expressions.IExpression;
import com.example.a7gui.Model.ProgramState.ProgramState;
import com.example.a7gui.Model.Types.IType;
import com.example.a7gui.Model.Types.StringType;
import com.example.a7gui.Model.Values.IValue;
import com.example.a7gui.Model.Values.StringValue;

import java.io.BufferedReader;
import java.io.IOException;

public class CloseReadFile implements IStatement {
    private IExpression expr;

    public CloseReadFile(IExpression e) {
        this.expr = e;
    }

    @Override
    public ProgramState execute(ProgramState state) throws InterpreterException {
        IValue value = expr.evaluate(state.getSymbolTable(), state.getHeap());

        if(!value.getType().equals(new StringType())) {
            throw new InterpreterException(String.format("%s is not string value", expr));
        }

        StringValue fileName = (StringValue) value;
        IDictionary<String, BufferedReader> fileTable = state.getFileTable();

        if(!fileTable.exists(fileName.getValue())) {
            throw new InterpreterException(String.format("%s is not in the file table", value));
        }

        BufferedReader br = fileTable.search(fileName.getValue());
        try {
            br.close();
        }
        catch(IOException e) {
            throw new InterpreterException(String.format("Error on closing %s",value));
        }

        fileTable.remove(fileName.getValue());
        state.setFileTable(fileTable);
        return null;
    }

    @Override
    public IDictionary<String, IType> typeCheck(IDictionary<String, IType> typeEnv) throws InterpreterException {
        if (expr.typeCheck(typeEnv).equals(new StringType()))
            return typeEnv;
        else
            throw new InterpreterException("CloseReadFile requires a string expression.");
    }

    @Override
    public IStatement deepCopy() {
        return new CloseReadFile(expr.deepCopy());
    }

    @Override
    public String toString() {
        return String.format("CloseReadFile(%s)",expr.toString());
    }
}
