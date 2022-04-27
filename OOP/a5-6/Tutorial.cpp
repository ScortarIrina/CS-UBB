#include "Tests.h"
#include <assert.h>

void Tests::testDynamicVector()
{
	Tutorial t1("a", "aa", Duration(1, 1), 100, "https://www.youtube.com/watch?v=iVLQeWbgbXs");
	Tutorial t2("b", "bb", Duration(2, 2), 200, "https://www.youtube.com/watch?v=rtgwvkaYt1A");
	Tutorial t3("c", "cc", Duration(3, 3), 300, "https://www.youtube.com/watch?v=wJ1L2nSIV1s");
	Tutorial t4("d", "dd", Duration(4, 4), 400, "https://www.youtube.com/watch?v=NUZdUSqsCs4");
	Tutorial t5("e", "ee", Duration(5, 5), 500, "https://www.youtube.com/watch?v=MR37gqFEmFA");
	Tutorial t6("f", "ff", Duration(5, 5), 500, "https://www.youtube.com/watch?v=R37gqFEmFA");
	Tutorial t7("g", "gg", Duration(5, 5), 500, "https://www.youtube.com/watch?v=M7gqFEmFA");
	Tutorial t8("h", "hh", Duration(5, 5), 500, "https://www.youtube.com/watch?v=MR3gqFEmFA");
	Tutorial t9("i", "ii", Duration(5, 5), 500, "https://www.youtube.com/watch?v=R37gqFEmFA");
	Tutorial t10("j", "jj", Duration(5, 5), 500, "https://www.youtube.com/watch?v=R37gqFEmFA");
	Tutorial t11("j", "jj", Duration(5, 5), 500, "https://www.yo.com/watch?v=R37gqFEmFA");

	DynamicVector<Tutorial> v1;
	v1.addElem(t1);
	v1.addElem(t2);
	assert(v1.getLength() == 2);
	t6 = v1.getAllElems()[0];
	assert(t6 == t1);
	DynamicVector<Tutorial> v2;
	v2 = v1;
	assert(v2[0] == t1);
	assert(v2[1] == t2);
	v1.deleteElem(1);
	assert(v1.getLength() == 1);
	v1.addElem(t1);
	v1.addElem(t1);
	v1.addElem(t1);
	v1.addElem(t1);
	v1.addElem(t1);
	v1.addElem(t1);
	v1.addElem(t1);
	v1.addElem(t1);
	v1.addElem(t1);
	v1.deleteElem(4);
	assert(v1.getLength() == 9);
	Tutorial aux = v1[0];
	v1 + aux;
	aux + v1;
	DynamicVector<Tutorial> v4;
	v4.addElem(t3);
	v4.addElem(t3);
	v4.addElem(t3);
	v4.addElem(t3);
	v4.addElem(t3);
	v4.addElem(t3);
	v4.addElem(t3);
	v4.addElem(t3);
	v4.addElem(t3);
	v4.addElem(t3);
	v4.addElem(t3);

	DynamicVector<Tutorial> v3;
	v3 = v3;
	v3.addElem(t4);
	v3.addElem(t3);
	DynamicVector<Tutorial> v33(v3);
	assert(v33.getLength() == v3.getLength());

	DynamicVector<Tutorial> v44;
	v44.addElem(t1);
	v44.addElem(t2);
	v44.addElem(t3);
	v44.addElem(t4);
	v44.addElem(t5);
	v44.addElem(t6);
	v44.addElem(t7);
	v44.addElem(t8);
	v44.addElem(t9);
	v44.addElem(t10);
	v44+ t11;
}

