#include <QApplication>
#include <QPushButton>
#include "GUI.h"
#include "Repository.h"
#include "Service.h"
#include "UserService.h"
#include "Validator.h"


int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    std::vector<Tutorial> adminRepoVector;
    std::string filename = R"(/home/irina/Desktop/CLion_projects/a11-12-ScortarIrina/Tutorials.txt)";
    Repository repo{adminRepoVector, filename};
    repo.initialiseRepo();
    Watchlist watchlist;
    Service service{repo, watchlist};
    UserService userService{repo};
    TutorialValidator validator{};
    GUI gui{service, userService, validator, repo};
    gui.show();
    return QApplication::exec();

}
