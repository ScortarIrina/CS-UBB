#include <QApplication>
#include <QPushButton>
#include "ui/GUIManager.h"


int main(int argc, char *argv[]) {
    QApplication a(argc, argv);
    TasksRepository tasks("/Users/irinascortar/CLionProjects/task-manager-2/tasks.txt");
    ProgrammersRepository programmers("/Users/irinascortar/CLionProjects/task-manager-2/programmers.txt");
    Controller c(tasks, programmers);
    GUIManager gui(c);
    return QApplication::exec();
}
