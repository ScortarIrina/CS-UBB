//
// Created by Irina Scortar on 01.07.2022.
//

#ifndef TASK_MANAGER_2_APPEXCEPTION_H
#define TASK_MANAGER_2_APPEXCEPTION_H

#include <stdexcept>

class AppException : public std::runtime_error {
public:
    explicit AppException(const std::string &arg)
            : std::runtime_error(arg) {}
};

#endif //TASK_MANAGER_2_APPEXCEPTION_H