void Tests::testTutorial()
{
	Duration d;
	d.setMinutes(12);
	d.setSeconds(34);
	assert(d.getMinutes() == 12);
	assert(d.getSeconds() == 34);
	std::cout << d;

	Tutorial t;
	t.setTitle("e");
	t.setPresenter("ee");
	t.setDuration(11, 11);
	t.setLikes(12345);
	t.setLink("cucu");
	Duration d1;
	d1.setMinutes(11);
	d1.setSeconds(11);
	std::cout << t;

	assert(t.getTitle() == "e");
	assert(t.getPresenter() == "ee");
	assert(t.getDuration() == d1);
	assert(t.getLikes() == 12345);
	assert(t.getLink() == "cucu");
	
	Duration d2(12, 22);
	assert(d != d1);
	assert(d == d);
	assert(!(d != d));
	assert(d != d2);
	assert(!(d == d2));

	Tutorial t4("d", "dd", Duration(4, 4), 400, "https://www.youtube.com/watch?v=NUZdUSqsCs4");
	Tutorial t5("d", "dd", Duration(4, 4), 400, "https://www.youtube.com/watch?v=NUZdUSqsCs4");
	assert(t4 == t5);
	Tutorial t6("dd", "dd", Duration(4, 4), 400, "https://www.youtube.com/watch?v=NUZdUSqsCs4");
	assert((t4 == t6));
	Tutorial t7("d", "ddd", Duration(4, 4), 400, "https://www.youtube.com/watch?v=NUZdUSqsCs4");
	assert((t4 == t7));
	Tutorial t8("d", "dd", Duration(3, 4), 400, "https://www.youtube.com/watch?v=NUZdUSqsCs4");
	assert((t4 == t8));
	Tutorial t9("d", "dd", Duration(4, 4), 40, "https://www.youtube.com/watch?v=NUZdUSqsCs4");
	assert((t4 == t9));
	Tutorial t10("d", "dd", Duration(4, 4), 400, "ttps://www.youtube.com/watch?v=NUZdUSqsCs4");
	assert((t4 == t10) == false);
}

void Tests::testRepository()
{
	Repository repo;
	Tutorial t1("a", "aa", Duration(1, 1), 100, "https://www.youtube.com/watch?v=iVLQeWbgbXs");
	Tutorial t2("aa", "aa", Duration(12, 21), 1002, "https://www.youtube.com/watch?v=iVLQeWgbXs");
	int res1 = repo.addTutorial(t1);
	assert(res1 == 0);
	repo.addTutorial(t2);
	std::vector<int> positions(2, -1);
	positions = repo.getTutorialsByPresenter("aa", positions);
	assert(positions.size() == 4);
	assert(repo.getTutorialOnPOs(0) == t1);
	assert(repo.getTutorials()[0] == t1);
	assert(repo.getLengthRepo() == 2);
	Tutorial t3("aa", "aa", Duration(12, 21), 1002, "https://www.youtube.com/watch?v=iVLQeWgbXs");
	int res2 = repo.addTutorial(t3);
	assert(res2 == -1);
	repo.deleteTutorial(1);
	repo.updateTutorial(0, 111, "asdfasdf");
	DynamicVector<Tutorial> dv;
	Repository repo2(dv);
}

void Tests::testService()
{
	Repository repo;
	Watchlist w;
	Service s(repo, w);

	s.addTutorialService("a", "aa", Duration(12, 12), 123, "asdfasdf");
	Tutorial t1("a", "aa", Duration(12, 12), 123, "asdfasdf");
	assert(t1 == s.getTutorialOnPOsService(0));
	s.addTutorialWatchlistService(t1);
	assert(t1 == s.getTutorialOnPOsWatchlistService(0));
	assert(s.getLengthWatchlistService() == 1);
	s.deleteTutorialFromWatchlistService(0);
	assert(s.getLengthWatchlistService() == 0);
	assert(s.getLengthService() == 1);
	assert(s.getPosOfExistingTutorialService(t1) == 0);
	assert(s.getLengthWatchlistService() == 0);
	Tutorial* t = s.getTutorialsWatchlistService();
	assert(w.getLengthWatchlist() == 0);
	s.deleteTutorialService("a", "aa", Duration(12, 12), 123, "asdfasdf");
	assert(s.getLengthService() == 0);
	assert(s.deleteTutorialService("b", "bb", Duration(12, 12), 123, "asdfasdf") == -1);

	s.addTutorialService("a", "aa", Duration(12, 12), 123, "asdfasdf");
	assert(s.getTutorialsService()[0] == Tutorial("a", "aa", Duration(12, 12), 123, "asdfasdf"));

	s.updateTutorialService("a", "aa", Duration(12, 12), 123, "asdfasdf", 111, "aaa");
	assert(s.getTutorialsService()[0] == Tutorial("a", "aa", Duration(12, 12), 111, "aaa"));
	s.deleteTutorialService("a", "aa", Duration(12, 12), 111, "aaa");
	assert(s.updateTutorialService("a", "aa", Duration(12, 12), 123, "asdfasdf", 111, "aaa") == -1);

	Tutorial t2("a", "aa", Duration(1, 1), 100, "https://www.youtube.com/watch?v=iVLQeWbgbXs");
	Tutorial t3("aa", "aa", Duration(12, 21), 1002, "https://www.youtube.com/watch?v=iVLQeWgbXs");
	s.addTutorialService("a", "aa", Duration(1, 1), 100, "https://www.youtube.com/watch?v=iVLQeWbgbXs");
	s.addTutorialService("aa", "aa", Duration(12, 21), 1002, "https://www.youtube.com/watch?v=iVLQeWgbXs");
	std::vector<int> positions1(2, -1);
	std::vector<int> positions2(2, -1);
	positions1 = s.getByPresenter("aa", positions1);
	positions2 = s.getByPresenter("", positions2);
}

