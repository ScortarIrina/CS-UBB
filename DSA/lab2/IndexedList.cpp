#include "IndexedList.h"
#include "ListIterator.h"
#include <exception>
#include <iostream>
using namespace std;


IndexedList::IndexedList() 
{
    this->length = 0;
    this->head = nullptr;
    this->tail = nullptr;
}

int IndexedList::size() const 
{
	return this->length;
}

bool IndexedList::isEmpty() const 
{
    if (this->length == 0)
        return true;
	return false;
}

TElem IndexedList::getElement(int pos) const 
{
    if (pos < 0 || pos >= this->length)
        throw exception();
    else
    {
        DLLNode* currentNode = this->head;
        int index = 0;
        while (currentNode != nullptr)
        {
            if (index == pos)
                return currentNode->info;
            currentNode = currentNode->next;
            index++;
        }
    }
}

TElem IndexedList::setElement(int pos, TElem e) 
{
    if (pos < 0 || pos >= this->length)
        throw exception();
    else
    {
        DLLNode* currentNode = this->head;
        int index = 0;
        TElem nodeValue{};
        while (currentNode != nullptr)
        {
            if (index == pos)
            {
                nodeValue = currentNode->info;
                currentNode->info = e;
            }
            currentNode = currentNode->next;
            index++;
        }
        return nodeValue;
    }
}

void IndexedList::addToEnd(TElem e) 
{
    DLLNode* newNode = new DLLNode();
    newNode->info = e;

    // the list is empty
    if (this->head == nullptr)
    {
        this->head = newNode;
        newNode->prev = nullptr;
        newNode->next = nullptr;
        this->tail = newNode;
        this->length++;
    }
    else
    {
        newNode->prev = this->tail;
        this->tail->next = newNode;
        newNode->next = nullptr;
        this->tail = newNode;
        this->length++;
    }
}

void IndexedList::addToPosition(int pos, TElem e) 
{
    // allocate node to new element
    DLLNode* newNode = new DLLNode();
    newNode->info = e;
    newNode->next = nullptr;
    newNode->prev = nullptr;

    // check if the position is valid
    if (pos < 0 || pos >= this->length)
        throw exception();
    else if(pos == 0)
    {
        // if the position is 0, make new node as head
        newNode->next = this->head;
        this->head->prev = newNode;
        this->head = newNode;
        this->length++;
    }
    else
    {
        // make a temp node and traverse to the node previous to the position
        DLLNode* temp = this->head;
        for (int i = 0; i < pos - 1; i++)
        {
            if (temp != nullptr)
            {
                temp = temp->next;
            }
        }
        // If the previous node is not null, adjust the links
        if (temp != nullptr)
        {
            newNode->next = temp->next;
            newNode->prev = temp;
            temp->next = newNode;
            if (newNode->next != nullptr)
                newNode->next->prev = newNode;
            this->length++;
        }
        else
        {
            // the previous node is null
            throw exception();
        }
    }
}

TElem IndexedList::remove(int pos) 
{
    DLLNode* currentNode = this->head;
    TElem nodeValue{};
    int index;
    if (pos < 0 || pos >= this->length || this->length == 0)
        throw exception();
    else
    {
        for (index = 0; index < pos && currentNode != nullptr; index++)
            currentNode = currentNode->next;

        if (currentNode != nullptr)
            nodeValue = currentNode->info;
        this->length--;

        if (currentNode != nullptr && currentNode == this->head)
            this->head = currentNode->next;

        if (currentNode != nullptr && currentNode->next != nullptr)
            currentNode->next->prev = currentNode->prev;

        if (currentNode != nullptr && currentNode->prev != nullptr)
            currentNode->prev->next = currentNode->next;

        delete currentNode;
    }
    return nodeValue;
}

int IndexedList::search(TElem e) const
{
    DLLNode* currentNode = this->head;
    int index = 0;
    int foundIndex = -1;
    while (currentNode != nullptr && foundIndex == -1)
    {
        if (currentNode->info == e)
            foundIndex = index;
        else
        {
            currentNode = currentNode->next;
            index++;
        }
    }
    return foundIndex;
}

ListIterator IndexedList::iterator() const 
{
    return ListIterator(*this);        
}

IndexedList::~IndexedList() 
{
    DLLNode* prevNode = nullptr;
    DLLNode* currentNode = this->head;
    while (currentNode != nullptr) 
    {
        prevNode = currentNode;
        currentNode = currentNode->next;
        delete prevNode;
    }
}
