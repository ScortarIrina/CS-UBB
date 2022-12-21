#include "UI.h"
#include "Repository.h"
#include "Service.h"
#include "UserService.h"
#include "Validator.h"


int main()
{
    std::vector<Tutorial> adminRepoVector;
    adminRepoVector.reserve(10);
    std::string filename = R"(/home/irina/Desktop/CLion_projects/a8-9-ScortarIrina/Project1/Tutorials.txt)";
    Repository repo{ adminRepoVector, filename };
//    repo.loadTutorialsFromFile();
    repo.initialiseRepo();
    Watchlist watchlist;
    Service service{ repo, watchlist };
    UserService userService{ repo };
    TutorialValidator validator{};
    UI ui{ service, userService, validator };
    ui.start();
    return 0;
}