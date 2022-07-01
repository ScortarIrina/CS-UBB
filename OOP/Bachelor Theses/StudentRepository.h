//
// Created by Irina Scortar on 01.07.2022.
//

#ifndef BACHELOR_THESES_2_STUDENTREPOSITORY_H
#define BACHELOR_THESES_2_STUDENTREPOSITORY_H

#include <vector>
#include <string>
#include "domain/Student.h"
#include "domain/AppException.h"
#include "domain/Teacher.h"
#include <iostream>
#include <fstream>
#include <cstdlib>
#include <algorithm>


class StudentRepository {
    std::vector<Student> students;
    std::string filepath;

public:
    explicit StudentRepository(const std::string &filepath);

    void add(const Student &s);

    void remove(std::string id);

    void update(Student &s);

    std::vector<Student> getAll();

    virtual ~StudentRepository();
};


#endif //BACHELOR_THESES_2_STUDENTREPOSITORY_H
