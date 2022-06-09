//
// Created by irina on 23.05.2022.
//

#include <algorithm>
#include "Service.h"

Service::Service(Repository &repo1)
    : repo(repo1)
{
}

std::vector<Dog> Service::getAllDogsService()
{
    return this->repo.getAllDogs();
}

unsigned int Service::getNrDogsService()
{
    return this->repo.getNrDogs();
}

void Service::addDogService(const std::string &breed, const std::string &name, int age, const std::string &photograph)
{
    Dog dog = Dog(breed, name, age, photograph);
    this->repo.addDog(dog);
}

void Service::deleteDogService(const std::string &name)
{
    int delete_index = this->repo.findByName(name);
    this->repo.deleteDog(delete_index);
}

void Service::updateService(const std::string &old_name, const std::string &new_breed, const std::string &new_name,
                            int new_age, const std::string &new_photo)
{
    int update_index = this->repo.findByName(old_name);
    Dog new_dog = Dog(new_breed, new_name, new_age, new_photo);
    this->repo.updateDog(update_index, new_dog);
}

void Service::getFiltered(std::vector<Dog> &valid_dogs, const std::string &filter_string, int age_filter)
{
    std::vector<Dog> data;
    data = this->repo.getAllDogs();
    if (filter_string[0] == '\0')
    {
        std::copy_if(data.begin(), data.end(), std::back_inserter(valid_dogs),[&age_filter](Dog& dog) { return dog.getAge() < age_filter; });
    }
    else
    {
        std::copy_if(data.begin(), data.end(), std::back_inserter(valid_dogs),[&age_filter, &filter_string](Dog& dog) { return dog.getAge() < age_filter && dog.getBreed() == filter_string; });
    }
}

int Service::findByNameService(const std::string &name)
{
    return this->repo.findByName(name);
}

std::vector<std::string> Service::getAllBreeds()
{
    std::vector<std::string> breeds;
    std::vector<Dog> data;
    data = this->repo.getAllDogs();
    for (const Dog& dog: data)
    {
        if (std::find(breeds.begin(), breeds.end(), dog.getBreed()) == breeds.end())
            breeds.push_back(dog.getBreed());
    }
    return breeds;
}

Service::~Service() = default;
