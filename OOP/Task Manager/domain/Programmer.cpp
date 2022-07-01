//
// Created by Irina Scortar on 01.07.2022.
//

#include "Programmer.h"
#include "AppException.h"
#include <sstream>
#include <iostream>

Programmer::Programmer(std::string name, int id) : name(name), id(id){
}

std::string Programmer::getName() {
    return this->name;
}

int Programmer::getId() {
    return this->id;
}

void Programmer::setName(std::string new_name) {
    this->name = new_name;
}

void Programmer::setId(int new_id) {
    this->id = new_id;
}

std::ostream &operator<<(std::ostream &os, const Programmer &programmer) {
    os << programmer.name << "|" << programmer.id;
    return os;
}

std::istream &operator>>(std::istream &is, Programmer &programmer) {
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

    if (parts.size() != 2)
        throw AppException("Invalid line for programmer");

    std::istringstream name_stream(parts[0]), id_stream(parts[1]);
    name_stream >> programmer.name;
    id_stream >> programmer.id;

    return is;
}
