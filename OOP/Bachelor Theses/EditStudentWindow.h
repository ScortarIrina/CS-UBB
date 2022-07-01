//
// Created by Irina Scortar on 01.07.2022.
//

#ifndef BACHELOR_THESES_2_EDITSTUDENTWINDOW_H
#define BACHELOR_THESES_2_EDITSTUDENTWINDOW_H

#include <QWidget>
#include "controller/Controller.h"
#include "domain/Observer.h"


QT_BEGIN_NAMESPACE
namespace Ui { class EditStudentWindow; }
QT_END_NAMESPACE

class EditStudentWindow : public QWidget, public Observer {
Q_OBJECT

public:
     EditStudentWindow(Controller &controller, Teacher teacher, QWidget *parent = nullptr);

    ~EditStudentWindow() override;

private:
    Ui::EditStudentWindow *ui;
    Controller& controller;
    Teacher teacher;

    void populateList();

    void connectSignalsAndSlots();

    void update() override;

    void editStudent();

    int getSelectedIndex() const;
};


#endif //BACHELOR_THESES_2_EDITSTUDENTWINDOW_H
