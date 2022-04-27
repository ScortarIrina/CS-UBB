#pragma once
#include "IndexedList.h"
class IndexedList;

class ListIterator
{
    //DO NOT CHANGE THIS PART
	friend class IndexedList;

private:
	const IndexedList& list;
    ListIterator(const IndexedList& list);
    IndexedList::DLLNode* currentNode;

public:
    void first();
    void next();
    bool valid() const;
    TElem getCurrent() const;

};

