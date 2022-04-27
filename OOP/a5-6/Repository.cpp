#include "Repository.h"

Repository::Repository()
{
}

Repository::Repository(DynamicVector<Tutorial>& v)
	:repo(v)
{
}

Tutorial* Repository::getTutorials() const
{
	return repo.getAllElems();
}

int Repository::addTutorial(const Tutorial& t)
{
	int pos = getPosOfExistingTutorial(t);
	if (pos == -1)
	{
		repo + t;
		return 0;
	}

	return -1;
}

int Repository::getPosOfExistingTutorial(const Tutorial& t)
{
	Tutorial* elements = repo.getAllElems();
	int len = repo.getLength();
	for (int i = 0; i < len; i++)
		if (elements[i] == t)
			return i;
	return -1;
}

Tutorial Repository::getTutorialOnPOs(int pos)
{
	Tutorial* elements = repo.getAllElems();
	int len = repo.getLength();
	for (int i = 0; i < len; i++)
		if (i == pos)
			return elements[i];
}

void Repository::deleteTutorial(int pos)
{
	repo.deleteElem(pos);
}

std::vector<int> Repository::getTutorialsByPresenter(const std::string presenter_to_filter_by, std::vector<int> positions)
{
	Tutorial* t = this->getTutorials();
	for (int i = 0; i < this->getLengthRepo(); i++)
		if (t[i].getPresenter() == presenter_to_filter_by)
			positions.push_back(i);

	return positions;
}

void Repository::updateTutorial(int pos, int updated_likes, std::string updated_link)
{
	repo.getAllElems()[pos].setLikes(updated_likes);
	repo.getAllElems()[pos].setLink(updated_link);
}

int Repository::getLengthRepo()
{
	return repo.getLength();
}
