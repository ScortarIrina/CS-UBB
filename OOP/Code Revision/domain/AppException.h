//
// Created by Irina Scortar on 01.07.2022.
//

#ifndef CODE_REVISION_APPEXCEPTION_H
#define CODE_REVISION_APPEXCEPTION_H

#include <stdexcept>

class AppException : public std::runtime_error {
public:
    explicit AppException(const std::string &arg)
            : std::runtime_error(arg) {}
};

#endif //CODE_REVISION_APPEXCEPTION_H
