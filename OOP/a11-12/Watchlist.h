#pragma once
#include "Tutorial.h"
#include <vector>
#include <algorithm>


class Watchlist
{
private:
    std::vector<Tutorial> watchlist;
    std::string userFilename;
    int index;

public:
    // constructor for a Watchlist
    Watchlist();

    // returns the number of elements from the watchlist
    int getLengthWatchlist();

    // adds a tutorial to the watchlist
    // 0 = error (tutorial already in watchlist)
    // 1 = success
    int addTutorialWatchlist(const Tutorial& t);

    // deletes the tutorial from a certain position in the playlist
    void deleteTutorialOnPos(int pos);

    // returns all the tutorials from the watchlist
    std::vector<Tutorial>& getTutorialsWatchlist();

    // returns the tutorial on a certain position
    Tutorial getTutorialOnPos(int pos) const;

    // returns the position on which the existing tutorial is
    // returns -1 if the tutorial doesn't exist in the watchlist
    int getPosOfExistingTutorial(const Tutorial&);

    // plays a tutorial in the browser
    void play();

    // goes to the next tutorial in the playlist
    void next();
};


class WatchlistException : public std::exception
{
private:
    std::string message;

public:
    explicit WatchlistException(std::string& _message);

    const char* what() const noexcept override;
};