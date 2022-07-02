//
// Created by Irina Scortar on 01.07.2022.
//

#ifndef CODE_REVISION_SOURCEFILE_H
#define CODE_REVISION_SOURCEFILE_H

#include <string>


class SourceFile {
    std::string name;
    std::string status;
    std::string creator;
    std::string reviewer;

public:
    SourceFile(std::string name, std::string status, std::string creator, std::string reviewer)
        : name(name), status(status), creator(creator), reviewer(reviewer) {}

    SourceFile() = default;

    ~SourceFile() = default;

    /// getters
    std::string getName() const { return this->name; }
    std::string getStatus() const {return this->status; }
    std::string getCreator() const { return this->creator; }
    std::string getReviewer() const { return this->reviewer; }

    /// setters
    void setName(std::string new_name) { this->name = new_name; }
    void setStatus(std::string new_status) { this->status = new_status; }
    void setCreator(std::string new_creator) { this->creator = new_creator; }
    void setReviewer(std::string new_reviewer) { this->reviewer = new_reviewer; }

    /// overloading operators
    friend std::ostream &operator<<(std::ostream &os, const SourceFile &file);
    friend std::istream &operator>>(std::istream &is, SourceFile &file);
};


#endif //CODE_REVISION_SOURCEFILE_H
