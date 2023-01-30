package com.example.a7gui.Model.Statements;

import com.example.a7gui.Exceptions.InterpreterException;
import com.example.a7gui.Model.ADTs.IDictionary;
import com.example.a7gui.Model.Expressions.IExpression;
import com.example.a7gui.Model.ProgramState.ProgramState;
import com.example.a7gui.Model.Types.IType;
import com.example.a7gui.Model.Types.IntType;
import com.example.a7gui.Model.Types.StringType;
import com.example.a7gui.Model.Values.IValue;
import com.example.a7gui.Model.Values.IntValue;
import com.example.a7gui.Model.Values.StringValue;

import java.io.BufferedReader;
import java.io.IOException;

public class ReadFile implements IStatement {
    private IExpression expression;
    private String varName;

    public ReadFile(IExpression expr, String varName) {
        this.expression = expr;
        this.varName = varName;
    }

    @Override
    public ProgramState execute(ProgramState state) throws InterpreterException {
        IDictionary<String, IValue> symTable = state.getSymbolTable();
        IDictionary<String, BufferedReader> fileTable = state.getFileTable();

        if(symTable.exists(varName)) {
            IValue value = symTable.search(varName);

            if(value.getType().equals(new IntType())) {
                value = expression.evaluate(symTable, state.getHeap());

                if(value.getType().equals(new StringType())) {
                    StringValue castValue = (StringValue) value;

                    if(fileTable.exists(castValue.getValue())) {
                        BufferedReader br = fileTable.search(castValue.getValue());

                        try {
                            String line = br.readLine();
                            if(line == null)
                                line = "0";
                            symTable.put(varName,new IntValue(Integer.parseInt(line)));
                        }
                        catch(IOException e) {
                            throw new InterpreterException(String.format("ERROR: Couldn't read from file %s",castValue));
                        }
                    }
                    else
                        throw new InterpreterException(String.format("ERROR: The file table doesn't contain %s", castValue));
                }
                else
                    throw new InterpreterException(String.format("ERROR: %s is not a string type",value));
            }
            else
                throw new InterpreterException(String.format("ERROR: %s is not int type",value));
        }
        else
            throw new InterpreterException(String.format("ERROR: %s is not in the symbol table", varName));

        return null;
    }

    @Override
    public IDictionary<String, IType> typeCheck(IDictionary<String, IType> typeEnv) throws InterpreterException {
        if (expression.typeCheck(typeEnv).equals(new StringType()))
            if (typeEnv.search(varName).equals(new IntType()))
                return typeEnv;
            else
                throw new InterpreterException("ReadFile requires an int as its variable parameter.");
        else
            throw new InterpreterException("ReadFile requires a string as es expression parameter.");
    }

    @Override
    public IStatement deepCopy() {
        return new ReadFile(expression.deepCopy(), varName);
    }

    @Override
    public String toString() {
        return String.format("ReadFile(%s %s)", expression.toString(),varName);
    }

}
