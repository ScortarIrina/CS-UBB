package com.example.a7gui.Model.Expressions;

import com.example.a7gui.Model.ADTs.IDictionary;
import com.example.a7gui.Model.ADTs.IHeap;
import com.example.a7gui.Model.Types.IType;
import com.example.a7gui.Model.Types.IntType;
import com.example.a7gui.Model.Values.IValue;
import com.example.a7gui.Model.Values.IntValue;
import com.example.a7gui.Exceptions.InterpreterException;

public class ArithmeticExpression implements IExpression {
    IExpression expression1;
    IExpression expression2;
    char operation;

    public ArithmeticExpression(IExpression e1, char op, IExpression e2) {
        this.expression1 = e1;
        this.expression2 = e2;
        this.operation = op;
    }

    @Override
    public IValue evaluate(IDictionary<String, IValue> symTable, IHeap heap) throws InterpreterException {
        IValue v1, v2;
        v1 = expression1.evaluate(symTable, heap);
        if (v1.getType().equals(new IntType())) {
            v2 = expression2.evaluate(symTable, heap);

            if (v2.getType().equals(new IntType())) {
                IntValue i1 = (IntValue) v1;
                IntValue i2 = (IntValue) v2;

                if (this.operation == '+') {
                    return new IntValue(i1.getValue() + i2.getValue());
                }
                else if (this.operation == '-') {
                    return new IntValue(i1.getValue() - i2.getValue());
                }
                else if (this.operation == '*') {
                    return new IntValue(i1.getValue() * i2.getValue());
                }
                else if (this.operation == '/') {
                    if (i2.getValue() != 0)
                        return new IntValue(i1.getValue() / i2.getValue());
                    else
                        throw new InterpreterException("ERROR: Division by 0!");
                }
                else
                    throw new InterpreterException("ERROR: Operation is not defined!");
            } else
                throw new InterpreterException("ERROR: Second operand is not int!");
        } else
            throw new InterpreterException("ERROR: First operand is not int!");
    }

    @Override
    public IType typeCheck(IDictionary<String, IType> typeEnv) throws InterpreterException {
        IType type1, type2;
        type1 = expression1.typeCheck(typeEnv);
        type2 = expression2.typeCheck(typeEnv);
        if (type1.equals(new IntType())) {
            if (type2.equals(new IntType())) {
                return new IntType();
            } else
                throw new InterpreterException("ERROR: Second operand is not an integer!");
        } else
            throw new InterpreterException("ERROR: First operand is not an integer!");
    }

    @Override
    public IExpression deepCopy() {
        return new ArithmeticExpression(expression1.deepCopy(), operation, expression2.deepCopy());
    }

    @Override
    public String toString()
    {
        return expression1.toString() + " " + operation + " "+ expression2.toString();
    }

}

