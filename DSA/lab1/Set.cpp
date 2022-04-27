#include "Set.h"
#include "SetITerator.h"
#include <exception>

Set::Set(int capacity, int capacity_bool)
{
	if (capacity <= 0 || capacity_bool <= 0)
		throw std::exception();

	this->length = 0;
	this->capacity = capacity;
	this->elems = new TElem[capacity];

	this->length_bool = 0;
	this->capacity_bool = capacity_bool;
	this->elems_bool = new TElemBool[capacity_bool];
}

// WC: O(this->length_bool)
// BC: O(1)
bool Set::add(TElem elem)
{
	if (search(elem) == true)
		return false;  // the element is already in the array

	// the element is not in the array
	if (this->length == this->capacity)
		//throw std::exception();
		this->resize();
	this->elems[this->length] = elem;
	this->length++;

	TElem min = getMinimum();
	TElem max = getMamimum();
	int index_bool = -1;
	this->length_bool = max - min;

	while (min < max)
	{
		if (this->length_bool > this->capacity_bool)
			//throw std::exception();
			resizeBool();
		if (search(min) == true)
			this->elems_bool[++index_bool] = true;
		else
			this->elems_bool[++index_bool] = false;
		min++;
	}
	return true;
}

// BC: O(1)
// WC: O(n)
bool Set::remove(TElem elem) 
{
	int i;
	for (i = 0; i < this->length; i++)
		if (this->elems[i] == elem)
			break;
	if (i < this->length)
	{
		this->elems[i] = this->elems[this->length - 1];
		this->length--;
		this->elems_bool[i] = false;
		return true;
	}
	return false;
}

// BC: O(1)
// WC: O(n)
TElem Set::getMinimum()
{
	TElem min = this->elems[0];
	for (int i = 1; i < this->length; i++)
		if (this->elems[i] < min)
		{
			min = this->elems[i];
			return min;
		}
	return min;
}

// BC: O(1)
// WC: O(n)
TElem Set::getMamimum()
{
	TElem max = this->elems[0];
	for (int i = 1; i < this->length; i++)
		if (this->elems[i] > max)
		{
			max = this->elems[i];
			return max;
		}
	return max;
}

// BC: O(1)
// WC: O(n)
bool Set::search(TElem elem) const 
{
	for (int i = 0; i < this->length; i++)
	{
		if (this->elems[i] == elem)
			return true;
	}
	return false;
}

int Set::size() const 
{
	return this->length;
}

bool Set::isEmpty() const 
{
	if (this->length == 0)
		return true;
	return false;
}

Set::~Set() 
{
	delete this->elems;
	delete this->elems_bool;
}

// O(2*nr_elements)
void Set::resize(double factor)
{
	this->capacity *= this->capacity;
	TElem* aux = new TElem[this->capacity];

	for (int i = 0; i < this->length; i++)
		aux[i] = this->elems[i];

	delete[] this->elems;
	this->elems = aux;
}

// O(2*nr_elements)
void Set::resizeBool(double factor)
{
	this->capacity_bool *= this->capacity_bool;
	TElemBool* aux = new TElemBool[this->capacity_bool];

	for (int i = 0; i < this->length_bool; i++)
		aux[i] = this->elems_bool[i];

	delete[] this->elems_bool;
	this->elems_bool = aux;
}

// O(this->length + this->length_bool)
void Set::empty()
{
	for (int i = 0; i < this->length; i++)
		remove(this->elems[i]);
	for (int i = 0; i < this->length_bool; i++)
		remove(this->elems_bool[i]);

	this->length = 0;
	this->length_bool = 0;
}

SetIterator Set::iterator() const 
{
	return SetIterator(*this);
}
