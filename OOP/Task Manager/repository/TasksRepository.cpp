//
// Created by Irina Scortar on 01.07.2022.
//

#include "TasksRepository.h"

TasksRepository::~TasksRepository() {
    std::ofstream g(this->filepath);
    for(const auto& entity : tasks){
        g << entity << "\n";
    }
    g.close();
}

void TasksRepository::add(const Task &task) {
    this->tasks.push_back(task);
}

void TasksRepository::remove(const std::string& description) {
    int pos = -1;
    for(int i = 0; i < this->tasks.size(); i++) {
        if (this->tasks[i].getDescription() == description) {
            pos = i;
            break;
        }
    }
    if (pos == -1) {
        throw AppException("There is no task with this description!");
    }
    else {
        this->tasks.erase(this->tasks.begin() + pos);
    }
}

void TasksRepository::update(Task &task) {
    for(auto& t : this->tasks){
        if(t.getDescription() == task.getDescription()) {
            t = task;
            return;
        }
    }
}

TasksRepository::TasksRepository(const std::string &filepath) : filepath(filepath) {
    std::ifstream f(filepath);
    if(!f){
        throw AppException("File " + filepath + " doesn't exist");
    }

    this->tasks = {};
    Task t;

    while(f >> t){
        this->tasks.push_back(t);
    }
    f.close();
}
