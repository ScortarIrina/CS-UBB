package Model.Statements;

import Exceptions.ADTException;
import Exceptions.ExpressionEvaluationException;
import Exceptions.StatementExecutionException;
import Model.ProgramState.ProgramState;

public interface IStatement {
    ProgramState execute(ProgramState state) throws StatementExecutionException, ExpressionEvaluationException, ADTException;

    IStatement deepCopy();
}
