package Model.Expressions;

import Exceptions.ADTException;
import Exceptions.ExpressionEvaluationException;
import Model.ADTs.IDictionary;
import Model.ADTs.IHeap;
import Model.Values.IValue;

public interface IExpression
{
    IValue evaluate(IDictionary<String,IValue> symTable, IHeap heap) throws ExpressionEvaluationException, ADTException;
    IExpression deepCopy();
}
