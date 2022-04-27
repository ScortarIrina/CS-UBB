#include "UI.h"

UI::UI(Service& service)
	:ui(service)
{
}

void UI::printMenuAdmin()
{
	std::cout << "\n\n\t~ ADMIN MENU ~\n\n";
	std::cout << "\t0. Exit\n";
	std::cout << "\t1. Display all tutorials\n";
	std::cout << "\t2. Add tutorial\n";
	std::cout << "\t3. Delete tutorial\n";
	std::cout << "\t4. Update tutorial\n";
	std::cout << "\n";
}

void UI::printMenuUser()
{
	std::cout << "\n\n\t~ USER MENU ~\n\n";
	std::cout << "\t0. Exit\n";
	std::cout << "\t1. Print the tutorials in the database having a given presenter\n";
	std::cout << "\t2. Print the tutorials from the watchlist\n";
	std::cout << "\t3. Watch the tutorials from the watchlist\n";
	std::cout << "\n";
}

void UI::printSubmenuUser()
{
	std::cout << "\n\n\t~ USER SUBMENU ~\n\n";
	std::cout << "\t0. Exit from watchlist preview\n";
	std::cout << "\t1. Add to watchlist and continue\n";
	std::cout << "\t2. Continue (without addng to the watchlist)\n";
	std::cout << "\n";
}

/// <summary>
/// Adds a tutorial to the database
/// </summary>
/// <returns>  
///			   1 = success
///			   0 = already in database
///			  -1 = error reading input
/// </returns>
int UI::addTutorialUI()
{
	std::string title_to_add;
	std::string presenter_to_add;
	std::string link_to_add;
	Duration duration_to_add;
	int nr_likes_to_add;
	char min_duration[3];
	char sec_duration[3];

	// read title
	std::cout << "\t- title: ";
	std::getline(std::cin, title_to_add);

	// read presenter
	std::cout << "\t- presenter: ";
	std::getline(std::cin, presenter_to_add);
	
	// read duration
	std::cout << "\t- minutes of duration (0-59): ";
	std::cin.getline(min_duration, 10);
	std::cout << "\t- seconds of duration (0-59): ";
	std::cin.getline(sec_duration, 10);
	
	// read number of likes
	std::cout << "\t- number of likes: ";
	std::cin >> nr_likes_to_add;
	std::cin.ignore();

	// read link
	std::cout << "\t- link: ";
	std::getline(std::cin, link_to_add);

	strcat(min_duration, "\0");
	strcat(sec_duration, "\0");

	if (!isdigit(min_duration[0]) || !isdigit(min_duration[1]) || !isdigit(sec_duration[0]) || !isdigit(sec_duration[1]))
		return -1;  // invalid duration

	duration_to_add.setMinutes(std::stoi(min_duration));
	duration_to_add.setSeconds(std::stoi(sec_duration));

	int res = ui.addTutorialService(title_to_add, presenter_to_add, duration_to_add, nr_likes_to_add, link_to_add);
	if (res == -1)
		return 0;  // tutorial already in database
	else if (res == 0)
		return 1;  // successful addition
}

int UI::deleteTutorialUI()
{
	std::string title_to_delete;
	std::string presenter_to_delete;
	std::string link_to_delete;
	Duration duration_to_delete;
	int nr_likes_to_delete;
	char min_duration[30];
	char sec_duration[30];

	// read title
	std::cout << "\t- title: ";
	std::getline(std::cin, title_to_delete);

	// read presenter
	std::cout << "\t- presenter: ";
	std::getline(std::cin, presenter_to_delete);

	// read duration
	std::cout << "\t- minutes of duration (0-59): ";
	std::cin.getline(min_duration, 10);
	std::cout << "\t- seconds of duration (0-59): ";
	std::cin.getline(sec_duration, 10);

	// read number of likes
	std::cout << "\t- number of likes: ";
	std::cin >> nr_likes_to_delete;
	std::cin.ignore();

	// read link
	std::cout << "\t- link: ";
	std::getline(std::cin, link_to_delete);

	strcat(min_duration, "\0");
	strcat(sec_duration, "\0");

	if (!isdigit(min_duration[0]) || !isdigit(min_duration[1]) || !isdigit(sec_duration[0]) || !isdigit(sec_duration[1]))
		return -1;  // invalid duration

	duration_to_delete.setMinutes(std::stoi(min_duration));
	duration_to_delete.setSeconds(std::stoi(sec_duration));

	int res = ui.deleteTutorialService(title_to_delete, presenter_to_delete, duration_to_delete, nr_likes_to_delete, link_to_delete);
	if (res == -1)
		return 0;  // tutorial not in database
	else if (res == 0)
		return 1;  // successful deletion
}

