#pragma once
#include "DynamicVector.h"
#include "Tutorial.h"
#include <vector>

class Watchlist
{
private:
	DynamicVector<Tutorial> watchlist;
	int index;

public:
	Watchlist();

	// copy constructor for Watchlist
	Watchlist(DynamicVector<Tutorial>& w);

	// returns the number of elements from the watchlist
	int getLengthWatchlist();

	// adds a tutorial to the watchlist
	// 0 = error (tutorial already in watchlist)
	// 1 = success
	int addTutorial(const Tutorial& t);

	// deletes the tutorial from a certain position in the playlist
	void deleteTutorialOnPos(int pos);

	// returns all thetutorials from the playlist
	Tutorial* getTutorials() const;

	// returns the tutorial on a certain position
	Tutorial getTutorialOnPos(int pos) const;

	// plays a tutorial in the browser
	void play() const;

	// goes to the next tutorial in the playlist
	void next();
};
