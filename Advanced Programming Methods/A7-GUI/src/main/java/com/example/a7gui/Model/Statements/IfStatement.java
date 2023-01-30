package com.example.a7gui.Model.Statements;

import com.example.a7gui.Exceptions.InterpreterException;
import com.example.a7gui.Model.Expressions.IExpression;
import com.example.a7gui.Model.ProgramState.ProgramState;
import com.example.a7gui.Model.Types.BoolType;
import com.example.a7gui.Model.Types.IType;
import com.example.a7gui.Model.Values.*;
import com.example.a7gui.Model.ADTs.*;

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
    public ProgramState execute(ProgramState state) throws InterpreterException {
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
            return null;
        }
        else
            throw new InterpreterException("No boolean expression in the if statement was provided!");
    }

    @Override
    public IDictionary<String, IType> typeCheck(IDictionary<String, IType> typeEnv) throws InterpreterException {
        IType typeExpr = expr.typeCheck(typeEnv);
        if (typeExpr.equals(new BoolType())) {
            thenStatement.typeCheck(typeEnv.deepCopy());
            elseStatement.typeCheck(typeEnv.deepCopy());
            return typeEnv;
        } else
            throw new InterpreterException("The condition of IF does not have the type Bool.");
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
