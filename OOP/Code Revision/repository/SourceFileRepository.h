//
// Created by Irina Scortar on 02.07.2022.
//

#ifndef CODE_REVISION_SOURCEFILEREPOSITORY_H
#define CODE_REVISION_SOURCEFILEREPOSITORY_H

#include "domain/SourceFile.h"
#include "domain/AppException.h"
#include <fstream>
#include <vector>
#include <cstdlib>
#include <algorithm>


class SourceFileRepository {
    std::vector<SourceFile> files;
    std::string filepath;

public:
    explicit SourceFileRepository(const std::string &filepath);

    virtual ~SourceFileRepository();

    void add(const SourceFile &file);

    void update(SourceFile &file);

    std::vector<SourceFile> getAll() { return this->files; }
};


#endif //CODE_REVISION_SOURCEFILEREPOSITORY_H
