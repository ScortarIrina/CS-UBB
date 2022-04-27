#pragma once
#include "Tutorial.h"
// Define the DynamicVector class which provides 
// the specific operations: add, remove, length, etc.


//typedef Tutorial TElem;
template <typename T>
class DynamicVector
{
private:
	T* elems;
	int length;
	int capacity;

public:
	// default constructor for a DynamicVector
	DynamicVector(int capacity = 10);

	// copy constructor for a DynamicVector
	DynamicVector(const DynamicVector& v);

	// destructor
	~DynamicVector();

	// assignment operator for a DynamicVector
	DynamicVector& operator=(const DynamicVector& v);

	// addition operator for a DynamicVector with a TElem
	void operator+(/*DynamicVector& v, */const T& t);

	// addition operator for a TElem with a DynamicVector
	friend void operator+(const T& t, DynamicVector& v)
	{
		if (v.capacity == v.length)
			v.resize();
		v.elems[v.length] = t;
		v.length++;
	}

	// subscript operator overloading
	T& operator[](int pos);

	// adds an element to the current DynamicVector
	void addElem(const T& e);

	// returns the number of elements from the DynamicVector
	int getLength() const;

	// returns all elements from the DynamicVector
	T* getAllElems() const;

	// deletes an element from the current DynamicVector
	void deleteElem(int pos);

private:
	// resizes the current DynamicVector, multiplying its capacity by a given factor (real number)
	void resize(double factor = 2);
};

template <typename T>
DynamicVector<T>::DynamicVector(int capacity)
{
	this->length = 0;
	this->capacity = capacity;
	this->elems = new T[capacity];
}

template <typename T>
DynamicVector<T>::DynamicVector(const DynamicVector& v)
{
	this->length = v.length;
	this->capacity = v.capacity;
	this->elems = new T[this->capacity];

	for (int i = 0; i < this->length; i++)
		this->elems[i] = v.elems[i];
}

template <typename T>
DynamicVector<T>::~DynamicVector()
{
	delete[] this->elems;
}

template <typename T>
DynamicVector<T>& DynamicVector<T>::operator=(const DynamicVector<T>& v)
{
	if (this == &v)
		return *this;
	this->length = v.length;
	this->capacity = v.capacity;
	delete[] this->elems;
	this->elems = new T[this->capacity];

	for (int i = 0; i < this->capacity; i++)
		this->elems[i] = v.elems[i];

	return *this;
}

template<typename T>
inline void DynamicVector<T>::operator+(const T& t)
{
	if (this->capacity == this->length)
		this->resize();
	this->elems[this->length] = t;
	this->length++;
}

template <typename T>
T& DynamicVector<T>::operator[](int pos)
{
	return this->elems[pos];
}

template <typename T>
void DynamicVector<T>::addElem(const T& elem)
{
	if (this->length == this->capacity)
		this->resize();
	this->elems[this->length] = elem;
	this->length++;
}

template <typename T>
int DynamicVector<T>::getLength() const
{
	return this->length;
}

template <typename T>
T* DynamicVector<T>::getAllElems() const
{
	return this->elems;
}

template <typename T>
void DynamicVector<T>::resize(double factor)
{
	this->capacity *= 2;
	T* aux = new T[this->capacity];

	for (int i = 0; i < this->length; i++)
		aux[i] = this->elems[i];

	delete[] this->elems;
	this->elems = aux;
}

template <typename T>
void DynamicVector<T>::deleteElem(int pos)
{
	for (int i = pos; i < this->length - 1; i++)
		this->elems[i] = this->elems[i + 1];
	this->length--;
}

//template <typename T>
//void operator+(/*DynamicVector<T>& v, */const T& t)
//{
//	if (this->capacity == this->length)
//		v.resize();
//	this->elems[this->length] = t;
//	this->length++;
//}

//template <typename T>
//void operator+(const T& t, DynamicVector<T>& v)
//{
//	v + t;
//}
