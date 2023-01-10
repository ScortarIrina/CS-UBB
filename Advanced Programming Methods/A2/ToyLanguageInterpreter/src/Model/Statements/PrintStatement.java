package Model.Statements;

import Exceptions.ADTException;
import Exceptions.ExpressionEvaluationException;
import Model.ADTs.IList;
import Model.Expressions.IExpression;
import Model.ProgramState.ProgramState;
import Model.Values.IValue;

public class PrintStatement implements IStatement {
    IExpression expr;

    public PrintStatement(IExpression e) {
        this.expr = e;
    }

    @Override
    public ProgramState execute(ProgramState state) throws ExpressionEvaluationException, ADTException {
        IList<IValue> out = state.getOutput();
        out.add(expr.evaluate(state.getSymbolTable(), state.getHeap()));
        state.setOutput(out);
        return state;
    }

    @Override
    public IStatement deepCopy() {
        return new PrintStatement(expr.deepCopy());
    }

    @Override
    public String toString() {
        return String.format("Print(%s)",expr.toString());
    }
}
