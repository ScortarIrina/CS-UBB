//
// Created by Irina Scortar on 01.07.2022.
//

#include "Controller.h"
#include <algorithm>

std::vector<Task> Controller::getTasksSortedByStatus() {
    std::vector<Task> students_sorted_by_status = this->tasks.getAll();

    std::sort(students_sorted_by_status.begin(), students_sorted_by_status.end(),
              [](const Task& first, const Task& second)
              {
                  return first.getStatus() < second.getStatus();
              });

    return students_sorted_by_status;
}

void Controller::addTask(const std::string& description, Programmer &programmer) {
    if (description.empty())
        throw AppException("Description cannot be empty!");

    Task t;
    t.setDescription(description);
    t.setStatus("open");
    t.setProgrammerId(programmer.getId());
    this->tasks.add(t);
    this->notify();
}

void Controller::removeTask(const std::string& description) {
    if (description.empty())
        throw AppException("Description cannot be empty!");

    this->tasks.remove(description);
    this->notify();
}

void Controller::updateTask(std::string description, std::string updated_status) {
    std::vector<Task> allTasks = this->tasks.getAll();
    for (auto task : allTasks) {
        if (task.getDescription() == description) {
            if (updated_status == "IN_PROGRESS" && task.getStatus() != "OPEN")
                throw AppException("You have to start working on an open task!");
            task.setStatus(updated_status);
            this->tasks.update(task);
            this->notify();
        }
    }
}



