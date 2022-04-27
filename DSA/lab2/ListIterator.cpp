#include "ListIterator.h"
#include "IndexedList.h"
#include <iostream>
#include <exception>
using namespace std;

// O(1)
ListIterator::ListIterator(const IndexedList& list) : list(list)
{
    this->currentNode = list.head;
}

// O(1)
void ListIterator::first()
{
    this->currentNode = this->list.head;
}

// O(1)
void ListIterator::next()
{
    if (this->currentNode != nullptr)
        this->currentNode = this->currentNode->next;
    else
        throw exception();
}

// O(1)
bool ListIterator::valid() const
{
    if (this->currentNode == nullptr)
        return false;
    return true;
}

// O(1)
TElem ListIterator::getCurrent() const
{
    if (this->currentNode == nullptr)
        throw exception();
    return this->currentNode->info;
}
