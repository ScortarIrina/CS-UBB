#include "Service.h"


Service::Service(Repository& repo, Watchlist& w)
	:service(repo), watchlist(w)
{
}

/// <returns>    
///				 0 = tutorial was successfully added
///				-1 = tutorial already in database
/// </returns>
int Service::addTutorialService(const std::string title, const std::string presenter, const Duration duration, const int nr_likes, const std::string link)
{
	Tutorial newTutorial(title, presenter, duration, nr_likes, link);
	return service.addTutorial(newTutorial);
}

void Service::addTutorialWatchlistService(Tutorial t)
{
	int res = watchlist.addTutorial(t);
}

/// <returns>    
///				 0 = tutorial was successfully deleted
///				-1 = tutorial not in database
/// </returns>
int Service::deleteTutorialService(const std::string title, const std::string presenter, const Duration duration, const int nr_likes, const std::string link)
{
	Tutorial t(title, presenter, duration, nr_likes, link);
	int pos = service.getPosOfExistingTutorial(t);
	if (pos == -1)
		return -1; // tutorial not in database
	else
		service.deleteTutorial(pos);
	return 0;
}

void Service::deleteTutorialFromWatchlistService(int pos)
{
	watchlist.deleteTutorialOnPos(pos);
}

int Service::updateTutorialService(const std::string title_to_update, const std::string presenter_to_update, const Duration duration_to_update, int nr_likes_to_update, std::string link_to_update, int updated_likes, std::string updated_link)
{
	Tutorial t(title_to_update, presenter_to_update, duration_to_update, nr_likes_to_update, link_to_update);
	int pos = service.getPosOfExistingTutorial(t);
	if (pos == -1)
		return -1; // tutorial not in database
	else
		service.updateTutorial(pos, updated_likes, updated_link);
	return 0;
}

int Service::getPosOfExistingTutorialService(const Tutorial t)
{
	return service.getPosOfExistingTutorial(t);
}

Tutorial* Service::getTutorialsService() const
{
	return service.getTutorials();
}

Tutorial* Service::getTutorialsWatchlistService() const
{
	return watchlist.getTutorials();
}

Tutorial Service::getTutorialOnPOsService(int pos)
{
	return service.getTutorialOnPOs(pos);
}

Tutorial Service::getTutorialOnPOsWatchlistService(int pos)
{
	return service.getTutorialOnPOs(pos);
}

int Service::getLengthService()
{
	return service.getLengthRepo();
}

std::vector<int> Service::getByPresenter(std::string presenter_to_filter_by, std::vector<int> positions)
{
	if (presenter_to_filter_by.size() == 0)
	{
		for (int i = 0; i < service.getLengthRepo(); i++)
			positions.push_back(i);
		return positions;
	}

	return service.getTutorialsByPresenter(presenter_to_filter_by, positions);
}

int Service::getLengthWatchlistService()
{
	return watchlist.getLengthWatchlist();
}
