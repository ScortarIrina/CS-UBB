package Model.Statements;

import Exceptions.ADTException;
import Exceptions.ExpressionEvaluationException;
import Exceptions.StatementExecutionException;
import Model.ADTs.IDictionary;
import Model.ADTs.IStack;
import Model.ADTs.MyDictionary;
import Model.ADTs.MyStack;
import Model.ProgramState.ProgramState;
import Model.Types.IType;
import Model.Values.IValue;

import java.util.Map;

public class ForkStatement implements IStatement {
    private final IStatement statement;

    public ForkStatement(IStatement statement ){
        this.statement = statement;
    }

    @Override
    public ProgramState execute(ProgramState state) throws StatementExecutionException, ExpressionEvaluationException, ADTException {
        IStack<IStatement> newStack = new MyStack<>();
        newStack.push(statement);
        IDictionary<String, IValue> newSymTable = new MyDictionary<>();
        for (Map.Entry<String, IValue> entry: state.getSymbolTable().getContent().entrySet()) {
            newSymTable.put(entry.getKey(), entry.getValue().deepCopy());
        }

        return new ProgramState(newStack, newSymTable, state.getOutput(), state.getFileTable(), state.getHeap());
    }

    @Override
    public IDictionary<String, IType> typeCheck(IDictionary<String, IType> typeEnv) throws StatementExecutionException, ExpressionEvaluationException, ADTException {
        statement.typeCheck(typeEnv.deepCopy());
        return typeEnv;
    }

    @Override
    public IStatement deepCopy() {
        return new ForkStatement(statement.deepCopy());
    }

    @Override
    public String toString() {
        return String.format("Fork(%s)", statement.toString());
    }
}
