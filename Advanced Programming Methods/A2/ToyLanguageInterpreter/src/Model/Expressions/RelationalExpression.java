package Model.Expressions;

import Exceptions.ADTException;
import Exceptions.ExpressionEvaluationException;
import Model.ADTs.IDictionary;
import Model.ADTs.IHeap;
import Model.Types.IntType;
import Model.Values.BoolValue;
import Model.Values.IValue;
import Model.Values.IntValue;

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
    public IValue evaluate(IDictionary<String, IValue> symTable, IHeap heap) throws ExpressionEvaluationException, ADTException {
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
                    throw new ExpressionEvaluationException("ERROR: Operation does not exist");
                }
            }
            else {
                throw new ExpressionEvaluationException("ERROR: Second operand is not int");
            }
        }
        else {
            throw new ExpressionEvaluationException("ERROR: First operand in not int");
        }
    }

    @Override
    public IExpression deepCopy() {
        return new RelationalExpression(expression1.deepCopy(),operator, expression2.deepCopy());
    }

    @Override
    public String toString() {
        return this.expression1.toString() + " "+this.operator+" "+this.expression2.toString();
    }
}
