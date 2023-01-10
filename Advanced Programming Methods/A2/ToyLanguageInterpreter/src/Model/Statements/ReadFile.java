package Model.Statements;

import Exceptions.ADTException;
import Exceptions.ExpressionEvaluationException;
import Exceptions.StatementExecutionException;
import Model.ADTs.IDictionary;
import Model.Expressions.IExpression;
import Model.ProgramState.ProgramState;
import Model.Types.IntType;
import Model.Types.StringType;
import Model.Values.IValue;
import Model.Values.IntValue;
import Model.Values.StringValue;

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
    public ProgramState execute(ProgramState state) throws StatementExecutionException, ExpressionEvaluationException, ADTException {
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
                            throw new StatementExecutionException(String.format("ERROR: Couldn't read from file %s",castValue));
                        }
                    }
                    else
                        throw new StatementExecutionException(String.format("ERROR: The file table doesn't contain %s", castValue));
                }
                else
                    throw new StatementExecutionException(String.format("ERROR: %s is not a string type",value));
            }
            else
                throw new StatementExecutionException(String.format("ERROR: %s is not int type",value));
        }
        else
            throw new StatementExecutionException(String.format("ERROR: %s is not in the symbol table", varName));
        return state;
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
