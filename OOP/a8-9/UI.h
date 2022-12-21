#pragma once
#include "Service.h"
#include "UserService.h"
#include <string>
#include "Validator.h"
#include <cstdlib>
#include <iostream>
#include <vector>


class UI
{
private:
    Service& ui;
    UserService& userService;
    TutorialValidator& validator;

public:
    // copy constructor
    UI(Service& service, UserService& userService, TutorialValidator& v);

    // -1 = tutorial doesn't exist, ERROR
    // 0 = successful addition
    void addTutorialUI();

    // -1 = tutorial doesn't exist, ERROR
    // 0 = successful deletion
    void deleteTutorialUI();

    // -1 = tutorial doesn't exist, ERROR
    // 0 = successful update
    void updateTutorialUI();

    static void printMenu();

    // prints the menu for the admin
    static void printMenuAdmin();

    // prints the menu for the user
    static void printMenuUser();

    static void printSubmenuUser();

    // prints all tutorials
    void printTutorials();

    // -1 = tutorial doesn't exist, ERROR
    // 0 = successful addition
    void addTutorialWatchlistUI(Tutorial t);

    // prints all tutorials from the watchlist
    void printTutorialsWatchlistUI();

    // prints the tutorials which have a given presenter
    int tutorialsWithGivenPresenterUI();

    // watch the tutorials from the watchlist one by one
    void watchTutorialsFromWatchlist();

    void openFile();

    void adminMode();

    void userMode();

    // starts the application
    void start();
};