package Model.Statements;

import Exceptions.ADTException;
import Exceptions.ExpressionEvaluationException;
import Exceptions.StatementExecutionException;
import Model.ADTs.IDictionary;
import Model.Expressions.IExpression;
import Model.ProgramState.ProgramState;
import Model.Types.StringType;
import Model.Values.IValue;
import Model.Values.StringValue;

import java.io.BufferedReader;
import java.io.IOException;

public class CloseReadFile implements IStatement {
    private IExpression expr;

    public CloseReadFile(IExpression e) {
        this.expr = e;
    }

    @Override
    public ProgramState execute(ProgramState state) throws StatementExecutionException, ExpressionEvaluationException, ADTException {
        IValue value = expr.evaluate(state.getSymbolTable(), state.getHeap());

        if(!value.getType().equals(new StringType())) {
            throw new StatementExecutionException(String.format("%s is not string value", expr));
        }

        StringValue fileName = (StringValue) value;
        IDictionary<String, BufferedReader> fileTable = state.getFileTable();

        if(!fileTable.exists(fileName.getValue())) {
            throw new StatementExecutionException(String.format("%s is not in the file table", value));
        }

        BufferedReader br = fileTable.search(fileName.getValue());
        try {
            br.close();
        }
        catch(IOException e) {
            throw new StatementExecutionException(String.format("Error on closing %s",value));
        }

        fileTable.remove(fileName.getValue());
        state.setFileTable(fileTable);
        return null;
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
