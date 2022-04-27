#include "UI.h"
#include <stdio.h>
#include <stdlib.h>

UI* createUI(Controller* controller)
{
    UI* ui = malloc(sizeof(UI));
    if (ui == NULL)
        return NULL;
    ui->controller = controller;

    return ui;
}

void destroyUI(UI* ui)
{
    if (ui == NULL)
        return;

    // first destroy the controller
    destroyController(ui->controller);
    // free the ui memory
    free(ui);
}

/// <summary>
/// Prints the available menu for the problem
/// 
/// Input: -
/// 
/// Output : the menu is printed at the console
/// </summary>
void printMenu()
{
    printf("\n*******************************************************\n");
    printf("\n~~~ Menu options ~~~\n\n");
    printf("\t0. Exit\n");
    printf("\t1. List all offers\n");
    printf("\t2. Add an offer\n");
    printf("\t3. Delete an offer\n");
    printf("\t4. Update an offer\n\n");
}

int addOfferUI(UI* ui)
{
    char type[11], destination[21], departure_date[11];
    double price = 0;

    printf("\t- type (seaside, mountain or city break): ");
    int scanf_result = scanf("%10s", type);
    printf("\t- destination: ");
    scanf_result = scanf("%20s", destination);
    printf("\t- departure date (dd.mm.yyyy format): ");
    scanf_result = scanf("%10s", departure_date);
    printf("\t- price: ");
    scanf_result = scanf("%lf", &price);

    return addOffer(ui->controller, type, destination, departure_date, price);
}

int deleteOffer(UI* ui)
{
    if (ui == NULL)
        return 0;
    OfferRepo* repo = getRepo(ui->controller);

    if (repo == NULL)
        return 0;

    char* dest_to_delete;
    char* departure_to_delete;

    dest_to_delete = malloc(20);
    departure_to_delete = malloc(10);

    printf("\t- destination of offer: ");
    scanf("%s", dest_to_delete);

    printf("\t- departure date of offer: ");
    scanf("%s", departure_to_delete);

    return deleteOfferFromController(ui->controller, dest_to_delete, departure_to_delete);
}

void listAllOffers(UI* ui)
{
    if (ui == NULL)
        return;
    OfferRepo* repo = getRepo(ui->controller);
    if (repo == NULL)
        return;

    for (int i = 0; i < getLength(repo); i++)
    {
        Offer* offer = getOfferOnPos(repo, i);
        char offerString[200];
        toString(offer, offerString);
        printf("%s\n", offerString);
    }
}

/// <summary>
/// Reads an integer number from the keyboard. Asks for number while read errors encoutered.
/// Input: the message to be displayed when asking the user for input.
/// Returns the number.
/// </summary>
int readMenuOption(const char* message)
{
    char s[16] = { 0 };
    int res = 0;
    int flag = 0;
    int r = 0;

    while (flag == 0)
    {
        printf(message);
        int scanf_result = scanf("%15s", s);

        r = sscanf(s, "%d", &res);	// reads data from s and stores them as integer, if possible; returns 1 if successful
        flag = (r == 1);
        if (flag == 0)
            printf("Error reading number!\n");
    }
    return res;
}

/// <summary>
/// Verifies if the given command is valid (is either 1, 2 or 0)
/// 
/// Input: command - integer
/// 
/// Output: 1 - if the command is valid
///         0 - otherwise
/// 
/// </summary>
int validOption(int option)
{
    if (option >= 0 && option <= 3)
        return 1;
    return 0;
}

void startUI(UI* ui)
{
    while (1)
    {
        printMenu();
        int menu_option = readMenuOption("\nChoose an option (0-1): ");
        while (validOption(menu_option) == 0)
        {
            printf("Invalid menu option!");
            menu_option = readMenuOption("Choose an option (0-1): ");
        }
        if (menu_option == 0)
            break;
        switch (menu_option)
        {
        case 1:  // list all offers
        {
            listAllOffers(ui);
            break;
        }
        case 2:  // add an offer
        {
            int result = addOfferUI(ui);
            if (result == 1)
                printf("Offer successfully added.\n");
            else
                printf("Error! Offer couldn't be added, as there is another offer to the same destination on the same date.\n");
            break;
        }
        case 3:  // delete an offer
        {
            int result = deleteOffer(ui);
            if (result == 1)
                printf("Offer successfully deleted.\n");
            else
                printf("Error! No offer was found with the given information\n");
            break;
        }
        }
    }
}
