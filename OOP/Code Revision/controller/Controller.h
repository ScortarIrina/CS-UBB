//
// Created by Irina Scortar on 02.07.2022.
//

#ifndef CODE_REVISION_CONTROLLER_H
#define CODE_REVISION_CONTROLLER_H

#include "repository/SourceFileRepository.h"
#include "repository/MemberRepository.h"
#include "domain/Subject.h"


class Controller : public Subject {
    SourceFileRepository &files;
    MemberRepository &members;

public:
    Controller(SourceFileRepository &fileRepository, MemberRepository &memberRepository)
        : files(fileRepository), members(memberRepository) {}

    std::vector<SourceFile> getAllSourceFiles() { return this->files.getAll(); }

    std::vector<Member> getAllMembers() { return this->members.getAll(); }

    std::vector<SourceFile> getFilesSortedByName();

    void addFile(const std::string &file_name, Member &member);

    void reviseFile(const std::string &file_name, Member &member);

    ~Controller() = default;
};


#endif //CODE_REVISION_CONTROLLER_H
