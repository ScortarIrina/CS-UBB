//
// Created by Irina on 5/5/2022.
//

#ifndef A8_9_SCORTARIRINA_CLION_VALIDATOR_H
#define A8_9_SCORTARIRINA_CLION_VALIDATOR_H

#include "Tutorial.h"


class ValidationException : public std::exception
{
private:
    std::string message;

public:
    explicit ValidationException(std::string& _message);

    const char* what() const noexcept override;
};

class TutorialValidator
{
public:
    TutorialValidator();

    bool validateString(const std::string& input);

    void validateTitle(const std::string& title);

    void validatePresenter(const std::string& presenter);

    void validateDurationString(const std::string& duration);

    void validateNrLikesString(std::string likes);

    void validateNrLikes(int likes);

    void validateVideoLink(const std::string& link);

    ~TutorialValidator();
};


#endif //A8_9_SCORTARIRINA_CLION_VALIDATOR_H
