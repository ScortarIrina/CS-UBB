//
// Created by irina on 23.05.2022.
//

#ifndef TEST3_PRACTICE_GUI_SERVICE_H
#define TEST3_PRACTICE_GUI_SERVICE_H

#include "Repository.h"


class Service
{
private:
    Repository& repo;

public:
    explicit Service(Repository &repo1);

    std::vector<Dog> getAllDogsService();

    unsigned int getNrDogsService();

    void addDogService(const std::string& breed, const std::string& name, int age, const std::string& photograph);

    void deleteDogService(const std::string& name);

    void updateService(const std::string& old_name, const std::string& new_breed, const std::string& new_name, int new_age,const std::string& new_photo);

    void getFiltered(std::vector<Dog> &valid_dogs, const std::string &filter_string, int age_filter);

    int findByNameService(const std::string& name);

    std::vector<std::string> getAllBreeds();

    ~Service();
};


#endif //TEST3_PRACTICE_GUI_SERVICE_H
