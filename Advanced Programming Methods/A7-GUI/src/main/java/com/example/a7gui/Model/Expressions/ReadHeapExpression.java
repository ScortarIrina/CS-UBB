package com.example.a7gui.Model.Expressions;

import com.example.a7gui.Model.ADTs.IDictionary;
import com.example.a7gui.Model.ADTs.IHeap;
import com.example.a7gui.Model.Types.IType;
import com.example.a7gui.Model.Types.ReferenceType;
import com.example.a7gui.Model.Values.IValue;
import com.example.a7gui.Model.Values.ReferenceValue;
import com.example.a7gui.Exceptions.InterpreterException;

public class ReadHeapExpression implements IExpression {

    private final IExpression expression;

    public ReadHeapExpression(IExpression expression) {
        this.expression = expression;
    }

    @Override
    public IValue evaluate(IDictionary<String, IValue> symbolTable, IHeap heap) throws InterpreterException {
        // the expression must be evaluated to a ReferenceValue
        IValue value = expression.evaluate(symbolTable, heap);
        if (!(value instanceof ReferenceValue)) {
            throw new InterpreterException(String.format("ERROR: %s not of type reference!", value));
        }

        // take the address of the ReferenceValue and use it to access Heap table
        ReferenceValue refValue = (ReferenceValue) value;
        return heap.get(refValue.getAddress());
    }

    @Override
    public IType typeCheck(IDictionary<String, IType> typeEnv) throws InterpreterException {
        IType type = expression.typeCheck(typeEnv);
        if (type instanceof ReferenceType) {
            ReferenceType refType = (ReferenceType) type;
            return refType.getInner();
        } else
            throw new InterpreterException("ERROR: The readHeap argument is not a ReferenceType!");
    }

    @Override
    public String toString() {
        return String.format("ReadHeap(%s)", expression);
    }

    @Override
    public IExpression deepCopy() {
        return new ReadHeapExpression(expression.deepCopy());
    }
}

