//
// Created by Irina on 5/5/2022.
//

#include "CSVRepository.h"
#include <fstream>


CSVRepository::CSVRepository(const std::vector<Tutorial>& watchlist, const std::string& userFilename)
{
    this->watchlist = watchlist;
    this->userFilename = userFilename;
}

std::vector<Tutorial>& CSVRepository::getAllUserRepo()
{
    return this->watchlist;
}

unsigned int CSVRepository::getNrElems()
{
    return this->watchlist.size();
}

unsigned int CSVRepository::getCap()
{
    return this->watchlist.capacity();
}

void CSVRepository::addUserRepo(const Tutorial& tutorial)
{
    this->watchlist.push_back(tutorial);
    this->writeToFile();
}

void CSVRepository::writeToFile()
{
    std::ofstream fout(this->userFilename);
    if (!this->watchlist.empty())
    {
        for (const Tutorial& t : this->watchlist)
        {
            fout << t << "\n";
        }
    }
    fout.close();
}

std::string& CSVRepository::getFilename()
{
    return this->userFilename;
}

CSVRepository::~CSVRepository() = default;
