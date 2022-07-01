//
// Created by Irina Scortar on 01.07.2022.
//

#ifndef TASK_MANAGER_2_PROGRAMMERSREPOSITORY_H
#define TASK_MANAGER_2_PROGRAMMERSREPOSITORY_H

#include "domain/Programmer.h"
#include "domain/AppException.h"
#include <fstream>
#include <vector>
#include <cstdlib>
#include <algorithm>


class ProgrammersRepository {
    std::vector<Programmer> programmers;
    std::string filepath;

public:
    explicit ProgrammersRepository(const std::string &filepath);

    virtual ~ProgrammersRepository();

    void add(const Programmer &programmer);

    void remove(const int& id);

    void update(Programmer &programmer);

    std::vector<Programmer> getAll() { return this->programmers; }
};


#endif //TASK_MANAGER_2_PROGRAMMERSREPOSITORY_H
