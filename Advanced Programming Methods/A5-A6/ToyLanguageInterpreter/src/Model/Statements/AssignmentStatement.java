package Model.Statements;

import Exceptions.ADTException;
import Exceptions.ExpressionEvaluationException;
import Exceptions.StatementExecutionException;
import Model.ADTs.IDictionary;
import Model.Expressions.IExpression;
import Model.ProgramState.ProgramState;
import Model.Values.IValue;
import Model.Types.IType;

public class AssignmentStatement implements IStatement {
    private String key;
    private IExpression expression;

    public AssignmentStatement(String id, IExpression e) {
        this.key = id;
        this.expression = e;
    }

    @Override
    public ProgramState execute(ProgramState state) throws StatementExecutionException, ExpressionEvaluationException, ADTException {
        IDictionary<String, IValue> symbolTable = state.getSymbolTable();

        if (symbolTable.exists(key)) {
            IValue value = expression.evaluate(symbolTable, state.getHeap());
            IType typeId = (symbolTable.search(key)).getType();

            if (value.getType().equals(typeId)) {
                symbolTable.update(key, value);
            } else {
                throw new StatementExecutionException("Declared type of variable " + key + " and type of the assigned expression do not match.");
            }
        } else {
            throw new StatementExecutionException("The used variable " + key + " was not declared before.");
        }
        state.setSymbolTable(symbolTable);
        return null;
    }

    @Override
    public IDictionary<String, IType> typeCheck(IDictionary<String, IType> typeEnv) throws StatementExecutionException, ExpressionEvaluationException, ADTException {
        IType typeVar = typeEnv.search(key);
        IType typeExpr = expression.typeCheck(typeEnv);
        if (typeVar.equals(typeExpr))
            return typeEnv;
        else
            throw new StatementExecutionException("Assignment: right hand side and left hand side have different types.");
    }

    @Override
    public IStatement deepCopy() {
        return new AssignmentStatement(key, expression.deepCopy());
    }


    @Override
    public String toString() {
        return String.format("%s = %s", this.key,this.expression.toString());
    }
}
