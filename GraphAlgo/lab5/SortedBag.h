//
// Created by irina on 27.05.2022.
//

#ifndef DSA_SORETEDBAG_LAB5_SORTEDBAG_H
#define DSA_SORETEDBAG_LAB5_SORTEDBAG_H

//DO NOT INCLUDE SORTEDBAGITERATOR

//DO NOT CHANGE THIS PART
typedef int TComp;
typedef TComp TElem;
typedef bool(*Relation)(TComp, TComp);
#define NULL_TCOMP -11111;


class SortedBagIterator;


class SortedBag
{
    friend class SortedBagIterator;

private:
    struct BSTNode
    {
        TComp info;
        BSTNode *left_child;
        BSTNode *right_child;
    } *root;

    int nr_elems;

public:
    /// constructor
    explicit SortedBag(Relation r);

    /// adds an element to the sorted bag
    void add(TComp e);

    /// removes one occurrence of an element from a sorted bag
    /// returns true if an element was removed, false otherwise (if e was not part of the sorted bag)
    bool remove(TComp e);

    /// checks if an element appears is the sorted bag
    bool search(TComp e) const;

    /// returns the number of occurrences for an element in the sorted bag
    int nrOccurrences(TComp e) const;

    /// returns the number of elements from the sorted bag
    int size() const;

    /// returns an iterator for this sorted bag
    SortedBagIterator iterator() const;

    /// adds nr occurrences of elem into the SortedBag
    /// if elem was not in the bag, it will be added
    /// throws an exception if nr. is negative
    void addOccurrences(int nr, TComp elem);

    /// checks if the sorted bag is empty
    bool isEmpty() const;

    /// destructor
    ~SortedBag();

private:
    Relation relation;
};


#endif //DSA_SORETEDBAG_LAB5_SORTEDBAG_H
