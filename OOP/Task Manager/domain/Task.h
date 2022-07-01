//
// Created by Irina Scortar on 01.07.2022.
//

#ifndef TASK_MANAGER_2_TASK_H
#define TASK_MANAGER_2_TASK_H

#include <string>
#include <vector>
#include <sstream>
#include <iostream>


class Task {
private:
    std::string description;
    std::string status;
    int programmer_id;

public:
    Task() = default;

    Task(std::string description, std::string status, int programmer_id)
        : description(description), status(status), programmer_id(programmer_id) {}

    ~Task() = default;

    /// getters
    std::string getDescription() const { return this->description; }
    std::string getStatus() const { return this->status; }
    int getProgrammerId() const { return this->programmer_id; }

    /// setters
    void setDescription(std::string new_description) { this->description = new_description; }
    void setStatus(std::string new_status) { this->status = new_status; }
    void setProgrammerId(int new_programmer_id) { this->programmer_id = new_programmer_id; }

    /// overloading operators
    friend std::ostream &operator<<(std::ostream &os, const Task &task);
    friend std::istream &operator>>(std::istream &is, Task &task);
};


#endif //TASK_MANAGER_2_TASK_H
