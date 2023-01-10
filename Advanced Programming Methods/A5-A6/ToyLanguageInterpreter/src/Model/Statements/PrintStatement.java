package Model.Statements;

import Exceptions.ADTException;
import Exceptions.ExpressionEvaluationException;
import Exceptions.StatementExecutionException;
import Model.ADTs.IDictionary;
import Model.ADTs.IList;
import Model.Expressions.IExpression;
import Model.ProgramState.ProgramState;
import Model.Types.IType;
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
        return null;
    }

    @Override
    public IDictionary<String, IType> typeCheck(IDictionary<String, IType> typeEnv) throws StatementExecutionException, ExpressionEvaluationException, ADTException {
        expr.typeCheck(typeEnv);
        return typeEnv;
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
