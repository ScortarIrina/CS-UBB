//
// Created by Irina Scortar on 01.07.2022.
//

#ifndef TASK_MANAGER_2_TASKSREPOSITORY_H
#define TASK_MANAGER_2_TASKSREPOSITORY_H

#include "domain/Task.h"
#include "domain/AppException.h"
#include <fstream>
#include <vector>
#include <cstdlib>
#include <algorithm>


class TasksRepository {
    std::vector<Task> tasks;
    std::string filepath;

public:
    explicit TasksRepository(const std::string &filepath);

    virtual ~TasksRepository();

    void add(const Task &task);

    void remove(const std::string& description);

    void update(Task &task);

    std::vector<Task> getAll() { return this->tasks; }
};


#endif //TASK_MANAGER_2_TASKSREPOSITORY_H
