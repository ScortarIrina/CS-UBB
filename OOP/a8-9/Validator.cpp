//
// Created by Irina on 5/5/2022.
//

#include "Validator.h"

TutorialValidator::TutorialValidator()
{
}

bool TutorialValidator::validateString(const std::string& input)
{
    for (char i : input)
        if (isdigit(i) != false)
            return false;
    return true;
}

void TutorialValidator::validateTitle(const std::string& title)
{
    std::string errors;
    if (!validateString(title))
        errors += std::string("The title contains digits!");
    if (title.length() == 0)
        errors += std::string("The title is empty!");
    if (!isupper(title[0]))
        errors += std::string("The title should start with a capital letter!");
    if (!errors.empty())
        throw ValidationException(errors);
}

void TutorialValidator::validatePresenter(const std::string& presenter)
{
    std::string errors;
    if (!validateString(presenter))
        errors += std::string("The presenter name input contains digits!");
    if (presenter.length() == 0)
        errors += std::string("The presenter name input is empty!");
    if (!isupper(presenter[0]))
        errors += std::string("The presenter name should start with a capital letter!");
    if (!errors.empty())
        throw ValidationException(errors);
}

void TutorialValidator::validateDurationString(const std::string& duration)
{
    std::string errors;
    if (duration.empty())
        errors += std::string("The duration input is empty!");
    if (duration.find_first_not_of(":0123456789") != std::string::npos)
        errors += std::string("The duration has non-digit characters!");
    if (duration.size() != 5)
        errors += std::string("The duration has invalid format!");
    if (duration[2] != ':')
        errors += std::string("The separator between minutes and seconds has to be ':'!");
    if (duration[0] > '5')
        errors += std::string("Invalid minutes format!");
    if (duration[3] > '5')
        errors += std::string("Invalid seconds format!");
    if (!errors.empty())
        throw ValidationException(errors);
}

void TutorialValidator::validateNrLikesString(std::string likes)
{
    std::string errors;
    if (likes.empty())
        errors += std::string("The likes input is empty!");
    if (likes.find_first_not_of("0123456789") != std::string::npos)
        errors += std::string("The duration has non-digit characters!");
    if (!errors.empty())
        throw ValidationException(errors);
}

void TutorialValidator::validateNrLikes(int likes)
{
    std::string errors;
    if (likes < 0)
        errors += std::string("The number of likes cannot be a negative number!");
    if (!errors.empty())
        throw ValidationException(errors);
}

void TutorialValidator::validateVideoLink(const std::string& link)
{
    std::string errors;
    if (link.length() == 0)
        errors += std::string("The link input is empty!");
    if (link.find("www") == std::string::npos)
        errors += std::string("The link is not a valid one!");
    if (!errors.empty())
        throw ValidationException(errors);
}

TutorialValidator::~TutorialValidator() = default;

ValidationException::ValidationException(std::string& _message)
        : message(_message)
{
}

const char* ValidationException::what() const noexcept
{
    return message.c_str();
}