int UI::updateTutorialUI()
{
	std::string title_to_update;
	std::string presenter_to_update;
	std::string link_to_update;
	Duration duration_to_update;
	int nr_likes_to_update;
	char min_duration[30];
	char sec_duration[30];

	int updated_likes;
	std::string updated_link;

	// read title to update
	std::cout << "\t- title: ";
	std::getline(std::cin, title_to_update);

	// read presenter to update
	std::cout << "\t- presenter: ";
	std::getline(std::cin, presenter_to_update);

	// read duration to update
	std::cout << "\t- minutes of duration (0-59): ";
	std::cin.getline(min_duration, 10);
	std::cout << "\t- seconds of duration (0-59): ";
	std::cin.getline(sec_duration, 10);

	// read number of likes to update
	std::cout << "\t- number of likes: ";
	std::cin >> nr_likes_to_update;
	std::cin.ignore();

	// read link to update
	std::cout << "\t- link: ";
	std::getline(std::cin, link_to_update);

	strcat(min_duration, "\0");
	strcat(sec_duration, "\0");

	if (strlen(min_duration) > 3 || strlen(sec_duration) > 3 || !isdigit(min_duration[0]) || !isdigit(min_duration[1]) || !isdigit(sec_duration[0]) || !isdigit(sec_duration[1]))
		return -1;  // invalid duration

	duration_to_update.setMinutes(std::stoi(min_duration));
	duration_to_update.setSeconds(std::stoi(sec_duration));

	// read updated number of likes
	std::cout << "\t- updated number of likes: ";
	std::cin >> updated_likes;
	std::cin.ignore();

	// read updated link
	std::cout << "\t- updated link: ";
	std::getline(std::cin, updated_link);

	int res = ui.updateTutorialService(title_to_update, presenter_to_update, duration_to_update, nr_likes_to_update, link_to_update, updated_likes, updated_link);
	if (res == -1)
		return 0;  // tutorial not in database
	else/* if (res == 0)*/
		return 1;  // successful update
}

void UI::printTutorials()
{
	Tutorial* t = this->ui.getTutorialsService();
	int length = this->ui.getLengthService();
	for (int i = 0; i < length; i++)
		std::cout << "\n  " << i + 1 << ") " << t[i] << "\n\n";
}

void UI::addTutorialWatchlistUI(Tutorial t)
{
	int init_len = this->ui.getLengthWatchlistService();
	this->ui.addTutorialWatchlistService(t);
	int curr_len = this->ui.getLengthWatchlistService();

	if (init_len == curr_len)
		std::cout << "Couldn't add! The tutorial is already in the plsylist\n";
}

void UI::printTutorialsWatchlistUI()
{
	Tutorial* t = this->ui.getTutorialsWatchlistService();
	int length = this->ui.getLengthWatchlistService();
	if (length == 0)
		std::cout << "The watchlist is empty!\n";
	for (int i = 0; i < length; i++)
		std::cout << "\n  " << i + 1 << ") " << t[i] << "\n\n";
}

int UI::tutorialsWithGivenPresenterUI()
{
	std::string presenter_to_filter_by;

	// read presenter
	std::cout << "\t- presenter: ";
	std::getline(std::cin, presenter_to_filter_by);

	Tutorial* t = this->ui.getTutorialsService();
	const int length = ui.getLengthService();
	int ok = 0, loop = 1;
	std::vector<int> positions(length, -1);
	positions = ui.getByPresenter(presenter_to_filter_by, positions);
	for (const int& i : positions)
		if (i != -1)
			ok = 1;
	if (ok == 0)
		return 0;
	while (loop)
	{
		for (const int& i : positions)
			if (i != -1)
			{
				std::cout << "\n     " << t[i] << "\n";
				std::string user_option;
				this->printSubmenuUser();
				std::cout << "\tChoose an option (0-2): ";
				std::getline(std::cin, user_option);

				if (user_option == "1")  // Add to watchlist and continue
				{
					Tutorial current = this->ui.getTutorialOnPOsWatchlistService(i);
					this->addTutorialWatchlistUI(current);
					std::cout << "\t0. Exit\n";
					std::cout << "\t1. Next\n\n";
					std::string user_option;
					std::cout << "Choose an option (0-1): ";
					std::getline(std::cin, user_option);
					if (user_option == "1")
						continue;
					else if (user_option == "0")
					{
						loop = 0;
						return 1;
					}
				}
				else if (user_option == "2")  // Continue (without addng to the watchlist)
					continue;
				else if (user_option == "0")  // Exit from watchlist preview
				{
					loop = 0;
					return 1;
				}
			}
	}
}

