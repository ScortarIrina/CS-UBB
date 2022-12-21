#pragma once
#include <vector>
#include <algorithm>
#include "Tutorial.h"
#include <QWidget>
#include "Repository.h"


class Repository
{
private:
    std::vector<Tutorial> adminRepoVector;
    std::string tutorialsFilename;

public:
    void loadTutorialsFromFile();

    void writeTutorialsToFile();

    void initialiseRepo();

    // constructor for a Repository
    explicit Repository(std::vector<Tutorial>& repo_vector, std::string& tutorial_filename);

    // returns all the tutorials from the database of the admin
    //Tutorial* getTutorialsRepo();
    std::vector<Tutorial>& getTutorialsRepo();

    // adds a tutorial to the database if possible
    // 1 = the tutorial is not in the database, so we add it
    // 0 = the tutorial is already in the database
    void addTutorialRepo(const Tutorial&);

    // returns the position on which the existing tutorial is
    // returns -1 if the tutorial doesn't exist in the database
    int getPosOfExistingTutorial(const Tutorial&);

    // returns the tutorial on a given position from the database
    Tutorial getTutorialOnPos(int pos);

    int getByTitle(std::string title);

    // deletes a tutorial from the database
    void deleteTutorial(int pos);

    // returns the positions on which tutorials with a given presenter are in the database
    std::vector<int> getTutorialsByPresenter(const std::string presenter_to_filter_by, std::vector<int> positions);

    // updates the info of a tutorial (only number of likes and link)
    void updateTutorial(int pos, int updated_likes);

    // returns the number of elements from the database
    int getLengthRepo();
};

class RepoException : public std::exception
{
private:
    std::string message;

public:
    explicit RepoException(std::string& _message);

    const char* what() const noexcept override;
};
