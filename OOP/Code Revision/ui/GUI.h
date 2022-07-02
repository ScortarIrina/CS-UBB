//
// Created by Irina Scortar on 02.07.2022.
//

#ifndef CODE_REVISION_GUI_H
#define CODE_REVISION_GUI_H

#include <QWidget>
#include "controller/Controller.h"
#include "domain/Observer.h"


QT_BEGIN_NAMESPACE
namespace Ui { class GUI; }
QT_END_NAMESPACE

class GUI : public QWidget, public Observer {
Q_OBJECT

public:
    GUI(Controller &controller, Member member, QWidget *parent = nullptr);

    ~GUI() override;

    void update() override;

    void connectSignalsAndSlots();

    void populateList();

    void addFile();

    void reviseFile();

    void activateReviseButton();

    int getSelectedIndex() const;

private:
    Ui::GUI *ui;
    Controller &controller;
    Member member;
};


#endif //CODE_REVISION_GUI_H
