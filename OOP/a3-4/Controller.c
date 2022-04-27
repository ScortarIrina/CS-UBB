#include "Controller.h"
#include <stdlib.h>
#include <string.h>

Controller* createController(OfferRepo* r)
{
	Controller* c = malloc(sizeof(Controller));
	if (c == NULL)
		return NULL;
	c->repo = r;

	return c;
}

void destroyController(Controller* controller)
{
	if (controller == NULL)
		return;

	// first destroy the repo inside
	destroyRepo(controller->repo);
	// then free the memory
	free(controller);
}

int addOffer(Controller* controller, char* type, char* destination, char* departure_date, double price)
{
	Offer* offer = createOffer(type, destination, departure_date, price);

	int result = add(controller->repo, offer);

	// if the offer was not added, destroy it (as it won't be destroyed by the repo)
	if (result == 0)
		destroyOffer(offer);

	return result;
}

OfferRepo* getRepo(Controller* controller)
{
	return controller->repo;
}

int findPositionOfOffer(Controller* controller, char* destination, char* departure_date)
{
	OfferRepo* repo = getRepo(controller);
	for (int i = 0; i < repo->length; i++)
	{
		if (strcmp(repo->offers[i]->destination, destination) && strcmp(repo->offers[i]->departure_date, departure_date))
			return i;
	}
	return -1;
}

int deleteOfferFromController(Controller* controller, char* destination, char* departure_date)
{
	int position = findPositionOfOffer(controller, destination, departure_date);

	if (position != -1)
	{
		removeOfferFromRepo(controller->repo, controller->repo->offers[position], position);
		return 1;
	}
	return 0;
}

