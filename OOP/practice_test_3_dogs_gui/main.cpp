#include "Repository.h"
#include "Service.h"
#include <QApplication>
#include "GUI.h"

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    std::vector<Dog> adminRepoVector;
    adminRepoVector.reserve(10);
    std::string filename = R"(/home/irina/Desktop/CLion_projects/test3_practice_GUI/Dogs.txt)";
    Repository repo{adminRepoVector, filename};
    repo.initialiseRepo();
    Service service{repo};
    GUI gui{service, repo};
    gui.show();
    return QApplication::exec();
}
