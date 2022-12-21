#include "UI.h"
#include <string>


UI::UI(Service& service, UserService& userService, TutorialValidator& v)
        :ui(service), userService(userService), validator(v)
{
}

void UI::printMenu()
{
    std::cout << "\n\t~ MENU ~\n\n";
    std::cout << "\t0. Exit\n";
    std::cout << "\t1. Administrator mode\n";
    std::cout << "\t2. User mode\n";
    std::cout << "\n";
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
    std::cout << "\t4. See the watchlist file\n";
    std::cout << "\n";
}

void UI::printSubmenuUser()
{
    std::cout << "\n\n\t~ USER SUBMENU ~\n\n";
    std::cout << "\t0. Exit from watchlist preview\n";
    std::cout << "\t1. Add to watchlist and continue\n";
    std::cout << "\t2. Continue (without adding to the watchlist)\n";
    std::cout << "\n";
}

void UI::addTutorialUI()
{
    std::string title_to_add;
    std::string presenter_to_add;
    std::string link_to_add;
    std::string duration_to_add;
    std::string likes_string;
    int nr_likes_to_add;

    // title validation
    while (true)
    {
        try
        {
            std::cout << "   - title: ";
            std::getline(std::cin, title_to_add);
            this->validator.validateTitle(title_to_add);
            break;
        }
        catch (ValidationException& ex)
        {
            std::cout << ex.what() << std::endl;
        }
    }
    // presenter validation
    while (true)
    {
        try
        {
            std::cout << "   - presenter: ";
            std::getline(std::cin, presenter_to_add);
            this->validator.validatePresenter(presenter_to_add);
            break;
        }
        catch (ValidationException& ex)
        {
            std::cout << ex.what() << std::endl;
        }
    }
    // duration validation
    while (true)
    {
        try
        {
            std::cout << "   - duration (mm:ss): ";
            std::getline(std::cin, duration_to_add);
            this->validator.validateDurationString(duration_to_add);
            break;
        }
        catch (ValidationException& ex)
        {
            std::cout << ex.what() << std::endl;
        }
    }
    // likes validation
    while (true)
    {
        try
        {
            std::cout << "   - likes: ";
            std::getline(std::cin, likes_string);
            this->validator.validateNrLikesString(likes_string);
            nr_likes_to_add = stoi(likes_string);
            this->validator.validateNrLikes(nr_likes_to_add);
            break;
        }
        catch (ValidationException& ex)
        {
            std::cout << ex.what() << std::endl;
        }
    }
    // link validation
    while (true)
    {
        try
        {
            std::cout << "   - link: ";
            std::getline(std::cin, link_to_add);
            this->validator.validateVideoLink(link_to_add);
            break;
        }
        catch (ValidationException& ex)
        {
            std::cout << ex.what() << std::endl;
        }
    }

    Duration duration;
    int minutes = (int(duration_to_add[0]) - '0') * 10 + (int(duration_to_add[1]) - '0');
    int seconds = (int(duration_to_add[3]) - '0') * 10 + (int(duration_to_add[4]) - '0');
    duration.setMinutes(minutes);
    duration.setSeconds(seconds);

    ui.addTutorialService(title_to_add, presenter_to_add, duration, nr_likes_to_add, link_to_add);
    std::cout << "Tutorial added successfully!" << std::endl;
}

void UI::deleteTutorialUI()
{
    std::string title_to_delete;
    std::string presenter_to_delete;
    std::string link_to_delete;
    std::string duration_to_delete;
    std::string likes_string;
    int nr_likes_to_delete;

    // title validation
    while (true)
    {
        try
        {
            std::cout << "   - title: ";
            std::getline(std::cin, title_to_delete);
            this->validator.validateTitle(title_to_delete);
            break;
        }
        catch (ValidationException& ex)
        {
            std::cout << ex.what() << std::endl;
        }
    }

    // presenter validation
    while (true)
    {
        try
        {
            std::cout << "   - presenter: ";
            std::getline(std::cin, presenter_to_delete);
            this->validator.validatePresenter(presenter_to_delete);
            break;
        }
        catch (ValidationException& ex)
        {
            std::cout << ex.what() << std::endl;
        }
    }

    // duration validation
    while (true)
    {
        try
        {
            std::cout << "   - duration (mm:ss): ";
            std::getline(std::cin, duration_to_delete);
            this->validator.validateDurationString(duration_to_delete);
            break;
        }
        catch (ValidationException& ex)
        {
            std::cout << ex.what() << std::endl;
        }
    }

    // likes validation
    while (true)
    {
        try
        {
            std::cout << "   - likes: ";
            std::getline(std::cin, likes_string);
            this->validator.validateNrLikesString(likes_string);
            nr_likes_to_delete = stoi(likes_string);
            this->validator.validateNrLikes(nr_likes_to_delete);
            break;
        }
        catch (ValidationException& ex)
        {
            std::cout << ex.what() << std::endl;
        }
    }

    // link validation
    while (true)
    {
        try
        {
            std::cout << "   - link of the video to delete: ";
            std::getline(std::cin, link_to_delete);
            this->validator.validateVideoLink(link_to_delete);
            break;
        }
        catch (ValidationException& ex)
        {
            std::cout << ex.what() << std::endl;
        }
    }

    Duration duration;
    int minutes = (int(duration_to_delete[0]) - '0') * 10 + (int(duration_to_delete[1]) - '0');
    int seconds = (int(duration_to_delete[3]) - '0') * 10 + (int(duration_to_delete[4]) - '0');
    duration.setMinutes(minutes);
    duration.setSeconds(seconds);

    int res = ui.deleteTutorialService(title_to_delete, presenter_to_delete, duration, nr_likes_to_delete, link_to_delete);
    std::cout << "Tutorial deleted successfully!" << std::endl;
}

