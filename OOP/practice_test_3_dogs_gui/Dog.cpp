//
// Created by irina on 22.05.2022.
//

#include "Dog.h"
#include <vector>
#include <sstream>


Dog::Dog()
    :breed(""), name(""), age(), photo_link("")
{
}

Dog::Dog(std::string breed, std::string name, int age, std::string photo)
    :breed(breed), name(name), age(age), photo_link(photo)
{
}

std::string Dog::getBreed() const
{
    return this->breed;
}

std::string Dog::getName() const
{
    return this->name;
}

int Dog::getAge() const
{
    return this->age;
}

std::string Dog::getPhoto() const
{
    return this->photo_link;
}

void Dog::setBreed(std::string new_breed)
{
    this->breed = new_breed;
}

void Dog::setName(std::string new_name)
{
    this->name = new_name;
}

void Dog::setAge(int new_age)
{
    this->age = new_age;
}

void Dog::setPhoto(std::string new_photo)
{
    this->photo_link = new_photo;
}

std::string Dog::toString() const
{
    auto str_age = std::to_string(this->age);
    return "Breed: " + this->breed + "  ||  Name: " + this->name + "  ||  Age: " +
           str_age + "  ||  Photograph link: " + this->photo_link;
}

std::vector<std::string> tokenize(const std::string& str, char delimiter)
{
    std::vector<std::string> result;
    std::stringstream ss(str);
    std::string token;
    while (getline(ss, token, delimiter))
        result.push_back(token);

    return result;
}

bool Dog::operator==(const Dog &dogToCheck) const
{
    return this->name == dogToCheck.name;
}

std::istream &operator>>(std::istream &inputStream, Dog &dog)
{
    std::string line;
    std::getline(inputStream, line);
    std::vector<std::string> tokens;
    if (line.empty())
        return inputStream;
    tokens = tokenize(line, ',');
    dog.breed = tokens[0];
    dog.name = tokens[1];
    dog.age = std::stoi(tokens[2]);
    dog.photo_link = tokens[3];
    return inputStream;
}

std::ostream &operator<<(std::ostream &outputStream, const Dog &dogOutput)
{
    outputStream << dogOutput.breed << "," << dogOutput.name << "," << std::to_string(dogOutput.age) << ","
                 << dogOutput.photo_link;
    return outputStream;
}

Dog::~Dog() = default;
