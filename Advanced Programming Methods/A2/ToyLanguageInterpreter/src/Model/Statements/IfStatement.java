package Model.Statements;
import Exceptions.ADTException;
import Exceptions.ExpressionEvaluationException;
import Exceptions.StatementExecutionException;
import Model.Expressions.IExpression;
import Model.ProgramState.ProgramState;
import Model.Values.*;
import Model.ADTs.*;

public class IfStatement implements IStatement {
    IExpression expr;
    IStatement thenStatement;
    IStatement elseStatement;

    public IfStatement(IExpression e, IStatement thenS, IStatement elseS) {
        this.expr= e;
        this.thenStatement = thenS;
        this.elseStatement = elseS;
    }

    @Override
    public ProgramState execute(ProgramState state) throws StatementExecutionException, ExpressionEvaluationException, ADTException {
        IValue result = this.expr.evaluate(state.getSymbolTable(), state.getHeap());

        if (result instanceof BoolValue boolResult) {
            IStatement statement;
            if (boolResult.getValue())
                statement = thenStatement;
            else
                statement = elseStatement;

            IStack<IStatement> stack = state.getExecutionStack();
            stack.push(statement);
            state.setExecutionStack(stack);
            return state;
        }
        else
            throw new StatementExecutionException("No boolean expression in the if statement was provided!");
    }

    @Override
    public IStatement deepCopy() {
        return new IfStatement(expr.deepCopy(), thenStatement.deepCopy(), elseStatement.deepCopy());
    }

    @Override
    public String toString() {
        return String.format("if(%s) {%s} else{%s}", expr.toString(), thenStatement.toString(), elseStatement.toString());
    }
}
