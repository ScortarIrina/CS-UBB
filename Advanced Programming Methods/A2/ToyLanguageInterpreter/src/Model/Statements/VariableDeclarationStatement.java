package Model.Statements;

import Exceptions.StatementExecutionException;
import Model.ADTs.IDictionary;
import Model.ProgramState.ProgramState;
import Model.Values.IValue;
import Model.Types.IType;

public class VariableDeclarationStatement implements IStatement {
    String name;
    IType type;

    public VariableDeclarationStatement(String n, IType t) {
        this.name = n;
        this.type = t;
    }

    @Override
    public ProgramState execute(ProgramState state) throws StatementExecutionException {
        IDictionary<String,IValue> symTable = state.getSymbolTable();

        if(symTable.exists(this.name)) {
            throw new StatementExecutionException("Variable " + this.name + " is already declared");
        }

        symTable.put(this.name,this.type.defaultValue());
        state.setSymbolTable(symTable);
        return state;
    }

    @Override
    public IStatement deepCopy() {
        return new VariableDeclarationStatement(name, type);
    }

    @Override
    public String toString() {
        return String.format("%s %s", type.toString(), name);
    }
}