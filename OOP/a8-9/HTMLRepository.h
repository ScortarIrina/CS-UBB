//
// Created by Irina on 5/5/2022.
//

#ifndef A8_9_SCORTARIRINA_CLION_HTMLREPOSITORY_H
#define A8_9_SCORTARIRINA_CLION_HTMLREPOSITORY_H
#include "UserRepository.h"


class HTMLRepository : public UserRepository {
public:

    HTMLRepository(const std::vector<Tutorial>& watchlist, const std::string& userFilename);

    std::vector<Tutorial>& getAllUserRepo() override;

    unsigned int getNrElems() override;

    unsigned int getCap() override;

    void addUserRepo(const Tutorial& tutorial) override;

    void writeToFile() override;

    std::string& getFilename() override;

    ~HTMLRepository();

};


#endif //A8_9_SCORTARIRINA_CLION_HTMLREPOSITORY_H
