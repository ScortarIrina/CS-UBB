//
// Created by Irina Scortar on 01.07.2022.
//

#ifndef TASK_MANAGER_2_CONTROLLER_H
#define TASK_MANAGER_2_CONTROLLER_H

#include "repository/TasksRepository.h"
#include "repository/ProgrammersRepository.h"
#include "domain/Subject.h"


class Controller : public Subject {
    TasksRepository &tasks;
    ProgrammersRepository &programmers;

public:
    Controller(TasksRepository &tasks, ProgrammersRepository &programmers)
        : tasks(tasks), programmers(programmers) {}

    std::vector<Task> getAllTasks() { return this->tasks.getAll(); }

    std::vector<Programmer> getAllProgrammers() { return this->programmers.getAll(); }

    std::vector<Task> getTasksSortedByStatus();

    void addTask(const std::string& description, Programmer &programmer);

    void removeTask(const std::string& description);

    void updateTask(std::string description, std::string updated_status);

    ~Controller() = default;
};


#endif //TASK_MANAGER_2_CONTROLLER_H
