#pragma once
#include <iostream>
#include <string>
#include <cstdlib>


class Duration
{
private:
    int minutes;
    int seconds;

public:
    // constructor
    Duration();

    Duration(int minutes, int seconds);

    // copy constructor
    Duration(const Duration&);

    // destructor
    ~Duration();

    // getters
    int getMinutes();
    int getSeconds();

    // setters
    void setMinutes(int minutes);
    void setSeconds(int seconds);

    std::string toStringDuration() const;

    // overloading '!=' operator
    friend bool operator!=(const Duration& d1, const Duration& d2);

    // overloading equality operator
    friend bool operator==(const Duration& d1, const Duration& d2);

    // overloading '<<' operator
    // used when printing the duration
    friend std::ostream& operator<<(std::ostream& os, const Duration& d);

    friend std::istream& operator>>(std::istream& is, Duration& d);
};

class Tutorial
{
private:
    std::string title;
    std::string presenter;
    std::string link;
    Duration duration;
    int nr_likes;

public:
    // constructor
    Tutorial();

    Tutorial(const std::string title, const std::string presenter, const Duration duration, const int nr_likes, const std::string link);

    // copy constructor
    Tutorial(const Tutorial&);

    // getters
    std::string getTitle() const;
    std::string getPresenter() const;
    std::string getLink() const;
    Duration getDuration() const;
    int getLikes() const;

    // setters
    void setTitle(std::string title);
    void setPresenter(std::string presenter);
    void setDuration(int minutes, int seconds);
    void setLikes(int nr_likes);
    void setLink(std::string link);

    std::string toString() const;

    // overloading equality operator
    friend bool operator==(const Tutorial& t1, const Tutorial& t2);

    // overloading '<<' operator
    // used when printing the tutorials
    friend std::ostream& operator<<(std::ostream& os, const Tutorial& t);

    // overloading '>>' operator
    // used when reading the tutorials
    friend std::istream& operator>>(std::istream& is, Tutorial& t);

    void play() const;
};
