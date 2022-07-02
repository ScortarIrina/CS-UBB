//
// Created by Irina Scortar on 02.07.2022.
//

#ifndef CODE_REVISION_MEMBERREPOSITORY_H
#define CODE_REVISION_MEMBERREPOSITORY_H

#include "domain/Member.h"
#include "domain/AppException.h"
#include <fstream>
#include <vector>
#include <cstdlib>
#include <algorithm>


class MemberRepository {
    std::vector<Member> members;
    std::string filepath;

public:
    explicit MemberRepository(const std::string &filepath);

    virtual ~MemberRepository();

    void add(const Member &member);

    void update(Member &member);

    std::vector<Member> getAll() { return this->members; }
};


#endif //CODE_REVISION_MEMBERREPOSITORY_H
