#include "Watchlist.h"

Watchlist::Watchlist()
        :index(0)
{
}

int Watchlist::getLengthWatchlist()
{
    return watchlist.size();
}

int Watchlist::addTutorialWatchlist(const Tutorial& t)
{
    // the tutorial is not in the watchlist
    if (this->getPosOfExistingTutorial(t) == -1)
    {
        watchlist.push_back(t);
        return 1;
    }
    // the tutorial is already in the database
    return 0;
}

void Watchlist::deleteTutorialOnPos(int pos)
{
    remove(watchlist.begin(), watchlist.end(), getTutorialOnPos(pos));
}

std::vector<Tutorial>& Watchlist::getTutorialsWatchlist()
{
    if (this->watchlist.empty())
    {
        std::string error;
        error += std::string("The database is empty!");
        if (!error.empty())
            throw WatchlistException(error);
    }
    return this->watchlist;
}

Tutorial Watchlist::getTutorialOnPos(int pos) const
{
    auto it = watchlist.at(pos);
    return it;
}

int Watchlist::getPosOfExistingTutorial(const Tutorial& t)
{
    auto it = std::find(watchlist.begin(), watchlist.end(), t);
    if (it != watchlist.end())
        return (it - watchlist.begin());
    else
        return -1;
}

void Watchlist::play()
{
    Tutorial* allTheTutorials = watchlist.data();
    allTheTutorials[index].play();
}

void Watchlist::next()
{
    index++;
    index %= watchlist.size();
}

WatchlistException::WatchlistException(std::string& _message)
        : message(_message)
{
}

const char* WatchlistException::what() const noexcept
{
    return message.c_str();
}
