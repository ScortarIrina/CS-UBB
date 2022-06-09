//
// Created by irina on 23.05.2022.
//

#include "Repository.h"
#include <algorithm>
#include <fstream>


Repository::Repository(std::vector<Dog> &repo_vector, std::string &dog_filename)
{
    this->listOfDogs = repo_vector;
    this->filename = dog_filename;
}

void Repository::loadDogsFromFile()
{
    if (!this->filename.empty())
    {
        Dog dog_from_file;
        std::ifstream fin(this->filename);
        while (fin >> dog_from_file)
        {
            if (std::find(this->listOfDogs.begin(), this->listOfDogs.end(), dog_from_file) ==
                this->listOfDogs.end())
                this->listOfDogs.push_back(dog_from_file);
        }
        fin.close();
    }
}

void Repository::writeDogsToFile()
{
    if (!this->filename.empty())
    {
        std::ofstream fout(this->filename);
        for (const Dog &dog: this->listOfDogs)
        {
            fout << dog << "\n";
        }
        fout.close();
    }
}

void Repository::initialiseRepo()
{
    this->loadDogsFromFile();
}

std::vector<Dog> &Repository::getAllDogs()
{
    return this->listOfDogs;
}

unsigned int Repository::getNrDogs()
{
    if (this->listOfDogs.empty())
    {
        std::string error;
        error += std::string("The database is empty!");
        if(!error.empty())
            throw RepositoryException(error);
    }
    return this->listOfDogs.size();
}

void Repository::addDog(const Dog &dog)
{
    int existing = this->findByName(dog.getName());
    if (existing != -1)
    {
        std::string error;
        error += std::string("The dog already exists!");
        if(!error.empty())
            throw RepositoryException(error);
    }
    this->listOfDogs.push_back(dog);
    this->writeDogsToFile();
}

void Repository::deleteDog(int delete_index)
{
    if (delete_index == -1)
    {
        std::string error;
        error += std::string("The dog does not exist!");
        if(!error.empty())
            throw RepositoryException(error);
    }
    this->listOfDogs.erase(this->listOfDogs.begin() + delete_index);
    this->writeDogsToFile();
}

void Repository::updateDog(int update_index, const Dog &new_dog)
{
    if (update_index == -1)
    {
        std::string error;
        error += std::string("The dog does not exist!");
        if(!error.empty())
            throw RepositoryException(error);
    }
    this->listOfDogs[update_index] = new_dog;
    this->writeDogsToFile();
}

int Repository::findByName(const std::string &name)
{
    int searched_index = -1;
    std::vector<Dog>::iterator it;
    it = std::find_if(this->listOfDogs.begin(), this->listOfDogs.end(), [&name](Dog& dog) {return dog.getName() == name;});
    if (it != this->listOfDogs.end())
    {
        searched_index = it - this->listOfDogs.begin();
    }
    return searched_index;
}

RepositoryException::RepositoryException(std::string &_message)
        : message(_message)
{
}

const char *RepositoryException::what() const noexcept
{
    return message.c_str();
}

Repository::~Repository() = default;
