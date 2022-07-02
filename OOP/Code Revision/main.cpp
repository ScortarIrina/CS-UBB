#include <QApplication>
#include <QPushButton>
#include "controller/Controller.h"
#include "ui/GUIManager.h"

int main(int argc, char *argv[]) {
    QApplication a(argc, argv);
    MemberRepository members("/Users/irinascortar/CLionProjects/code-revision/members.txt");
    SourceFileRepository files("/Users/irinascortar/CLionProjects/code-revision/files.txt");
    Controller c(files, members);
    GUIManager gui(c);
    return QApplication::exec();
}
