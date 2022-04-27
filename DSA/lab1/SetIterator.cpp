#include "SetIterator.h"
#include "Set.h"
#include <exception>
using namespace std;


SetIterator::SetIterator(const Set& m) : set(m)
{
	this->current_index = 0;
}


void SetIterator::first() 
{
	this->current_index = 0;
}


void SetIterator::next() 
{
	if (this->current_index < this->set.length)
		this->current_index++;
	else
		throw std::exception();
}


TElem SetIterator::getCurrent()
{
	if (this->valid())
		return this->set.elems[this->current_index];
	else
		throw std::exception();
}

bool SetIterator::valid() const 
{
	return this->current_index < this->set.length;
}
