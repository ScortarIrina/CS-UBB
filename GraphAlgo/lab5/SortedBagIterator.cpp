//
// Created by irina on 27.05.2022.
//

#include "SortedBagIterator.h"
#include "SortedBag.h"
#include <exception>

using namespace std;


/*
 * O(h)
 */
SortedBagIterator::SortedBagIterator(const SortedBag& b)
    : bag(b)
{
    SortedBag::BSTNode *node = this->bag.root;
    while (node != nullptr)
    {
        stack.push(node);
        node = node->left_child;
    }

    /// this->currentElement will point to the leftmost element (the first one)
    if (!stack.empty())
        current_node = stack.top();
    else
        current_node = nullptr;

    frequency_current_elem = 1;
}

/*
 * O(1)
 */
TComp SortedBagIterator::getCurrent()
{
    if (current_node == nullptr)
        throw std::exception();
    return current_node->info;
}

/*
 * O(1)
 */
bool SortedBagIterator::valid()
{
    if (this->current_node != nullptr)
        return true;
    return false;
}

void SortedBagIterator::next()
{
    if (!valid())
    {
        throw exception();
    }

    if (frequency_current_elem < bag.nrOccurrences(current_node->info))
    {
        /// current_node will point to the same node
        /// increase the frequency
        this->frequency_current_elem++;
    }
    else
    {
        SortedBag::BSTNode *node = stack.top();
        stack.pop();
        if (node->right_child != nullptr)
        {
            node = node->right_child;
            while (node != nullptr)
            {
                this->stack.push(node);
                node = node->left_child;
            }
        }
        if (!stack.empty())
            current_node = stack.top();
        else
            current_node = nullptr;
        frequency_current_elem = 1;
    }
}

/*
 * O(h)
 * h = height of the tree
 */
void SortedBagIterator::first()
{
    SortedBag::BSTNode *node = bag.root;
    while (node != nullptr)
    {
        stack.push(node);
        node = node->left_child;
    }
    if (!stack.empty())
        current_node = stack.top();
    else
        current_node = nullptr;
    frequency_current_elem = 1;
}