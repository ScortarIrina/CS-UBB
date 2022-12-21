//
// Created by irina on 27.05.2022.
//

#include "ShortTest.h"
#include "SortedBag.h"
#include "SortedBagIterator.h"
#include <cassert>
#include <exception>

bool relation(TComp e1, TComp e2) {
    return e1 <= e2;
}

void testAll() {
    SortedBag sb(relation);
    sb.add(5);
    sb.add(6);
    sb.add(0);
    sb.add(5);
    sb.add(10);
    sb.add(8);

    assert(sb.size() == 6);
    assert(sb.nrOccurrences(5) == 2);

    assert(sb.remove(5) == true);
    assert(sb.size() == 5);

    assert(sb.search(6) == true);
    assert(sb.isEmpty() == false);

    SortedBagIterator it = sb.iterator();
    assert(it.valid() == true);
    while (it.valid()) {
        it.getCurrent();
        it.next();
    }
    assert(it.valid() == false);
    it.first();
    assert(it.valid() == true);


   /// extra operation
    SortedBag sorted_bag(relation);
    sorted_bag.add(5);
    sorted_bag.addOccurrences(3, 5);
    assert(sorted_bag.size() == 4);

    sorted_bag.addOccurrences(3, 1);
    assert(sorted_bag.search(1) == true);
    assert(sorted_bag.size() == 7);
}
