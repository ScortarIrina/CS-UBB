//
// Created by Irina Scortar on 01.07.2022.
//

#ifndef BACHELOR_THESES_2_GUI_H
#define BACHELOR_THESES_2_GUI_H

#include <QWidget>
#include "domain/Observer.h"
#include "controller/Controller.h"


QT_BEGIN_NAMESPACE
namespace Ui { class GUI; }
QT_END_NAMESPACE

class GUI : public QWidget, public Observer {
Q_OBJECT

public:
    explicit GUI(Controller &controller, const Teacher &teacher, QWidget *parent = nullptr);

    ~GUI() override;

    void update() override;

    void populateList();

    int getSelectedIndex() const;

    void connectSignalsAndSlots();

    void addAsCoordinator();

    void editStudent();

    void filterList();

private:
    Ui::GUI *ui;
    Controller &controller;
    std::string name;
    Teacher teacher;
};


#endif //BACHELOR_THESES_2_GUI_H
