package Model.Expressions;

import Exceptions.ADTException;
import Exceptions.ExpressionEvaluationException;
import Model.ADTs.IDictionary;
import Model.ADTs.IHeap;
import Model.Types.IType;
import Model.Values.BoolValue;
import Model.Values.IValue;
import Model.Types.BoolType;

import java.util.Objects;

public class LogicalExpression implements IExpression {
    IExpression expression1;
    IExpression expression2;
    String operation;

    public LogicalExpression(IExpression e1, String op, IExpression e2) {
        this.expression1 = e1;
        this.expression2 = e2;
        this.operation = op;
    }

    @Override
    public IValue evaluate(IDictionary<String, IValue> symTable, IHeap heap) throws ExpressionEvaluationException, ADTException {
        IValue v1, v2;
        v1 = this.expression1.evaluate(symTable, heap);

        if(v1.getType().equals(new BoolType())) {
            v2 = this.expression2.evaluate(symTable, heap);

            if(v2.getType().equals(new BoolType())) {
                BoolValue b1 = (BoolValue)v1;
                BoolValue b2 = (BoolValue)v2;

                if(Objects.equals(this.operation, "and")) {
                    return new BoolValue(b1.getValue() && b2.getValue());
                }
                else if(Objects.equals(this.operation, "or")) {
                    return new BoolValue(b1.getValue() || b2.getValue());
                }
                else {
                    throw new ExpressionEvaluationException("ERROR: Operation is not defined");
                }
            }
            else {
                throw new ExpressionEvaluationException("ERROR: Second operand is not bool");
            }
        }
        else {
            throw new ExpressionEvaluationException("ERROR: First operand is not bool");
        }
    }

    @Override
    public IType typeCheck(IDictionary<String, IType> typeEnv) throws ExpressionEvaluationException, ADTException {
        IType type1, type2;
        type1 = expression1.typeCheck(typeEnv);
        type2 = expression2.typeCheck(typeEnv);
        if (type1.equals(new BoolType())) {
            if (type2.equals(new BoolType())) {
                return new BoolType();
            } else
                throw new ExpressionEvaluationException("Second operand is not a boolean.");
        } else
            throw new ExpressionEvaluationException("First operand is not a boolean.");

    }

    @Override
    public IExpression deepCopy() {
        return new LogicalExpression(expression1.deepCopy(), operation, expression2.deepCopy());
    }


    @Override
    public String toString() {
        return this.expression1.toString() + " " + this.operation + " " + this.expression2.toString();
    }
}
