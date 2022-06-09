//
// Created by irina on 23.05.2022.
//

#ifndef TEST3_PRACTICE_GUI_REPOSITORY_H
#define TEST3_PRACTICE_GUI_REPOSITORY_H

#include "Dog.h"
#include <vector>


class Repository
{
private:
    std::vector<Dog> listOfDogs;
    std::string filename;

public:
    explicit Repository(std::vector<Dog>& repo_vector, std::string& dog_filename);

    void loadDogsFromFile();

    void writeDogsToFile();

    void initialiseRepo();

    std::vector<Dog>& getAllDogs();

    unsigned int getNrDogs();

    void addDog(const Dog& dog);

    void deleteDog(int delete_index);

    void updateDog(int update_index, const Dog& new_dog);

    int findByName(const std::string& name);

    ~Repository();
};


class RepositoryException: public std::exception
{
private:
    std::string message;
public:
    explicit RepositoryException(std::string& _message);

    const char *what() const noexcept override;
};


#endif //TEST3_PRACTICE_GUI_REPOSITORY_H
