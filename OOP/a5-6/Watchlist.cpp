#include "Watchlist.h"


Watchlist::Watchlist()
	: index(0)
{
	//this->index = 0;
}

Watchlist::Watchlist(DynamicVector<Tutorial>& w)
	:watchlist(w)
{
	this->index = 0;
}

int Watchlist::getLengthWatchlist()
{
	return watchlist.getLength();
}

int Watchlist::addTutorial(const Tutorial& t)
{
	for (int i = 0; i < this->getLengthWatchlist(); i++)
		if (this->getTutorialOnPos(i) == t)
			return 0;
	watchlist.addElem(t);
	return 1;
}

void Watchlist::deleteTutorialOnPos(int pos)
{
	watchlist.deleteElem(pos);
}

Tutorial* Watchlist::getTutorials() const
{
	return watchlist.getAllElems();
}

Tutorial Watchlist::getTutorialOnPos(int pos) const
{
	Tutorial* elements = watchlist.getAllElems();
	int len = watchlist.getLength();
	for (int i = 0; i < len; i++)
		if (i == pos)
			return elements[i];
}

void Watchlist::play() const
{
	Tutorial* allTheTutorials = watchlist.getAllElems();
	allTheTutorials[index].play();
}

void Watchlist::next()
{
	index++;
	index %= watchlist.getLength();
}

