//
// Created by irina on 22.05.2022.
//

#ifndef TEST3_PRACTICE_GUI_DOG_H
#define TEST3_PRACTICE_GUI_DOG_H

#include <string>


class Dog
{
private:
    std::string breed;
    std::string name;
    int age;
    std::string photo_link;

public:
    Dog();

    /// Constructor for Dog class
    explicit Dog(std::string, std::string name, int age, std::string photo);

    /// Getters
    std::string getBreed() const;
    std::string getName() const;
    int getAge() const;
    std::string getPhoto() const;

    /// Setters
    void setBreed(std::string new_breed);
    void setName(std::string new_name);
    void setAge(int new_age);
    void setPhoto(std::string new_photo);

    /// Method to format an entity into a string
    std::string toString() const;

    bool operator==(const Dog &dogToCheck) const;

    friend std::istream &operator>>(std::istream &inputStream, Dog &dog);

    friend std::ostream &operator<<(std::ostream &outputStream, const Dog &dogOutput);

    /// Destructor for Dog class
    ~Dog();
};

#endif //TEST3_PRACTICE_GUI_DOG_H
