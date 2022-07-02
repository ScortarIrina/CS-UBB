//
// Created by Irina Scortar on 01.07.2022.
//

#include <vector>
#include <sstream>
#include "Member.h"
#include "AppException.h"

std::ostream &operator<<(std::ostream &os, const Member &member) {
    os << member.name << "|"  << member.revised_files << "|" << member.total_files;
    return os;
}

std::istream &operator>>(std::istream &is, Member &member) {
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

    if (parts.size() != 3)
        throw AppException("Invalid line for team member");

    std::istringstream name_stream(parts[0]), revised_files_stream(parts[1]), total_files_stream(parts[2]);
    name_stream >> member.name;
    revised_files_stream >> member.revised_files;
    total_files_stream >> member.total_files;

    return is;
}
