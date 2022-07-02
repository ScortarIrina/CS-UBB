//
// Created by Irina Scortar on 01.07.2022.
//

#include <vector>
#include <sstream>
#include "SourceFile.h"
#include "AppException.h"

std::ostream &operator<<(std::ostream &os, const SourceFile &file) {
    os << file.name << "|" << file.status << "|" << file.creator << "|" << file.reviewer;
    return os;
}

std::istream &operator>>(std::istream &is, SourceFile &file) {
    std::string line;
    std::getline(is, line);

    if (line.empty())
        return is;

    std::vector<std::string> parts = {""};

    for (auto it: line) {
        if (it == '|')
            parts.emplace_back("");
        else
            parts.back() += it;
    }

    if (parts.size() != 4)
        throw AppException("Invalid line for source file");

    std::istringstream name_stream(parts[0]), status_stream(parts[1]), creator_stream(parts[2]), reviewer_stream(parts[3]);
    name_stream >> file.name;
    status_stream >> file.status;
    creator_stream >> file.creator;
    reviewer_stream >> file.reviewer;

    return is;
}