void UI::updateTutorialUI()
{
    std::string title_to_update;
    std::string presenter_to_update;
    std::string link_to_update;
    std::string duration_to_update;
    std::string likes_string;
    int nr_likes_to_update;
    int updated_likes;
    // title validation
    while (true)
    {
        try
        {
            std::cout << "   - title: ";
            std::getline(std::cin, title_to_update);
            this->validator.validateTitle(title_to_update);
            break;
        }
        catch (ValidationException& ex)
        {
            std::cout << ex.what() << std::endl;
        }
    }
    // presenter validation
    while (true)
    {
        try
        {
            std::cout << "   - presenter: ";
            std::getline(std::cin, presenter_to_update);
            this->validator.validatePresenter(presenter_to_update);
            break;
        }
        catch (ValidationException& ex)
        {
            std::cout << ex.what() << std::endl;
        }
    }
    // duration validation
    while (true)
    {
        try
        {
            std::cout << "   - duration (mm:ss): ";
            std::getline(std::cin, duration_to_update);
            this->validator.validateDurationString(duration_to_update);
            break;
        }
        catch (ValidationException& ex)
        {
            std::cout << ex.what() << std::endl;
        }
    }
    // likes validation
    while (true)
    {
        try
        {
            std::cout << "   - likes: ";
            std::getline(std::cin, likes_string);
            this->validator.validateNrLikesString(likes_string);
            nr_likes_to_update = stoi(likes_string);
            this->validator.validateNrLikes(nr_likes_to_update);
            break;
        }
        catch (ValidationException& ex)
        {
            std::cout << ex.what() << std::endl;
        }
    }
    // link validation
    while (true)
    {
        try
        {
            std::cout << "   - link: ";
            std::getline(std::cin, link_to_update);
            this->validator.validateVideoLink(link_to_update);
            break;
        }
        catch (ValidationException& ex)
        {
            std::cout << ex.what() << std::endl;
        }
    }
    // UPDATED likes validation
    while (true)
    {
        try
        {
            std::cout << "\n   - updated likes: ";
            std::getline(std::cin, likes_string);
            this->validator.validateNrLikesString(likes_string);
            updated_likes = stoi(likes_string);
            this->validator.validateNrLikes(updated_likes);
            break;
        }
        catch (ValidationException& ex)
        {
            std::cout << ex.what() << std::endl;
        }
    }

    Duration duration;
    int minutes = (int(duration_to_update[0]) - '0') * 10 + (int(duration_to_update[1]) - '0');
    int seconds = (int(duration_to_update[3]) - '0') * 10 + (int(duration_to_update[4]) - '0');
    duration.setMinutes(minutes);
    duration.setSeconds(seconds);

    int res = ui.updateTutorialService(title_to_update, presenter_to_update, duration, nr_likes_to_update, link_to_update, updated_likes);
    std::cout << "Tutorial updated successfully!" << std::endl;
}

void UI::printTutorials()
{
    std::vector<Tutorial> tutorials = this->ui.getTutorialsService();
    int index = 0;
    for (const Tutorial& tutorial : tutorials)
    {
        std::cout << index + 1 << ". " << tutorial.toString() << "\n";
        index++;
    }
}

void UI::addTutorialWatchlistUI(Tutorial t)
{
    int init_len = this->ui.getLengthWatchlistService();
    this->ui.addTutorialWatchlistService(t);
    this->userService.addUserService(t);
    int curr_len = this->ui.getLengthWatchlistService();
    if (init_len == curr_len)
        std::cout << "Tutorial could not be added!\n";
}

void UI::printTutorialsWatchlistUI()
{
    std::vector<Tutorial> w;
    w = this->ui.getTutorialsWatchlistService();
    int index = 0;
    for (const Tutorial& tutorial : w)
    {
        std::cout << index + 1 << ". " << tutorial.toString() << "\n";
        index++;
    }
}

