//
// Created by Irina Scortar on 01.07.2022.
//

#ifndef CODE_REVISION_MEMBER_H
#define CODE_REVISION_MEMBER_H

#include <string>


class Member {
    std::string name;
    int revised_files;
    int total_files;

public:
    Member(std::string name, int revised_files, int total_files)
        : name(name), revised_files(revised_files), total_files(total_files) {}

    Member() = default;

    ~Member() = default;

    /// getters
    std::string getName() { return this->name; }
    int getRevisedFiles() const { return this->revised_files; }
    int getTotalFiles() const { return this->total_files; }

    /// setters
    void setName(std::string new_name) { this->name = new_name; }
    void setRevisedFiles(int nr) { this->revised_files = nr; }
    void setTotalFiles(int nr) { this->total_files = nr; }

    /// overloading operators
    friend std::ostream &operator<<(std::ostream &os, const Member &member);
    friend std::istream &operator>>(std::istream &is, Member &member);
};


#endif //CODE_REVISION_MEMBER_H