void UI::watchTutorialsFromtWatchlist()
{
	Tutorial* tutorial_watchlist = this->ui.getTutorialsWatchlistService();
	int length = this->ui.getLengthWatchlistService();

	// there are no tutorials in the watchlist, so we exit the function
	if (length == 0)
	{
		std::cout << "No tutorials to watch, the watchlist is empty\n\n";
		return;
	}

	// parse through the watchlist in order to watch the tutorials and give likes where needed
	for (int i = 0; i < length; i++)
	{
		std::cout << "\n     " << tutorial_watchlist[i] << "\n";
		std::cout << "\nTutorial number " << i+1 << " is now playing...\n";
		std::cout << "\nCalling the pause command\n";
		system("pause");
		std::cout << "pause program terminated. Resuming...\n\n";
		tutorial_watchlist[i].play();

		// the user chooses to like or not the tutorial
		std::cout << "Do you want to give the tutorial a like?\n";
		std::cout << "\t0. Exit\n";
		std::cout << "\t1. Yes\n";
		std::cout << "\t2. No\n\n";
		std::string user_option;
		std::cout << "Choose an option (0-2): ";
		std::getline(std::cin, user_option);

		// number of likes is updated in the service and the tutoril is deleted from the watchlist
		if (user_option == "1")
		{
			Tutorial t = this->ui.getTutorialOnPOsService(this->ui.getPosOfExistingTutorialService(tutorial_watchlist[i]));
			this->ui.updateTutorialService(t.getTitle(), t.getPresenter(), t.getDuration(), t.getLikes(), t.getLink(), t.getLikes() + 1, t.getLink());
			this->ui.deleteTutorialFromWatchlistService(i);
		}
		else if (user_option == "2")
			continue;
		else if (user_option == "0")
			return;
		else
			std::cout << "\nInvalid menu option!\n";
	}
}

void UI::start()
{
	std::string mode;
	std::cout << "Welcome to... Master C++!\n\nChoose your status (admin/user): ";
	std::getline(std::cin, mode);
	if (mode == "admin")
	{
		int running = 1;
		std::string menu_option;
		while (running)
		{
			std::cout << "\n---------------------------------------------------------------------------------";
			this->printMenuAdmin();
			std::cout << "Choose an option (0-4): ";
			std::getline(std::cin, menu_option);
			if (menu_option == "0")
				break;
			else if (menu_option == "1")
				this->printTutorials();
			else if (menu_option == "2")
			{
				int res = this->addTutorialUI();
				if (res == -1)
					std::cout << "Invalid input!\n";
				else if (res == 1)
					std::cout << "Tutorial successfully added\n";
				else
					std::cout << "Tutorial already in database\n";
			}
			else if (menu_option == "3")
			{
				int res = this->deleteTutorialUI();
				if (res == -1)
					std::cout << "Invalid input!\n";
				else if (res == 1)
					std::cout << "Tutorial successfully deleted\n";
				else
					std::cout << "No such tutorial in database\n";
			}
			else if (menu_option == "4")
			{
				int res = this->updateTutorialUI();
				if (res == -1)
					std::cout << "Invalid input!\n";
				else if (res == 1)
					std::cout << "Tutorial successfully updated\n";
				else
					std::cout << "No such tutorial in database\n";
			}
			else
				std::cout << "Invalid menu option!\n";
		}
	}
	else if (mode == "user")
	{
		int running = 1;
		std::string menu_option;
		while (running)
		{
			std::cout << "\n---------------------------------------------------------------------------------";
			this->printMenuUser();
			std::cout << "Choose an option (0-4): ";
			std::getline(std::cin, menu_option);
			if (menu_option == "0")
				break;
			else if (menu_option == "1")
			{
				int res = this->tutorialsWithGivenPresenterUI();
				if (res == 0)
					std::cout << "There are no tutorials with this presenter!\n";
			}
			else if (menu_option == "2")
				this->printTutorialsWatchlistUI();
			else if (menu_option == "3")
				this->watchTutorialsFromtWatchlist();
			else
				std::cout << "Invalid menu option!\n";
		}
	}
}
