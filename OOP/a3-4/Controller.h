#pragma once
#include "OfferRepo.h"

typedef struct
{
	OfferRepo* repo;
}Controller;

Controller* createController(OfferRepo* r);

void destroyController(Controller* controller);

int deleteOfferFromController(Controller* controller, char* destination, char* departure_date);

int addOffer(Controller* controller, char* type, char* destination, char* departure_date, double price);

//int destroyOffer(Controller* controller, char* destination, char* departure_date);

OfferRepo* getRepo(Controller* controller);
