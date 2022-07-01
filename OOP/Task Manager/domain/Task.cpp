//
// Created by Irina Scortar on 01.07.2022.
//

#include "Task.h"
#include "AppException.h"

std::ostream &operator<<(std::ostream &os, const Task &task) {
    os << task.description << "|" << task.status << "|" << task.programmer_id;
    return os;
}

std::istream &operator>>(std::istream &is, Task &task) {
    std::string line;
    std::getline(is, line);

    if (line.empty())
        return is;

    std::vector<std::string> parts = {""};

    for (auto it: line) {
        if (it == '|')
            parts.emplace_back("");
        else
            parts.back() += it;
    }

    if (parts.size() != 3)
        throw AppException("Invalid line for task");

    std::istringstream description_stream(parts[0]), status_stream(parts[1]), programmer_id_stream(parts[2]);
    description_stream >> task.description;
    status_stream >> task.status;
    programmer_id_stream >> task.programmer_id;

    return is;
}
