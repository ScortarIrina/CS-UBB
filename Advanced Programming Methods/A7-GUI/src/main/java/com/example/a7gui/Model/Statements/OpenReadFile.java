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
import java.io.FileNotFoundException;
import java.io.FileReader;

public class OpenReadFile implements IStatement {
    private IExpression expr;

    public OpenReadFile(IExpression expr) {
        this.expr = expr;
    }

    @Override
    public ProgramState execute(ProgramState state) throws InterpreterException {
        IValue value = expr.evaluate(state.getSymbolTable(), state.getHeap());

        if(value.getType().equals(new StringType())) {
            StringValue fileName = (StringValue) value;
            IDictionary<String, BufferedReader> fileTable = state.getFileTable();

            if(!fileTable.exists(fileName.getValue())) {
                BufferedReader br;
                try {
                    br = new BufferedReader(new FileReader(fileName.getValue()));
                }
                catch(FileNotFoundException e) {
                    throw new InterpreterException(String.format("%s could not be opened", fileName.getValue()));
                }

                fileTable.put(fileName.getValue(),br);
                state.setFileTable(fileTable);
            }
            else
                throw new InterpreterException(String.format("%s is already opened",fileName.getValue()));
        }
        else
            throw new InterpreterException(String.format("%s is not string type",expr.toString()));

        return null;
    }

    @Override
    public IDictionary<String, IType> typeCheck(IDictionary<String, IType> typeEnv) throws InterpreterException {
        if (expr.typeCheck(typeEnv).equals(new StringType()))
            return typeEnv;
        else
            throw new InterpreterException("OpenReadFile requires a string expression.");
    }

    @Override
    public IStatement deepCopy() {
        return new OpenReadFile(expr.deepCopy());
    }

    @Override
    public String toString() {
        return String.format("OpenReadFile(%s)",expr.toString());
    }
}
