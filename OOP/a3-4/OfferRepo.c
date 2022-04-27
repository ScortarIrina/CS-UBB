#include "OfferRepo.h"
#include "Offer.h"
#include <stdlib.h>
#include <string.h>

OfferRepo* createRepo()
{
    OfferRepo* repo = malloc(sizeof(OfferRepo));
    if (repo == NULL)
        return NULL;
    repo->length = 0;
    return repo;
}

void destroyRepo(OfferRepo* repo)
{
    if (repo == NULL)
        return;

    // If we decide that the repository takes hold of the memory allocated for the offers, 
    // then first destroy all the offers in the repository
    for (int i = 0; i < repo->length; i++)
        destroyOffer(repo->offers[i]);

    free(repo);
}

Offer* find(OfferRepo* r, char destination[], char departure_date[])
{   
    // TODO
    return NULL;
}

int add(OfferRepo* repo, Offer* new_offer)
{
    repo->length++;
    repo->offers[repo->length - 1] = new_offer;

    //repo->offers[repo->length - 1] = copyOffer(new_offer);

    return 1;
}

void removeOfferFromRepo(OfferRepo* repo, Offer* offer, int position)
{
    repo->offers[position] = repo->offers[repo->length - 1];
    repo->length--;
    destroyOffer(offer);
}

int getLength(OfferRepo* repo)
{
    return repo->length;
}

Offer* getOfferOnPos(OfferRepo* repo, int pos)
{
    if (repo == NULL)
        return NULL;
    if (pos < 0 || pos >= repo->length)
        return NULL;
    return repo->offers[pos];
}


//////////////   TESTS    /////////////////
//void initOfferRepoForTests(OfferRepo* r)
//{
//    Offer* o = createOffer()
//}
