package Model.Statements;

import Exceptions.ADTException;
import Exceptions.ExpressionEvaluationException;
import Exceptions.StatementExecutionException;
import Model.Expressions.IExpression;
import Model.ProgramState.ProgramState;
import Model.Types.BoolType;
import Model.ADTs.IStack;
import Model.Values.BoolValue;
import Model.Values.IValue;

public class WhileStatement implements IStatement {
    private final IExpression expression;
    private final IStatement statement;

    public WhileStatement(IExpression expression, IStatement statement) {
        this.expression = expression;
        this.statement = statement;
    }

    @Override
    public ProgramState execute(ProgramState state) throws StatementExecutionException, ExpressionEvaluationException, ADTException {
        IValue value = expression.evaluate(state.getSymbolTable(), state.getHeap());
        IStack<IStatement> stack = state.getExecutionStack();
        if (!value.getType().equals(new BoolType()))
            throw new StatementExecutionException(String.format("%s is not of type boolean", value));
        BoolValue boolValue = (BoolValue) value;
        if (boolValue.getValue()) {
            stack.push(this);
            stack.push(statement);
        }
        return state;
    }

    @Override
    public IStatement deepCopy() {
        return new WhileStatement(expression.deepCopy(), statement.deepCopy());
    }

    @Override
    public String toString() {
        return String.format("while(%s){%s}", expression, statement);
    }

}
