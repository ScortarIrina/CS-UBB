#pragma once
/*
Each Offer has a
	- type (one of seaside, mountain or city break)
	- destination
	- departure date
	- price
*/

typedef struct
{
	char* type;
	char* destination;
	char* departure_date;
	double price;
}Offer;

Offer* createOffer(char* type, char* destination, char* departure_date, double price);

void destroyOffer(Offer* offer);  // The memory is freed

char* getType(Offer* offer);

char* getDestination(Offer* offer);

char* getDeparture(Offer* offer);

double getPrice(Offer* offer);

void toString(Offer* offer, char str[]);

//Offer* copyOffer(Offer* offer);
