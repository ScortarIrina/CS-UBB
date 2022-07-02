//
// Created by Irina Scortar on 02.07.2022.
//

#include "SourceFileRepository.h"

SourceFileRepository::SourceFileRepository(const std::string &filepath) {
    std::ifstream f(filepath);
    if(!f){
        throw AppException("File " + filepath + " doesn't exist");
    }

    this->files = {};
    SourceFile file;

    while(f >> file){
        this->files.push_back(file);
    }
    f.close();
}

SourceFileRepository::~SourceFileRepository() {
    std::ofstream g(this->filepath);
    for(const auto& entity : files){
        g << entity << "\n";
    }
    g.close();
}

void SourceFileRepository::add(const SourceFile &file) {
    this->files.push_back(file);
}

void SourceFileRepository::update(SourceFile &file) {
    for(auto& f : this->files){
        if(f.getName() == file.getName()) {
            f = file;
            return;
        }
    }
}
