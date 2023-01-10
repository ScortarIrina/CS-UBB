package Model.Expressions;

import Exceptions.ADTException;
import Exceptions.ExpressionEvaluationException;
import Model.ADTs.IDictionary;
import Model.ADTs.IHeap;
import Model.Types.IType;
import Model.Values.IValue;

public interface IExpression
{
    IValue evaluate(IDictionary<String,IValue> symTable, IHeap heap) throws ExpressionEvaluationException, ADTException;
    IExpression deepCopy();
    IType typeCheck(IDictionary<String, IType> typeEnv) throws ExpressionEvaluationException, ADTException;
}
