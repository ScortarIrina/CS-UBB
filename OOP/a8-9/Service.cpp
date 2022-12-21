#include "Service.h"


Service::Service(Repository& repo, Watchlist& w)
        : reposit(repo), watchlist(w)
{
}

void Service::addTutorialService(const std::string& title, const std::string& presenter, const Duration duration, const int nr_likes, const std::string& link)
{
    Tutorial newTutorial = Tutorial(title, presenter, duration, nr_likes, link);
    this->reposit.addTutorialRepo(newTutorial);
}

int Service::deleteTutorialService(const std::string title, const std::string presenter, const Duration duration, const int nr_likes, const std::string link)
{
    Tutorial t(title, presenter, duration, nr_likes, link);
    int pos = reposit.getPosOfExistingTutorial(t);
    reposit.deleteTutorial(pos);
    return 1;
}

int Service::updateTutorialService(const std::string title_to_update, const std::string presenter_to_update, const Duration duration_to_update, int nr_likes_to_update, std::string link_to_update, int updated_likes)
{
    Tutorial t(title_to_update, presenter_to_update, duration_to_update, nr_likes_to_update, link_to_update);
    int pos = reposit.getPosOfExistingTutorial(t);
    if (pos == -1)
        return -1; // tutorial not in database
    else
        reposit.updateTutorial(pos, updated_likes);
    return 0;
}

void Service::addTutorialWatchlistService(Tutorial t)
{
    int res = watchlist.addTutorialWatchlist(t);
}

void Service::deleteTutorialFromWatchlistService(int pos)
{
    watchlist.deleteTutorialOnPos(pos);
}

std::vector<Tutorial> Service::getTutorialsWatchlistService()
{
    return this->watchlist.getTutorialsWatchlist();
}

Tutorial Service::getTutorialOnPOsWatchlistService(int pos)
{
    return watchlist.getTutorialOnPos(pos);
}

int Service::getPosOfExistingTutorialService(const Tutorial t)
{
    return reposit.getPosOfExistingTutorial(t);
}

std::vector<Tutorial> Service::getTutorialsService()
{
    return this->reposit.getTutorialsRepo();
}

Tutorial Service::getTutorialOnPOsService(int pos)
{
    return reposit.getTutorialOnPos(pos);
}

int Service::getLengthService()
{
    return reposit.getLengthRepo();
}

int Service::getLengthWatchlistService()
{
    return watchlist.getLengthWatchlist();
}

std::vector<int> Service::getByPresenter(const std::string& presenter_to_filter_by, std::vector<int> positions)
{
    if (presenter_to_filter_by.empty())
    {
        for (int i = 0; i < reposit.getLengthRepo(); i++)
            positions.push_back(i);
        return positions;
    }

    return reposit.getTutorialsByPresenter(presenter_to_filter_by, positions);
}