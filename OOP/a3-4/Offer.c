#include "Offer.h"
#include <string.h>
#include <stdlib.h>
#include <stdio.h>

Offer* createOffer(char* type, char* destination, char* departure_date, double price)
{
    Offer* offer = malloc(sizeof(Offer));
    if (offer == NULL)
        return NULL;

    offer->type = malloc(sizeof(char) * (strlen(type) + 1));
    if (offer->type != NULL)
        strcpy(offer->type, type);

    offer->destination = malloc(sizeof(char) * (strlen(destination) + 1));
    if (offer->destination != NULL)
        strcpy(offer->destination, destination);

    offer->departure_date = malloc(sizeof(char) * (strlen(departure_date) + 1));
    if (offer->departure_date != NULL)
        strcpy(offer->departure_date, departure_date);

    offer->price = price;

    return offer;
}

void destroyOffer(Offer* offer)
{
    if (offer == NULL)
        return;

    // free the memory which was allocated for the component fields
    free(offer->type);
    free(offer->destination);
    free(offer->departure_date);

    // free the memory which was allocated for the offer structure
    free(offer);
}

char* getType(Offer* offer)
{
    if (offer == NULL)
        return NULL;

    return offer->type;
}

char* getDestination(Offer* offer)
{
    if (offer == NULL)
        return NULL;

    return offer->destination;
}

char* getDeparture(Offer* offer)
{
    if (offer == NULL)
        return NULL;

    return offer->departure_date;
}

double getPrice(Offer* offer)
{
    if (offer == NULL)
        return -1;

    return offer->price;
}

//Offer* copyOffer(Offer* offer)
//{
//    if (offer == NULL)
//    {
//        return NULL;
//    }
//    Offer* copy_offer = createOffer(offer->type, offer->destination, offer->departure_date, offer->price);
//    return copy_offer;
//}

void toString(Offer* offer, char str[])
{
    if (offer == NULL)
        return;
    sprintf(str, "type: %10s    destination: %10s    departure date: %10s    price: %f", offer->type, offer->destination, offer->departure_date, offer->price);
}