void Tests::testWatchlist()
{
	Watchlist w;
	DynamicVector<Tutorial> dv;
	Watchlist w1(dv);

	Tutorial t1("a", "aa", Duration(1, 1), 100, "https://www.youtube.com/watch?v=iVLQeWbgbXs");
	Tutorial t2("b", "bb", Duration(2, 2), 200, "https://www.youtube.com/watch?v=rtgwvkaYt1A");

	w.addTutorial(t1);
	assert(w.addTutorial(t1) == 0);
	assert(w.getTutorialOnPos(0) == t1);
	w.play();
	w.addTutorial(t2);
	w.next();
}

#pragma once
#include "DynamicVector.h"
#include "Tutorial.h"
#include "Repository.h"
#include "Service.h"

class Tests
{
public:
	void testDynamicVector();
	void testTutorial();
	void testRepository();
	void testService();
	void testWatchlist();
};
#include "Tutorial.h"


Duration::Duration()
{
	minutes = 0;
	seconds = 0;
}

Duration::Duration(int minutes, int seconds)
{
	this->minutes = minutes;
	this->seconds = seconds;
}

Duration::Duration(const Duration& d)
{
	minutes = d.minutes;
	seconds = d.seconds;
}

Duration::~Duration()
{
	minutes = seconds = 0;
}

int Duration::getMinutes()
{
	return minutes;
}

int Duration::getSeconds()
{
	return seconds;
}

void Duration::setMinutes(int minutes)
{
	this->minutes = minutes;
}

void Duration::setSeconds(int seconds)
{
	this->seconds = seconds;
}

Tutorial::Tutorial()
	: title(""), presenter(""), duration(), nr_likes(), link("")
{
}

Tutorial::Tutorial(std::string _title, std::string _presenter, Duration _duration, int _nr_likes, std::string _link)
	: title(_title), presenter(_presenter), duration(_duration), nr_likes(_nr_likes), link(_link)
{
}

Tutorial::Tutorial(const Tutorial& t)
	: title(t.title), presenter(t.presenter), duration(t.duration), nr_likes(t.nr_likes), link(t.link)
{ 
}

std::string Tutorial::getTitle() const
{
	return this->title;
}

std::string Tutorial::getPresenter() const
{
	return this->presenter;
}

Duration Tutorial::getDuration() const
{
	return this->duration;
}

int Tutorial::getLikes() const
{
	return this->nr_likes;
}

std::string Tutorial::getLink() const
{
	return this->link;
}

bool operator!=(const Duration& d1, const Duration& d2)
{
	if (d1.minutes != d2.minutes)
		return true;
	else if (d1.seconds != d2.seconds)
		return true;
	return false;
}

bool operator==(const Duration& d1, const Duration& d2)
{
	if (d1.minutes == d2.minutes && d1.seconds == d2.seconds)
		return true;
	return false;
}

std::ostream& operator<<(std::ostream& os, const Duration& d)
{
	os << d.minutes << ":" << d.seconds;
	return os;
}


bool operator==(const Tutorial& t1, const Tutorial& t2)
{
	if (t1.link != t2.link)
		return false;
	return true;
}

std::ostream& operator<<(std::ostream& os, const Tutorial& t)
{
	os << "  TITLE: " << t.title << "\n       PRESENTER: " << t.presenter <<  "\n       DURATION: "  << t.getDuration() << 
		"\n       LIKES: " << t.nr_likes << "\n       LINK: " << t.link;
	return os;
}

void Tutorial::setTitle(std::string title)
{
	this->title = title;
}

void Tutorial::setPresenter(std::string presenter)
{
	this->presenter = presenter;
}

void Tutorial::setDuration(int minutes, int seconds)
{
	this->duration.setMinutes(minutes);
	this->duration.setSeconds(seconds);
}

void Tutorial::setLikes(int nr_likes)
{
	this->nr_likes = nr_likes;
}

void Tutorial::setLink(std::string link)
{
	this->link = link;
}

void Tutorial::play() const
{
	ShellExecuteA(NULL, NULL, "chrome.exe", this->getLink().c_str(), NULL, SW_SHOWMAXIMIZED);
}
