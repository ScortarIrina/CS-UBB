//
// Created by Irina Scortar on 01.07.2022.
//

#include "Student.h"
#include "AppException.h"
#include <ostream>
#include <vector>
#include <sstream>


std::string Student::getId() {
    return this->id;
}

std::string Student::getName() {
    return this->name;
}

std::string Student::getEmail() {
    return this->email;
}

int Student::getYear() {
    return this->year;
}

std::string Student::getTitle() {
    return this->title;
}

std::string Student::getCoordinator() {
    return this->coordinator;
}

void Student::setId(std::string id) {
    this->id = id;
}

void Student::setName(std::string name) {
    this->name = name;
}

void Student::setEmail(std::string email) {
    this->email = email;
}

void Student::setYear(int year) {
    this->year = year;
}

void Student::setTitle(std::string title) {
    this->title = title;
}

void Student::setCoordinator(std::string coordinator) {
    this->coordinator = coordinator;
}

std::ostream &operator<<(std::ostream &os, const Student &s) {
    os << s.id << "|" << s.name << "|" << s.email << "|" << s.year << "|" << s.title << "|" << s.coordinator;
    return os;
}

std::istream &operator>>(std::istream &is, Student &s) {
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

    if (parts.size() != 6)
        throw AppException("Invalid line for student");

    std::istringstream id_stream(parts[0]), name_stream(parts[1]), email_stream(parts[2]),
            year_stream(parts[3]), title_stream(parts[4]), coordinator_stream(parts[5]);
    id_stream >> s.id;
    name_stream >> s.name;
    email_stream >> s.email;
    year_stream >> s.year;
    title_stream >> s.title;
    coordinator_stream >> s.coordinator;

    return is;
}
