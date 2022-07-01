//
// Created by Irina Scortar on 01.07.2022.
//

#include "Teacher.h"
#include "AppException.h"
#include <sstream>
#include <vector>
#include <utility>
#include <ostream>


std::string Teacher::getName() const {
    return this->name;
}

void Teacher::setName(std::string name) {
    this->name = name;
}

std::ostream &operator<<(std::ostream &os, const Teacher &t) {
    os << t.name;
    return os;
}

std::istream &operator>>(std::istream &is, Teacher &t) {
    std::string line;
    std::getline(is, line);

    if(line.empty())
        return is;

    std::vector<std::string> parts = {""};

    for(auto it:line)
    {
        if(it == '|')
            parts.emplace_back("");
        else
            parts.back() += it;
    }

    if(parts.size() != 1)
        throw AppException("Invalid line for teacher");

    std::istringstream name_stream(parts[0]);

    name_stream >> t.name;

    return is;
}
