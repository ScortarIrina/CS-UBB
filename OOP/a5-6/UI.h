#pragma once
#include "Service.h"
#include <string>
#include <stdlib.h>

class UI
{
private:
	Service ui;

public:
	// copy constructor
	UI(Service& service);

	// -1 = tutorial doesn't exist, ERROR
	// 0 = successful addition
	int addTutorialUI();

	// -1 = tutorial doesn't exist, ERROR
	// 0 = successful deletion
	int deleteTutorialUI();

	// -1 = tutorial doesn't exist, ERROR
	// 0 = successful update
	int updateTutorialUI();

	// prints the menu for the admin
	void printMenuAdmin();

	// prints the menu for the user
	void printMenuUser();

	void printSubmenuUser();

	// prints all tutorials
	void printTutorials();

	// -1 = tutorial does't exist, ERROR
	// 0 = successful addition
	void addTutorialWatchlistUI(Tutorial t);

	// prints all tutorials from the watchlist
	void printTutorialsWatchlistUI();

	// prints the tutorials which have a given presenter
	int tutorialsWithGivenPresenterUI();

	// watch the tutorials from the watchlist one by one
	void watchTutorialsFromtWatchlist();

	// starts the application
	void start();
};
