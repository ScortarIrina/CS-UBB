//
// Created by Irina Scortar on 01.07.2022.
//

#include "TeacherRepository.h"

TeacherRepository::TeacherRepository(const std::string &filepath) : filepath(filepath) {
    std::ifstream f(filepath);
    if(!f){
        throw AppException("File " + filepath + " doesn't exist");
    }

    this->teachers = {};
    Teacher t;

    while(f >> t){
        this->teachers.push_back(t);
    }
    f.close();
}

void TeacherRepository::add(const Teacher &t) {
    this->teachers.push_back(t);
}

std::vector<Teacher> TeacherRepository::getAll() {
    return this->teachers;
}

TeacherRepository::~TeacherRepository() {
    std::ofstream g(this->filepath);
    for(const auto& entity : teachers){
        g << entity << "\n";
    }
    g.close();
}
