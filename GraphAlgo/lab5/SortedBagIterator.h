//
// Created by irina on 27.05.2022.
//

#ifndef DSA_SORETEDBAG_LAB5_SORTEDBAGITERATOR_H
#define DSA_SORETEDBAG_LAB5_SORTEDBAGITERATOR_H
#include "SortedBag.h"
#include <vector>
#include <stack>

class SortedBag;

class SortedBagIterator
{
    friend class SortedBag;

private:
    const SortedBag& bag;
    explicit SortedBagIterator(const SortedBag& b);

    SortedBag::BSTNode *current_node;
    int frequency_current_elem;
    std::stack<SortedBag::BSTNode*> stack{};

public:
    TComp getCurrent();
    bool valid();
    void next();
    void first();
};


#endif //DSA_SORETEDBAG_LAB5_SORTEDBAGITERATOR_H
