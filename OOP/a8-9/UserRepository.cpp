//
// Created by Irina on 5/5/2022.
//

#include "UserRepository.h"

UserRepository::UserRepository() = default;

UserRepository::~UserRepository() = default;

UserRepository::UserRepository(std::vector<Tutorial>& Watchlist1)
{
    this->watchlist = Watchlist1;
}

UserException::UserException(std::string& _message)
        : message(_message)
{
}

const char* UserException::what() const noexcept
{
    return message.c_str();
}

