//
// Created by Irina on 5/5/2022.
//

#ifndef A8_9_SCORTARIRINA_CLION_USERREPOSITORY_H
#define A8_9_SCORTARIRINA_CLION_USERREPOSITORY_H

#include "Tutorial.h"
#include <vector>


class UserRepository
{
protected:
    std::vector<Tutorial> watchlist;
    std::string userFilename;

public:
    ///Constructor for the UserRepository class
    explicit UserRepository(std::vector<Tutorial>& Watchlist1);

    UserRepository();

    ///Method to get all the elements of the UserRepository
    virtual std::vector<Tutorial>& getAllUserRepo() = 0;

    ///Method to get the number of elements from the UserRepository
    virtual unsigned int getNrElems() = 0;

    ///Method to get the capacity of the dynamic array used in the UserRepository
    virtual unsigned int getCap() = 0;

    ///Method to add an element to the UserRepository
    virtual void addUserRepo(const Tutorial& t) = 0;

    virtual void writeToFile() = 0;

    virtual std::string& getFilename() = 0;

    ///Destructor
    ~UserRepository();
};

class UserException : public std::exception
{
private:
    std::string message;

public:
    explicit UserException(std::string& _message);

    const char* what() const noexcept override;
};


#endif //A8_9_SCORTARIRINA_CLION_USERREPOSITORY_H
