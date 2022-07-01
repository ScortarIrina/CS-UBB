//
// Created by Irina Scortar on 01.07.2022.
//

#include "ProgrammersRepository.h"

ProgrammersRepository::~ProgrammersRepository() {
    std::ofstream g(this->filepath);
    for(const auto& entity : programmers){
        g << entity << "\n";
    }
    g.close();
}

void ProgrammersRepository::add(const Programmer &programmer) {
    this->programmers.push_back(programmer);
}

void ProgrammersRepository::remove(const int &id) {
    int pos = -1;
    for(int i = 0; i < this->programmers.size(); i++) {
        if (this->programmers[i].getId() == id) {
            pos = i;
            break;
        }
    }
    if (pos == -1) {
        throw AppException("There is no programmer with this id!");
    }
    else {
        this->programmers.erase(this->programmers.begin() + pos);
    }
}

void ProgrammersRepository::update(Programmer &programmer) {
    for(auto& p : this->programmers){
        if(programmer.getId() == p.getId()) {
            p = programmer;
            return;
        }
    }
}

ProgrammersRepository::ProgrammersRepository(const std::string &filepath) {
    std::ifstream f(filepath);
    if(!f){
        throw AppException("File " + filepath + " doesn't exist");
    }

    this->programmers = {};
    Programmer p;

    while(f >> p){
        this->programmers.push_back(p);
    }
    f.close();
}
