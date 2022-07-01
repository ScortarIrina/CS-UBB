//
// Created by Irina Scortar on 01.07.2022.
//

#include "StudentRepository.h"

StudentRepository::StudentRepository(const std::string &filepath) : filepath(filepath) {
    std::ifstream f(filepath);
    if(!f){
        throw AppException("File " + filepath + " doesn't exist");
    }

    this->students = {};
    Student s;

    while(f >> s){
        this->students.push_back(s);
    }
    f.close();
}

void StudentRepository::add(const Student &s) {
    this->students.push_back(s);
}

void StudentRepository::remove(std::string id) {
    int pos = -1;
    for(int i = 0; i < this->students.size(); i++) {
        if (this->students[i].getId() == id) {
            pos = i;
            break;
        }
    }
    if (pos == -1) {
        throw AppException("There is no student with this id!");
    }
    else {
        this->students.erase(this->students.begin() + pos);
    }
}

void StudentRepository::update(Student &s) {
    for(auto& student : this->students){
        if(student.getId() == s.getId()) {
            student = s;
            return;
        }
    }
}

std::vector<Student> StudentRepository::getAll() {
    return this->students;
}

StudentRepository::~StudentRepository() {
    std::ofstream g(this->filepath);
    for(const auto& entity : students){
        g << entity << "\n";
    }
    g.close();
}
