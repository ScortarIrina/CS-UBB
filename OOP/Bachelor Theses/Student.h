//
// Created by Irina Scortar on 01.07.2022.
//

#ifndef BACHELOR_THESES_2_STUDENT_H
#define BACHELOR_THESES_2_STUDENT_H

#include <string>


class Student {
    std::string id;
    std::string name;
    std::string email;
    int year;           // the year he/she has to finalize his/her bachelor thesis
    std::string title;
    std::string coordinator;

public:
    Student() = default;

    ~Student() = default;

    Student(std::string id, std::string name, std::string email, int year, std::string title, std::string coordinator)
            : id(id), name(name), email(email), year(year), title(title), coordinator(coordinator) {}

    /// getters
    std::string getId();
    std::string getName();
    std::string getEmail();
    int getYear();
    std::string getTitle();
    std::string getCoordinator();

    /// setters
    void setId(std::string id);
    void setName(std::string name);
    void setEmail(std::string email);
    void setYear(int year);
    void setTitle(std::string title);
    void setCoordinator(std::string coordinator);

    /// overloading operators
    friend std::ostream &operator<<(std::ostream &os, const Student &s);
    friend std::istream &operator>>(std::istream &is, Student &s);
};


#endif //BACHELOR_THESES_2_STUDENT_H
