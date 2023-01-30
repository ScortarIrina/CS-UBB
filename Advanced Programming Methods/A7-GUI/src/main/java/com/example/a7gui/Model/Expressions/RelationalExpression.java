package com.example.a7gui.Model.Expressions;

import com.example.a7gui.Model.ADTs.IDictionary;
import com.example.a7gui.Model.ADTs.IHeap;
import com.example.a7gui.Model.Types.BoolType;
import com.example.a7gui.Model.Types.IType;
import com.example.a7gui.Model.Types.IntType;
import com.example.a7gui.Model.Values.BoolValue;
import com.example.a7gui.Model.Values.IValue;
import com.example.a7gui.Model.Values.IntValue;
import com.example.a7gui.Exceptions.InterpreterException;
import java.util.Objects;

public class RelationalExpression implements IExpression {

    IExpression expression1;
    IExpression expression2;
    String operator;

    public RelationalExpression(IExpression e1, String op, IExpression e2) {
        this.expression1 = e1;
        this.operator = op;
        this.expression2 = e2;
    }

    @Override
    public IValue evaluate(IDictionary<String, IValue> symTable, IHeap heap) throws InterpreterException {
        IValue v1 = this.expression1.evaluate(symTable, heap);

        if(v1.getType().equals(new IntType())) {
            IValue v2 = this.expression2.evaluate(symTable, heap);

            if(v2.getType().equals(new IntType())) {
                int value1 = ((IntValue) v1).getValue();
                int value2 = ((IntValue) v2).getValue();

                if(Objects.equals(operator, "<")) {
                    return new BoolValue(value1 < value2);
                }
                else if(Objects.equals(operator, "<=")) {
                    return new BoolValue(value1 <= value2);
                }
                else if(Objects.equals(operator, "==")) {
                    return new BoolValue(value1 == value2);
                }
                else if(Objects.equals(operator, "!=")) {
                    return new BoolValue(value1 != value2);
                }
                else if(Objects.equals(operator, ">")) {
                    return new BoolValue(value1 > value2);
                }
                else if (Objects.equals(operator, ">=")) {
                    return new BoolValue(value1 >= value2);
                }
                else {
                    throw new InterpreterException("ERROR: Operation does not exist!");
                }
            }
            else {
                throw new InterpreterException("ERROR: Second operand is not int!");
            }
        }
        else {
            throw new InterpreterException("ERROR: First operand in not int!");
        }
    }

    @Override
    public IType typeCheck(IDictionary<String, IType> typeEnv) throws InterpreterException {
        IType type1, type2;
        type1 = expression1.typeCheck(typeEnv);
        type2 = expression2.typeCheck(typeEnv);
        if (type1.equals(new IntType())) {
            if (type2.equals(new IntType())) {
                return new BoolType();
            } else
                throw new InterpreterException("ERROR: Second operand is not an integer!");
        } else
            throw new InterpreterException("ERROR: First operand is not an integer!");

    }

    @Override
    public IExpression deepCopy() {
        return new RelationalExpression(expression1.deepCopy(), operator, expression2.deepCopy());
    }

    @Override
    public String toString() {
        return this.expression1.toString() + " " + this.operator + " " + this.expression2.toString();
    }
}

