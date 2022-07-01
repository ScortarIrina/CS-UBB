#include <QApplication>
#include <QPushButton>
#include "ui/GUIManager.h"


int main(int argc, char *argv[]) {
    QApplication a(argc, argv);
    StudentRepository students("/Users/irinascortar/CLionProjects/bachelor-theses-2/students.txt");
    TeacherRepository teachers("/Users/irinascortar/CLionProjects/bachelor-theses-2/teachers.txt");
    Controller c(students, teachers);
    GUIManager gui(c);
    return QApplication::exec();
}
