//
// Created by Irina Scortar on 01.07.2022.
//

#include "Controller.h"

std::vector<Student> Controller::getAllStudentsByCoordinator(std::string teacher) {
    std::vector<Student> students_coordinated_by_teacher;
    std::vector<Student> all_students = this->students.getAll();

    for (auto student : all_students)
        if (student.getCoordinator() == teacher)
            students_coordinated_by_teacher.push_back(student);

    std::sort(students_coordinated_by_teacher.begin(), students_coordinated_by_teacher.end(),
              [](Student first, Student second)
              {
                   return first.getYear() > second.getYear();
              });
    return students_coordinated_by_teacher;
}

std::vector<Student> Controller::filterStudentByNameOrId(std::string filter) {
    std::vector<Student> filtered_students;
    std::vector<Student> all_students = this->students.getAll();

    for (auto& student : all_students) {
        std::string name = student.getName();
        std::string id = student.getId();
        auto iterator1 = std::search(
                name.begin(), name.end(),
                filter.begin(), filter.end(),
                [](char ch1, char ch2) {
                    return std::toupper(ch1) == std::toupper(ch2);
                });
        auto iterator2 = std::search(
                id.begin(), id.end(),
                filter.begin(), filter.end(),
                [](char ch1, char ch2) {
                    return std::toupper(ch1) == std::toupper(ch2);
                });
        if (iterator1 != name.end() || iterator2 != id.end())
            filtered_students.push_back(student);
    }
    return filtered_students;
}

void Controller::addTeacherAsCoordinator(std::string student_id, std::string teacher) {
    std::vector<Student> all_students = this->students.getAll();
    for (auto &student : all_students) {
        if (student.getId() == student_id) {
            if(student.getCoordinator() == "-") {
                student.setCoordinator(teacher);
                this->students.update(student);
                this->notify();
            }
            else
                throw AppException("You cannot be the coordinator of a student who already has one");
        }
    }
}

void Controller::updateEmail(std::string student_id, std::string email) {
    std::vector<Student> allStudents = this->students.getAll();
    for (auto student : allStudents) {
        if (student.getId() == student_id) {
            student.setEmail(email);
            this->students.update(student);
            this->notify();
        }
    }
}

void Controller::updateTitle(std::string student_id, std::string title) {
    std::vector<Student> allStudents = this->students.getAll();
    for (auto student : allStudents) {
        if (student.getId() == student_id) {
            student.setTitle(title);
            this->students.update(student);
            this->notify();
        }
    }
}

std::vector<Student> Controller::sortStudents() {
    std::vector<Student> all_students = this->students.getAll();

    std::sort(all_students.begin(), all_students.end(),
              [](Student first, Student second)
              {
                    if(first.getYear() != 2022 && second.getYear() != 2022)
                        return first.getYear() > second.getYear();
                    return first.getYear() < second.getYear();
              });

    return all_students;
}
