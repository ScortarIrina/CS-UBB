package Model.Statements;

import Exceptions.ADTException;
import Exceptions.ExpressionEvaluationException;
import Exceptions.StatementExecutionException;
import Model.ADTs.IDictionary;
import Model.Expressions.IExpression;
import Model.ProgramState.ProgramState;
import Model.Types.IType;
import Model.Types.StringType;
import Model.Values.IValue;
import Model.Values.StringValue;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;

public class OpenReadFile implements IStatement {
    private IExpression expr;

    public OpenReadFile(IExpression expr) {
        this.expr = expr;
    }

    @Override
    public ProgramState execute(ProgramState state) throws StatementExecutionException, ExpressionEvaluationException, ADTException {
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
                    throw new StatementExecutionException(String.format("%s could not be opened", fileName.getValue()));
                }

                fileTable.put(fileName.getValue(),br);
                state.setFileTable(fileTable);
            }
            else
                throw new StatementExecutionException(String.format("%s is already opened",fileName.getValue()));
        }
        else
            throw new StatementExecutionException(String.format("%s is not string type",expr.toString()));

        return null;
    }

    @Override
    public IDictionary<String, IType> typeCheck(IDictionary<String, IType> typeEnv) throws StatementExecutionException, ExpressionEvaluationException, ADTException {
        if (expr.typeCheck(typeEnv).equals(new StringType()))
            return typeEnv;
        else
            throw new StatementExecutionException("OpenReadFile requires a string expression.");
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