int UI::tutorialsWithGivenPresenterUI()
{
    std::string presenter_to_filter_by;

    // read presenter
    std::cout << "   - presenter: ";
    std::getline(std::cin, presenter_to_filter_by);

    std::vector<Tutorial> t = this->ui.getTutorialsService();
    const int length = ui.getLengthService();
    int ok = 0, loop = 1;
    std::vector<int> positions(length, -1);
    positions = ui.getByPresenter(presenter_to_filter_by, positions);
    for (const int& i : positions)
        if (i != -1)
            ok = 1;
    if (ok == 0)
        return 0;
    while (true)
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
                    Tutorial current = this->ui.getTutorialOnPOsService(i);
                    this->addTutorialWatchlistUI(current);
                    std::cout << "\n\t0. Exit\n";
                    std::cout << "\t1. Next\n\n";
                    std::string user_option1;
                    std::cout << "Choose an option (0-1): ";
                    std::getline(std::cin, user_option1);
                    if (user_option1 == "1")
                        continue;
                    else if (user_option1 == "0")
                    {
                        loop = 0;
                        return 1;
                    }
                }
                else if (user_option == "2")  // Continue (without adding to the watchlist)
                    continue;
                else if (user_option == "0")  // Exit from watchlist preview
                {
                    loop = 0;
                    return 1;
                }
            }
    }
}

void UI::watchTutorialsFromWatchlist()
{
    std::vector<Tutorial> tutorial_watchlist = this->ui.getTutorialsWatchlistService();
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
        std::cout << "\nTutorial number " << i + 1 << " is now playing...\n";
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
            this->ui.updateTutorialService(t.getTitle(), t.getPresenter(), t.getDuration(), t.getLikes(), t.getLink(), t.getLikes() + 1);
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

void UI::openFile()
{
    std::string filepath = this->userService.getFileService();
    std::string link;
    if (filepath == "/home/irina/Desktop/CLion_projects/a8-9-ScortarIrina/Project1/Tutorials.html")
    {
        link = std::string("gopen ").append(filepath);
    }
    else if(filepath == "/home/irina/Desktop/CLion_projects/a8-9-ScortarIrina/Project1/Tutorials.csv")
    {
        link = std::string("gopen ").append(filepath);
    }
    system(link.c_str());
}

void UI::adminMode()
{
    std::cout << "\n~You entered the administrator mode~" << std::endl;
    bool done = false;
    while (true)
    {
        try
        {
            std::cout << "\n---------------------------------------------------------------------------------";
            this->printMenuAdmin();
            std::string menu_option;
            std::cout << "Choose an option (0-4): ";
            std::getline(std::cin, menu_option);
            if (menu_option == "0")
            {
                std::cout << "Exiting admin mode..." << std::endl;
                break;
            }
            else if (menu_option == "1")
                this->printTutorials();
            else if (menu_option == "2")
                this->addTutorialUI();
            else if (menu_option == "3")
                this->deleteTutorialUI();
            else if (menu_option == "4")
                this->updateTutorialUI();
            else
                std::cout << "Invalid menu option!\n";
        }
        catch (ValidationException& ex)
        {
            std::cout << ex.what() << std::endl;
        }
        catch (RepoException& ex)
        {
            std::cout << ex.what() << std::endl;
        }
    }
}

void UI::userMode()
{
    std::cout << "\n~You entered the user mode~" << std::endl;
    std::string menu_option;
    bool done = false;
    while (!done)
    {
        try
        {
            std::cout << "\n---------------------------------------------------------------------------------";
            this->printMenuUser();
            std::cout << "Choose an option (0-4): ";
            std::getline(std::cin, menu_option);

            if (menu_option == "0")
            {
                done = true;
                std::cout << "Exiting user mode..." << std::endl;
            }
            else if (menu_option == "1")
            {
                int res = this->tutorialsWithGivenPresenterUI();
                if (res == 0)
                    std::cout << "There are no tutorials with this presenter!\n";
            }
            else if (menu_option == "2")
                this->printTutorialsWatchlistUI();
            else if (menu_option == "3")
                this->watchTutorialsFromWatchlist();
            else if (menu_option == "4")
                this->openFile();
            else
                std::cout << "Invalid menu option!\n";
        }
        catch (ValidationException& ex)
        {
            std::cout << ex.what() << std::endl;
        }
        catch (UserException& ex)
        {
            std::cout << ex.what() << std::endl;
        }
        catch (RepoException& ex)
        {
            std::cout << ex.what() << std::endl;
        }
    }
}

void UI::start()
{
    std::cout << "Welcome to Master C++!\n";
    int user_mode = 0;
    bool done = false;

    while (!done)
    {
        printMenu();
        std::cout << "Choose an option (0-2): ";
        std::string option;
        getline(std::cin, option);
        if (option == "1")
            adminMode();
        else if (option == "2")
        {
            if (user_mode == 0)
            {
                std::cout << "\nFile type to save the watchlist(csv or html): ";
                std::string fileType;
                while (true)
                {
                    try
                    {
                        getline(std::cin, fileType);
                        this->userService.repositoryType(fileType);
                        break;
                    }
                    catch (UserException& ex)
                    {
                        std::cout << ex.what() << std::endl;
                    }
                }
                user_mode = 1;
            }
            userMode();
        }
        else if (option == "0")
        {
            done = true;
            std::cout << "Goodbye!" << std::endl;
        }
        else
            std::cout << "Bad input!" << std::endl;
    }
}
