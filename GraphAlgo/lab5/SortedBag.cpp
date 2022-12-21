//
// Created by irina on 27.05.2022.
//

#include "SortedBag.h"
#include "SortedBagIterator.h"
#include <stack>

/*
 * O(1)
 */
SortedBag::SortedBag(Relation r)
{
    this->root = new BSTNode;
    this->root->left_child = nullptr;
    this->root->right_child = nullptr;
    this->root->info = 0;
    this->nr_elems = 0;
    this->relation = r;
}

/*
 * WC: O(n)
 * AC: O(h)
 * h = height of the tree
 */
void SortedBag::add(TComp e)
{
    auto *temp = new BSTNode;
    temp->info = e;
    temp->left_child = nullptr;
    temp->right_child = nullptr;

    BSTNode *new_node = temp;
    BSTNode *current = root;
    BSTNode *prev = nullptr;

    while (current != nullptr)
    {
        prev = current;
        if (e < current->info)
            current = current->left_child;
        else
            current = current->right_child;
    }
    if (prev == nullptr)
    {
        prev = new_node;
        root = prev;
    }
    else if (e < prev->info)
        prev->left_child = new_node;
    else
        prev->right_child = new_node;

    this->nr_elems++;
}

/*
 * WC: O(n)
 * AC: O(h)
 * h = height of the tree
 */
bool SortedBag::remove(TComp e)
{
    /// current pointer to iterate
    BSTNode * stat = root;

    /// one previous pointer from current
    BSTNode *prev = nullptr;

    /// Iterating in BST to check if the key with value data is actually present there or not
    while (stat != nullptr && stat->info != e)
    {
        prev = stat;
        if (e < stat->info)
            stat = stat->left_child;
        else
            stat = stat->right_child;
    }
    /// value not found in BST
    if (stat == nullptr)
        return false;

    /// check if the node to be deleted has either 0 or 1 child
    if (stat->left_child == nullptr || stat->right_child == nullptr)
    {
        /// new_tree_node will store the node to be deleted
        BSTNode *new_tree_node;

        if (stat->left_child == nullptr)
            new_tree_node = stat->right_child;
        else
            new_tree_node = stat->left_child;

        /// check if the node to be deleted is the root
        if (prev == nullptr)
        {
            this->root = nullptr;
            this->nr_elems--;
            return true;
        }
        /// check the node to be deleted  is whether the previous nodes left or right
        /// and replace it with the new_tree_node
        if (stat == prev->left_child)
            prev->left_child = new_tree_node;
        else
            prev->right_child = new_tree_node;

        /// simply delete the node
        delete stat;
    }

    /// Node which has to be deleted has 2 child nodes
    else
    {
        BSTNode *previous = nullptr;
        BSTNode *temp;

        /// finding the inorder successor in case of node with 2 child nodes
        temp = stat->right_child;
        while (temp->left_child != nullptr)
        {
            previous = temp;
            temp = temp->left_child;
        }

        /// before replacing the value check if the parent node of the inorder successor
        /// is the current node or not if it is not then make the left child of the parent
        /// equal to the inorder successor of the right child else if inorder successor was
        /// itself  the current then make the right child of the node to be deleted equal
        /// to the right child of inorder successor
        previous!=nullptr?previous->left_child = temp->right_child:stat->right_child=temp->right_child;
        stat->info = temp->info;
        delete temp;
    }
    this->nr_elems--;
    return true;
}

/*
 * BC: O(1)
 * WC: O(n)
 * AC: O(h)
 * h = height of the tree
 */
bool SortedBag::search(TComp elem) const
{
    /// BASE CASES:
    /// 1. root is NULL
    if (root == nullptr)
        return false;
    /// 2. the element we're looking for is at root's info
    if (root->info == elem)
        return true;

    /// current pointer to iterate
    BSTNode *current_node = this->root;
    bool found = false;
    while (current_node != nullptr && !found)
    {
        /// the elem is at the current node
        if (current_node->info == elem)
            found = true;
        /// elem is smaller than current_node's info, so we search is the left child
        else if (elem <= current_node->info)
            current_node = current_node->left_child;
        /// elem is greater or equal than current_node's info, so we search is the right child
        else
            current_node = current_node->right_child;
    }
    return found;
}

/*
 * O(n)
 */
int SortedBag::nrOccurrences(TComp elem) const
{
    std::stack<BSTNode*> stack;
    BSTNode *current_node = root;
    int counter = 0;
    while (current_node != nullptr || !stack.empty())
    {
        while (current_node != nullptr)
        {
            stack.push(current_node);
            current_node = current_node->left_child;
        }
        current_node = stack.top();
        stack.pop();
        if (current_node->info == elem)
            counter++;
        current_node = current_node->right_child;
    }
    return counter;
}

/*
 * O(1)
 */
int SortedBag::size() const
{
    return nr_elems;
}

/*
 * O(1)
 */
bool SortedBag::isEmpty() const
{
    return (nr_elems == 0);
}

/*
 * adds nr occurrences of elem into the SortedBag
 * if elem was not in the bag, it will be added
 * throws an exception if nr. is negative
 */
void SortedBag::addOccurrences(int nr, TComp elem)
{
    if (nr < 0)
        throw std::exception();
    while (nr > 0)
    {
        add(elem);
        nr--;
    }
}

/*
 * O(1)
 */
SortedBagIterator SortedBag::iterator() const
{
    return SortedBagIterator(*this);
}

/*
 * O(1)
 */
SortedBag::~SortedBag()
{
    delete[] root;
}
