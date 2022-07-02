//
// Created by Irina Scortar on 02.07.2022.
//

#include "MemberRepository.h"

MemberRepository::MemberRepository(const std::string &filepath) {
    std::ifstream f(filepath);
    if(!f){
        throw AppException("File " + filepath + " doesn't exist");
    }

    this->members = {};
    Member m;

    while(f >> m){
        this->members.push_back(m);
    }
    f.close();
}

MemberRepository::~MemberRepository() {
    std::ofstream g(this->filepath);
    for(const auto& entity : members){
        g << entity << "\n";
    }
    g.close();
}

void MemberRepository::add(const Member &member) {
    this->members.push_back(member);
}

void MemberRepository::update(Member &member) {
    for(auto& m : this->members){
        if(m.getName() == member.getName()) {
            m = member;
            return;
        }
    }
}
