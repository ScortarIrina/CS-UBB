//
// Created by Irina on 5/5/2022.
//

#ifndef A8_9_SCORTARIRINA_CLION_USERSERVICE_H
#define A8_9_SCORTARIRINA_CLION_USERSERVICE_H
#include "Repository.h"
#include "UserRepository.h"

class UserService
{
private:
    Repository& repository;
    UserRepository* userRepository;
public:

    ///Constructor for the UserService class
    ///\param repository1 - the admin repository
    ///\param userRepository1 - the user repository
    UserService(Repository& repository1, UserRepository* userRepository1);

    explicit UserService(Repository& repository1);

    ///Method to get all the elements from the user repository
    ///\return - the elements from the user repository
    std::vector<Tutorial> getAllUserService();

    ///Method to get the number of elements from the user repository
    ///\return - the number of elements
    unsigned int getNrElemsUserService();

    ///Method to get the capacity of the user repository
    ///\return - the capacity
    unsigned int getCapUserService();

    ///Method to add a new tutorial to the user repository
    ///\param tutorial - the tutorial to be added
    void addUserService(const Tutorial& tutorial);

    void repositoryType(const std::string& fileType);

    std::string& getFileService();

    ///Destructor
    ~UserService();
};


#endif //A8_9_SCORTARIRINA_CLION_USERSERVICE_H
