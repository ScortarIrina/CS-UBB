//
// Created by Irina Scortar on 01.07.2022.
//

#ifndef TASK_MANAGER_2_GUI_H
#define TASK_MANAGER_2_GUI_H

#include <QWidget>
#include "controller/Controller.h"
#include "domain/Observer.h"


QT_BEGIN_NAMESPACE
namespace Ui { class gui; }
QT_END_NAMESPACE

class gui : public QWidget , public Observer {
Q_OBJECT

public:
    explicit gui(Controller &controller, Programmer programmer, QWidget *parent = nullptr);

    ~gui() override;

    void update() override;

    void connectSignalsAndSlots();

    void populateList();

    void addTask();

    void removeTask();

    void closeTask();

    void startWorkingOnTask();

    void activateDoneButton();

    void activateStartButton();

    int getSelectedIndex() const;

private:
    Ui::gui *ui;
    Controller &controller;
    Programmer programmer;
};


#endif //TASK_MANAGER_2_GUI_H
