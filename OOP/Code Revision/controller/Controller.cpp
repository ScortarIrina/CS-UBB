//
// Created by Irina Scortar on 02.07.2022.
//

#include "Controller.h"
#include <algorithm>


std::vector<SourceFile> Controller::getFilesSortedByName() {
    std::vector<SourceFile> sorted_files = this->files.getAll();

    std::sort(sorted_files.begin(), sorted_files.end(),
              [](const SourceFile &first, const SourceFile &second)
              {
                  return first.getName() < second.getName();
              });

    return sorted_files;
}

void Controller::addFile(const std::string &file_name, Member &member) {
    if (file_name.empty())
        throw AppException("The name of the file cannot be empty!");

    std::vector<SourceFile> all_files = this->files.getAll();
    for (auto file : all_files) {
        if (file.getName() == file_name) {
            throw AppException("The name of the files has to be unique!");
        }
    }

    SourceFile s;
    s.setName(file_name);
    s.setStatus("not_revised");
    s.setCreator(member.getName());
    s.setReviewer("-");
    this->files.add(s);
    this->notify();
}

void Controller::reviseFile(const std::string &file_name, Member &member) {
    std::vector<SourceFile> all_files = this->files.getAll();
    for (auto file : all_files) {
        if (file.getName() == file_name) {
            file.setStatus("revised");
            file.setReviewer(member.getName());
            this->files.update(file);
            this->notify();
        }
    }
}
