//
// Created by Irina Scortar on 01.07.2022.
//

#ifndef BACHELOR_THESES_2_TEACHER_H
#define BACHELOR_THESES_2_TEACHER_H

#include <string>
#include <utility>


class Teacher {
    std::string name;

public:
    Teacher() = default;

    ~Teacher() = default;

    explicit Teacher(std::string name) : name(std::move(name)) {}

    /// name getter
    std::string getName() const;

    /// setters
    void setName(std::string name);

    /// overloading operators
    friend std::ostream &operator<<(std::ostream &os, const Teacher &t);
    friend std::istream &operator>>(std::istream &is, Teacher &t);
};


#endif //BACHELOR_THESES_2_TEACHER_H
