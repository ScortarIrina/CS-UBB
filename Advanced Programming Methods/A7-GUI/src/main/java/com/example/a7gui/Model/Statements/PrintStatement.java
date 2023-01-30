package com.example.a7gui.Model.Statements;

import com.example.a7gui.Exceptions.InterpreterException;
import com.example.a7gui.Model.ADTs.IDictionary;
import com.example.a7gui.Model.ADTs.IList;
import com.example.a7gui.Model.Expressions.IExpression;
import com.example.a7gui.Model.ProgramState.ProgramState;
import com.example.a7gui.Model.Types.IType;
import com.example.a7gui.Model.Values.IValue;

public class PrintStatement implements IStatement {
    IExpression expr;

    public PrintStatement(IExpression e) {
        this.expr = e;
    }

    @Override
    public ProgramState execute(ProgramState state) throws InterpreterException {
        IList<IValue> out = state.getOutput();
        out.add(expr.evaluate(state.getSymbolTable(), state.getHeap()));
        state.setOutput(out);
        return null;
    }

    @Override
    public IDictionary<String, IType> typeCheck(IDictionary<String, IType> typeEnv) throws InterpreterException {
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
