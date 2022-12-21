//
// Created by Irina on 5/5/2022.
//

#include "UserService.h"
#include <algorithm>
#include "CSVRepository.h"
#include "HTMLRepository.h"

UserService::UserService(Repository& repository1, UserRepository* userRepository1)
        :repository(repository1)
{
    this->userRepository = userRepository1;
}

UserService::UserService(Repository& repository1)
        : repository(repository1)
{
}

std::vector<Tutorial> UserService::getAllUserService()
{
    if (this->userRepository->getAllUserRepo().empty())
    {
        std::string error;
        error += std::string("The watchlist is empty!");
        if (!error.empty())
            throw UserException(error);
    }
    return this->userRepository->getAllUserRepo();
}

unsigned int UserService::getNrElemsUserService()
{
    if (this->userRepository->getNrElems() == 0)
    {
        std::string error;
        error += std::string("The watchlist is empty!");
        if (!error.empty())
            throw UserException(error);
    }
    return this->userRepository->getNrElems();;
}

unsigned int UserService::getCapUserService()
{
    return this->userRepository->getCap();
}

void UserService::addUserService(const Tutorial& tutorial)
{
    this->userRepository->addUserRepo(tutorial);

    std::string title = tutorial.getTitle();
    std::string presenter = tutorial.getPresenter();
    Duration duration = tutorial.getDuration();
    int likes = tutorial.getLikes();
    std::string link = tutorial.getLink();
    Tutorial t = Tutorial(title, presenter, duration, likes, link);

    int delete_index = this->repository.getPosOfExistingTutorial(t);
}

void UserService::repositoryType(const std::string& fileType)
{
    if (fileType == "csv") {
        std::vector<Tutorial> userVector;
        std::string userFile = R"(/home/irina/Desktop/CLion_projects/a8-9-ScortarIrina/Project1/Tutorials.csv)";
        auto* repo = new CSVRepository{ userVector, userFile };
        this->userRepository = repo;
    }
    else if (fileType == "html") {
        std::vector<Tutorial> userVector;
        std::string userFile = R"(/home/irina/Desktop/CLion_projects/a8-9-ScortarIrina/Project1/Tutorials.html)";
        auto* repo = new HTMLRepository{ userVector, userFile };
        this->userRepository = repo;
    }
    else {
        std::string error;
        error += std::string("The filename is invalid!");
        if (!error.empty())
            throw UserException(error);
    }
}

std::string& UserService::getFileService()
{
    return this->userRepository->getFilename();
}

UserService::~UserService() = default;
