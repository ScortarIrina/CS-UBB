//
// Created by irina on 23.05.2022.
//

#ifndef TEST3_PRACTICE_GUI_GUI_H
#define TEST3_PRACTICE_GUI_GUI_H

#include "Service.h"
#include <QWidget>
#include <QLabel>
#include <QPushButton>
#include <QListWidget>
#include <QLineEdit>
#include <cstdlib>
#include <iostream>


class DogListModel: public QAbstractListModel
{
private:
    Repository& repository;

public:
    explicit DogListModel(Repository& repo): repository{ repo } {};

    int rowCount(const QModelIndex& parent = QModelIndex()) const override;

    QVariant data(const QModelIndex& index, int role = Qt::DisplayRole) const override;
};


class GUI: public QWidget
{
private:
    Service& service;
    Repository& repository;

    void initGUI();

    QLabel *titleWidget;
    QListWidget *dogsListWidget;
    QLineEdit *nameLineEdit, *breedLineEdit, *ageLineEdit, *linkLineEdit;
    QPushButton *addButton, *deleteButton, *updateButton;
    DogListModel *listModel;

    void populateList();

    void connectSignalsAndSlots();

    int getSelectedIndex() const;

    void addDog();

    void deleteDog();

    void updateDog();

public:
    explicit GUI(Service& serv, Repository& repo);

    ~GUI() override;
};


#endif //TEST3_PRACTICE_GUI_GUI_H
