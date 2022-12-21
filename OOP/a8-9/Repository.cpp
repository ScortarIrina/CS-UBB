#include "Repository.h"
#include <algorithm>
#include <fstream>


void Repository::loadTutorialsFromFile()
{
    if (!this->tutorialsFilename.empty())
    {
        Tutorial tutorial_from_file;
        std::ifstream fin(this->tutorialsFilename);
        while (fin >> tutorial_from_file)
        {
            if (std::find(this->adminRepoVector.begin(), this->adminRepoVector.end(), tutorial_from_file) ==
                this->adminRepoVector.end())
                this->adminRepoVector.push_back(tutorial_from_file);
        }
        fin.close();
    }
}

void Repository::writeTutorialsToFile()
{
    if (!this->tutorialsFilename.empty()) {
        std::ofstream fout(this->tutorialsFilename);
        for (const Tutorial& tutorial : this->adminRepoVector) {
            fout << tutorial << "\n";
        }
        fout.close();
    }
}

void clearFile()
{
    std::ofstream ofs;
    ofs.open("Tutorials.csv", std::ofstream::out | std::ofstream::trunc);
    ofs.close();
}

void Repository::initialiseRepo()
{
    this->loadTutorialsFromFile();
}

Repository::Repository(std::vector<Tutorial>& repo_vector, std::string& tutorial_filename)
{
    this->adminRepoVector = repo_vector;
    this->tutorialsFilename = tutorial_filename;
}

Repository::Repository(std::vector<Tutorial>& v)
        :adminRepoVector(v)
{
}

std::vector<Tutorial>& Repository::getTutorialsRepo()
{
    if (this->adminRepoVector.empty()) {
        std::string error;
        error += std::string("The database is empty!");
        if (!error.empty())
            throw RepoException(error);
    }
    return this->adminRepoVector;
}

void Repository::addTutorialRepo(const Tutorial& t)
{
    // the tutorial is not in the database
    if (this->getPosOfExistingTutorial(t) == -1)
    {
        adminRepoVector.push_back(t);
        this->writeTutorialsToFile();
    }
        // the tutorial is already in the database
    else
    {
        std::string error;
        error += std::string("The tutorial already exists!");
        if (!error.empty())
            throw RepoException(error);
    }
}

int Repository::getPosOfExistingTutorial(const Tutorial& t)
{
    //std::vector<Tutorial>::iterator it;
    auto it = std::find(adminRepoVector.begin(), adminRepoVector.end(), t);
    if (it != adminRepoVector.end())
        return (it - adminRepoVector.begin());
    else
        return -1;
}

Tutorial Repository::getTutorialOnPos(int pos)
{
    //std::vector<Tutorial>::iterator it;
    auto it = adminRepoVector.begin() + pos;
    return *it;
}

void Repository::deleteTutorial(int pos)
{
    if (pos == -1)
    {
        std::string error;
        error += std::string("The tutorial does not exist!");
        if (!error.empty())
            throw RepoException(error);
    }
    this->adminRepoVector.erase(this->adminRepoVector.begin() + pos);
    clearFile();
    this->writeTutorialsToFile();

    //remove(adminRepoVector.begin(), adminRepoVector.end(), getTutorialOnPos(pos));
    //adminRepoVector.pop_back();
}

std::vector<int> Repository::getTutorialsByPresenter(const std::string presenter_to_filter_by, std::vector<int> positions)
{
    Tutorial* t = adminRepoVector.data();
    for (int i = 0; i < adminRepoVector.size(); i++)
        if (t[i].getPresenter() == presenter_to_filter_by)
            positions.push_back(i);

    return positions;
}


void Repository::updateTutorial(int pos, int updated_likes)
{
    adminRepoVector.data()[pos].setLikes(updated_likes);
}

int Repository::getLengthRepo()
{
    return adminRepoVector.size();
}

RepoException::RepoException(std::string& _message)
        : message(_message)
{
}

const char* RepoException::what() const noexcept
{
    return message.c_str();
}