#pragma once
#include "DynamicVector.h"
#include "Tutorial.h"
#include <vector>

class Repository
{
private:
	DynamicVector<Tutorial> repo;

public:
	Repository();

	// copy constructor for a Repository
	Repository(DynamicVector<Tutorial>& v);

	// returns all the tutorials from the database of the admin
	Tutorial* getTutorials() const;

	// adds a tutorial to the database if possible
	int addTutorial(const Tutorial&);

	// returns the position on which the existing tutorial is
	// returns -1 if the tutorial doesn't exist in the database
	int getPosOfExistingTutorial(const Tutorial&);

	// returns the tutorial on a given position from the database
	Tutorial getTutorialOnPOs(int pos);

	// deletes a tutorialfrom the database
	void deleteTutorial(int pos);

	// returns the positions on which tutorials with a given presenter are in the database
	std::vector<int> getTutorialsByPresenter(const std::string presenter_to_filter_by, std::vector<int> positions);

	// updates the info of a tutorial (only number of likes and link)
	void updateTutorial(int pos, int updated_likes, std::string updated_link);

	// returns the number of elements from the database
	int getLengthRepo();
};
