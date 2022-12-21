//
// Created by irina on 25.05.2022.
//

#ifndef GA_LAB5_CUSTOMHASH_H
#define GA_LAB5_CUSTOMHASH_H


#pragma once
#include "edge.h"

class CustomHashFunction {
    int modulo = 666013; // it is a prime
public:
    size_t operator()(const Edge& edge) const;
};


#endif //GA_LAB5_CUSTOMHASH_H
