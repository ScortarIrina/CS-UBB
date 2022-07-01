//
// Created by Irina Scortar on 01.07.2022.
//

#ifndef BACHELOR_THESES_2_APPEXCEPTION_H
#define BACHELOR_THESES_2_APPEXCEPTION_H

#include <stdexcept>


class AppException : public std::runtime_error {
public:
    explicit AppException(const std::string &arg)
            : std::runtime_error(arg) {}
};


#endif //BACHELOR_THESES_2_APPEXCEPTION_H
