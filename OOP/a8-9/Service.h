#pragma once
#include "Repository.h"
#include "Watchlist.h"
#include "Tutorial.h"
#include <vector>

class Service
{
private:
    Repository& reposit;
    Watchlist& watchlist;

public:
    explicit Service(Repository& repo, Watchlist& w);

    // -1 = tutorial doesn't exist, ERROR
    // 0 = successful addition
    void addTutorialService(const std::string& title, const std::string& presenter, const Duration duration, int nr_likes, const std::string& link);

    // delete a tutorial from the database
    // -1 = tutorial doesn't exist, ERROR
    // 0 = successful deletion
    int deleteTutorialService(const std::string title, const std::string presenter, const Duration duration, const int nr_likes, const std::string link);

    // update the info of a tutorial
    // -1 = tutorial doesn't exist, ERROR
    // 0 = successful update
    int updateTutorialService(const std::string title_to_update, const std::string presenter_to_update, const Duration duration_to_update, int nr_likes_to_update, std::string link_to_update, int updated_likes);

    // add tutorial to the watchlist
    void addTutorialWatchlistService(Tutorial t);

    // delete a tutorial from the watchlist
    void deleteTutorialFromWatchlistService(int pos);

    // returns all tutorials from the watchlist
    std::vector<Tutorial> getTutorialsWatchlistService();

    // returns the tutorial on a given position in the watchlist
    Tutorial getTutorialOnPOsWatchlistService(int pos);

    // returns the position of a tutorial in the database
    // -1 if it wasn't found
    int getPosOfExistingTutorialService(const Tutorial t);

    // returns all tutorials
    //Tutorial* getTutorialsService();
    std::vector<Tutorial> getTutorialsService();

    // returns the tutorial on a given position in the database
    Tutorial getTutorialOnPOsService(int pos);

    // returns the number of tutorials added
    int getLengthService();

    // returns the number of tutorials from the watchlist
    int getLengthWatchlistService();

    std::vector<int> getByPresenter(const std::string& presenter_to_filter_by, std::vector<int> positions);
};