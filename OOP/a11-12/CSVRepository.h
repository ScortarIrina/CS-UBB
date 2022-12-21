//
// Created by Irina on 5/5/2022.
//

#ifndef A8_9_SCORTARIRINA_CLION_CSVREPOSITORY_H
#define A8_9_SCORTARIRINA_CLION_CSVREPOSITORY_H

#include "UserRepository.h"

class CSVRepository : public UserRepository
{
public:
    CSVRepository(const std::vector<Tutorial>& watchlist, const std::string& userFilename);

    std::vector<Tutorial>& getAllUserRepo() override;

    unsigned int getNrElems() override;

    unsigned int getCap() override;

    void addUserRepo(const Tutorial& tutorial) override;

    void writeToFile() override;

    std::string& getFilename() override;

    ~CSVRepository();
};


#endif //A8_9_SCORTARIRINA_CLION_CSVREPOSITORY_H
