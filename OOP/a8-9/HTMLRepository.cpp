//
// Created by Irina on 5/5/2022.
//

#include "HTMLRepository.h"
#include <fstream>


HTMLRepository::HTMLRepository(const std::vector<Tutorial>& watchlist, const std::string& userFilename)
{
    this->watchlist = watchlist;
    this->userFilename = userFilename;
}

std::vector<Tutorial>& HTMLRepository::getAllUserRepo()
{
    return this->watchlist;
}

unsigned int HTMLRepository::getNrElems()
{
    return this->watchlist.size();
}

unsigned int HTMLRepository::getCap()
{
    return this->watchlist.capacity();
}

void HTMLRepository::addUserRepo(const Tutorial& tutorial)
{
    this->watchlist.push_back(tutorial);
    this->writeToFile();
}

void HTMLRepository::writeToFile()
{
    std::ofstream fout(this->userFilename);
    fout << "<!DOCTYPE html>\n<html><head><title>watchlist</title></head><body>\n";
    fout << "<table border=\"1\">\n";
    fout << "<tr><td>Title</td><td>Presenter</td><td>Duration</td><td>Likes</td><td>Link</td></tr>\n";
    for (const Tutorial& tutorial : this->watchlist) {
        fout << "<tr><td>" << tutorial.getTitle() << "</td>"
             << "<td>" << tutorial.getPresenter() << "</td>"
             << "<td>" << tutorial.getDuration() << "</td>"
             << "<td>" << tutorial.getLikes() << "</td>"
             << "<td><a href=\"" << tutorial.getLink() << "\">" << tutorial.getLink() << "</a></td>" << '\n';
    }
    fout << "</table></body></html>";
    fout.close();
}

std::string& HTMLRepository::getFilename()
{
    return this->userFilename;
}

HTMLRepository::~HTMLRepository() = default;
