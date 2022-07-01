//
// Created by Irina Scortar on 01.07.2022.
//

#ifndef BACHELOR_THESES_2_CONTROLLER_H
#define BACHELOR_THESES_2_CONTROLLER_H

#include "repository/StudentRepository.h"
#include "repository/TeacherRepository.h"
#include "domain/Subject.h"
#include <vector>


class Controller : public Subject {
    StudentRepository &students;
    TeacherRepository &teachers;

public:
    Controller(StudentRepository &students, TeacherRepository &teachers)
        : students(students), teachers(teachers) {}

    std::vector<Student> getAllStudents() { return this->students.getAll(); }

    std::vector<Teacher> getAllTeachers() { return this->teachers.getAll(); }

    std::vector<Student> getAllStudentsByCoordinator(std::string teacher);

    std::vector<Student> filterStudentByNameOrId(std::string filter);

    std::vector<Student> sortStudents();

    void addTeacherAsCoordinator(std::string student_id, std::string teacher);

    void updateEmail(std::string student_id, std::string email);

    void updateTitle(std::string student_id, std::string title);

    ~Controller() = default;
};


#endif //BACHELOR_THESES_2_CONTROLLER_H
