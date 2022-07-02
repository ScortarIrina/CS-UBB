//
// Created by Irina Scortar on 01.07.2022.
//

#ifndef CODE_REVISION_SUBJECT_H
#define CODE_REVISION_SUBJECT_H

#include "Observer.h"
#include <vector>
#include <algorithm>


class Subject {
    std::vector<Observer*> observers;

public:
    void notify()
    {
        for(auto it:this->observers)
            it->update();
    }

    void attachObserver(Observer *obs)
    {
        this->observers.push_back(obs);
    }

    void detachObserver(Observer *obs)
    {
        auto it = std::find(observers.begin(), observers.end(), obs);
        this->observers.erase(it);
    }
};

#endif //CODE_REVISION_SUBJECT_H
