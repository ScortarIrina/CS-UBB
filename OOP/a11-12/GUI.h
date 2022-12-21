//
// Created by irina on 08.05.2022.
//

#ifndef A11_12_SCORTARIRINA_GUI_H
#define A11_12_SCORTARIRINA_GUI_H

#include <QWidget>
#include <QLabel>
#include <QPushButton>
#include <QListWidget>
#include <QLineEdit>
#include <QRadioButton>
#include <string>
#include "Validator.h"
#include "Repository.h"
#include "Service.h"
#include "UserService.h"
#include <cstdlib>
#include <iostream>
#include <vector>


class TutorialListModel : public QAbstractListModel
{
private:
    Repository& repository;

public:
    explicit TutorialListModel(Repository& repo): repository{ repo } {};

    int rowCount(const QModelIndex& parent = QModelIndex()) const override;

    QVariant data(const QModelIndex& index, int role = Qt::DisplayRole) const override;
};


class GUI: public QWidget
{
private:
    Service& ui;
    UserService& userService;
    TutorialValidator& validator;
    Repository& r;

    void initGUI();

    QLabel* titleWidget;
    QPushButton* adminButton;
    QPushButton* userButton;

    void showAdmin();
    void showUser();
    void connectSignalsAndSlots();

public:
    explicit GUI(Service& service, UserService& userService, TutorialValidator& v, Repository& r);
    ~GUI() override;
};


class AdminGUI: public QWidget
{
private:
    Service& ui;
    TutorialValidator& validator;
    Repository& repo;

    void initAdminGUI();

    QLabel* titleWidget;
    QListWidget* tutorialsListWidget;
    QListWidget* filtered;
    QLineEdit* titleLineEdit, *presenterLineEdit, *durationLineEdit, *likesLineEdit, *linkLineEdit, *presenterFilteredLineEdit;
    QPushButton *printAllButton, *addButton, *deleteButton, *updateButton, *chartButton, *filterButton, *backButton;
    TutorialListModel* listModel;

    void populateList();
    void connectSignalsAndSlots();
    int getSelectedIndex() const;
    void addTutorial();
    void deleteTutorial();
    void updateTutorial();
    void filterByPresenter();

    QWidget* chartWindow;

public:
    explicit AdminGUI(QWidget* parent, Service& serv, TutorialValidator& validator1, Repository& repo);
    ~AdminGUI() override;
};


class UserGUI: public QWidget
{
private:
    Service& service;
    UserService& userService;
    TutorialValidator& validator;

    void initUserGUI();
    QLabel* titleWidget;

    QListWidget* tutorialsListWidget, *watchlistWidget;
    QLineEdit* titleLineEdit, *presenterLineEdit, *durationLineEdit, *likesLineEdit, *linkLineEdit, *presenterFilterLineEdit;
    QPushButton* addButton, *filterButton, *openListButton;
    QRadioButton* csvButton, *htmlButton;

    bool repoTypeSelected;
    bool filtered;
    void populateTutorialList();
    void populateWatchlist();
    void connectSignalsAndSlots();
    int getSelectedIndex() const;
    void addTutorial();
    void filterTutorials();

public:
    explicit UserGUI(QWidget* parent, Service& serv, UserService& userserv, TutorialValidator& validator1);
    ~UserGUI() override;
};

#endif //A11_12_SCORTARIRINA_GUI_H
