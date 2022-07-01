//
// Created by Irina Scortar on 01.07.2022.
//

#ifndef BACHELOR_THESES_2_TEACHERREPOSITORY_H
#define BACHELOR_THESES_2_TEACHERREPOSITORY_H

#include <vector>
#include <string>
#include "domain/Student.h"
#include "domain/AppException.h"
#include "domain/Teacher.h"
#include <iostream>
#include <fstream>
#include <cstdlib>
#include <algorithm>


class TeacherRepository {
    std::vector<Teacher> teachers;
    std::string filepath;

public:
    explicit TeacherRepository(const std::string &filepath);

    void add(const Teacher &s);

    std::vector<Teacher> getAll();

    virtual ~TeacherRepository();
};


#endif //BACHELOR_THESES_2_TEACHERREPOSITORY_H
