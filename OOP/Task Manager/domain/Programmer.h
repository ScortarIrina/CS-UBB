//
// Created by Irina Scortar on 01.07.2022.
//

#ifndef TASK_MANAGER_2_PROGRAMMER_H
#define TASK_MANAGER_2_PROGRAMMER_H

#include <string>
#include <vector>


class Programmer {
private:
    std::string name;
    int id;

public:
    Programmer() = default;

    Programmer(std::string name, int id);

    /// getters
    std::string getName();
    int getId();

    /// setters
    void setName(std::string new_name);
    void setId(int new_id);

    /// overloading operators
    friend std::ostream &operator<<(std::ostream &os, const Programmer &programmer);
    friend std::istream &operator>>(std::istream &is, Programmer &programmer);

    ~Programmer() = default;
};


#endif //TASK_MANAGER_2_PROGRAMMER_H
