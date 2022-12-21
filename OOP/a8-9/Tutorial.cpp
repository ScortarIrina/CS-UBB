#include "Tutorial.h"
#include <utility>
#include <vector>
#include <sstream>


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
    if (d1.minutes != d2.minutes || d1.seconds != d2.seconds)
        return true;
    return false;
}

bool operator==(const Duration& d1, const Duration& d2)
{
    if (d1.minutes == d2.minutes && d1.seconds == d2.seconds)
        return true;
    return false;
}

std::vector<std::string> tokenize(const std::string& str, char delimiter)
{
    std::vector<std::string> result;
    std::stringstream ss(str);
    std::string token;
    while (getline(ss, token, delimiter))
        result.push_back(token);

    return result;
}

std::ostream& operator<<(std::ostream& os, const Duration& d)
{
    os << d.minutes << ":" << d.seconds;
    return os;
    //os << d.minutes << ":" << d.seconds;
    //return os;
}

std::istream& operator>>(std::istream& is, Duration& d)
{
    std::string line;
    std::getline(is, line);
    std::vector<std::string> tokens;
    if (line.empty())
        return is;
    tokens = tokenize(line, char(':'));
    d.minutes = std::stoi(tokens[0]);
    d.seconds = std::stoi(tokens[0]);
    return is;

    //std::string colon = ":";
    //is >> d.minutes >> colon >> d.seconds;
    //return is;
}

bool operator==(const Tutorial& t1, const Tutorial& t2)
{
    if (t1.link != t2.link)
        return false;
    return true;
}

std::ostream& operator<<(std::ostream& os, const Tutorial& t)
{
    os << t.title << "," << t.presenter << "," << t.duration << "," << t.nr_likes << "," << t.link;
    return os;

    //os << " TITLE: " << t.title << "\n      PRESENTER: " << t.presenter << "\n      DURATION: " << t.getDuration() <<
    //	"\n      LIKES: " << t.nr_likes << "\n      LINK: " << t.link;
    //return os;
}

std::istream& operator>>(std::istream& is, Tutorial& t)
{
    std::string line;
    std::getline(is, line);
    std::vector<std::string> tokens;
    if (line.empty())
        return is;
    tokens = tokenize(line, ',');
    t.title = tokens[0];
    t.presenter = tokens[1];
    std::string durationAsString = tokens[2];
    std::vector<std::string> tokensForDuration;
    tokensForDuration = tokenize(durationAsString, ':');
    t.setDuration(std::stoi(tokensForDuration[0]), std::stoi(tokensForDuration[1]));
    t.nr_likes = std::stoi(tokens[3]);
    t.link = tokens[4];
    return is;

    //std::string space = " ";
    //is >> t.title >> space >> t.presenter >> space >> t.duration >> space >> t.nr_likes >> space >> t.link;
    //return is;
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

std::string Duration::toStringDuration() const
{
    return std::to_string(this->minutes) + ":" + std::to_string(this->seconds);
}

std::string Tutorial::toString() const
{
    auto duration = this->getDuration().toStringDuration();
    return "TITLE: " + this->title + " \n   PRESENTER: " + this->presenter +
           " \n   DURATION: " + duration + " \n   LIKES: " + std::to_string(this->nr_likes) +
           " \n   LINK: " + this->link + "\n";
}

void Tutorial::play() const
{
    system(("firefox " + link).c_str());
}