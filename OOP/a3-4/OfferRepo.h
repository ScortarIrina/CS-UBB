#pragma once
#include "Offer.h"

typedef struct
{
	Offer* offers[100];
	int length;
}OfferRepo;

/// <summary>
/// Creates an OfferRepo
/// </summary>
OfferRepo* createRepo();

/// <summary>
/// Destroys a given offer repository. The memory is freed.
/// </summary>
void destroyRepo(OfferRepo* repo);

/// <summary>
/// Finds the offer with a given destination and departure date
/// </summary>
/// <param name="r">Pointer to the OfferRepo.</param>
/// <param name="destination">A string, the destination to search for.</param>
/// <param name="departure_date">A string, the departure date to search for.</param>
/// <returns>The position on which the offer with the given destination and departure date is in the OfferRepo</returns>
Offer* find(OfferRepo* r, char destination[], char departure_date[]);

/// <summary>
/// Adds an offer to the repo of offers
/// 
/// Input:  repo = pointer to the OfferRepo
///		    new_offer = the new offer
/// 
/// Output: 1 - if the offer was successfully added
///			0 - if the offer couldn't be added (it'a a duplicate)
/// </summary>
int add(OfferRepo* repo, Offer* new_offer);

int getLength(OfferRepo* repo);

/// <summary>
/// Returns the offer on the given position
/// 
/// Input:  repo - the offer repo
///		    pos - the position, an integer
/// 
/// Output: the offer on the given position, or an "empty" offer
/// </summary>
Offer* getOfferOnPos(OfferRepo* repo, int pos);

void removeOfferFromRepo(OfferRepo* repo, Offer* offer, int position);
