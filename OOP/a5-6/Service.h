#pragma once
#include "Repository.h"
#include "Watchlist.h"
#include <vector>

class Service
{
private:
	Repository service;
	Watchlist watchlist;

public:
	Service(Repository& repo, Watchlist& w);

	// -1 = tutorial does't exist, ERROR
	// 0 = successful addition
	int addTutorialService(const std::string title, const std::string presenter, const Duration duration, const int nr_likes, const std::string link);

	void addTutorialWatchlistService(Tutorial t);

	// -1 = tutorial does't exist, ERROR
	// 0 = successful deletion
	int deleteTutorialService(const std::string title, const std::string presenter, const Duration duration, const int nr_likes, const std::string link);

	void deleteTutorialFromWatchlistService(int pos);

	// -1 = tutorial does't exist, ERROR
	// 0 = successful update
	int updateTutorialService(const std::string title_to_update, const std::string presenter_to_update, const Duration duration_to_update, int nr_likes_to_update, std::string link_to_update, int updated_likes, std::string updated_link);

	int getPosOfExistingTutorialService(const Tutorial t);

	// returns all tutorials
	Tutorial* getTutorialsService() const;

	// returns all tutorials from the watchlist
	Tutorial* getTutorialsWatchlistService() const;

	Tutorial getTutorialOnPOsService(int pos);

	Tutorial getTutorialOnPOsWatchlistService(int pos);

	// returns the number of tutorials added
	int getLengthService();

	//int tutorialsHaveSamePresenter()

	std::vector<int> getByPresenter(std::string presenter_to_filter_by,  std::vector<int> positions);

	// returns the number of tutorials from the watchlist
	int getLengthWatchlistService();
};
