//
// Created by irina on 23.05.2022.
//

#include "GUI.h"
#include <QWidget>
#include <QLabel>
#include <QPushButton>
#include <QListWidget>
#include <QLineEdit>
#include <QRadioButton>
#include <string>
#include "Repository.h"
#include "Service.h"
#include <cstdlib>
#include <iostream>
#include <vector>
#include <QVBoxLayout>
#include <QFormLayout>


int DogListModel::rowCount(const QModelIndex &parent) const
{
    return this->repository.getAllDogs().size();
}

QVariant DogListModel::data(const QModelIndex &index, int role) const
{
    int row = index.row();
    Dog currentDog = this->repository.getAllDogs()[row];
    if(role == Qt::DisplayRole)
    {
        return QString::fromStdString(currentDog.getName());
    }
    return QVariant();
}

void GUI::initGUI()
{
    auto *layout = new QVBoxLayout(this);
    QFont titleFont = this->titleWidget->font();
    this->titleWidget->setText("<p style='align:center'><font color=#4D2D52>DOGS</font></p>");
    titleFont.setBold(true);
    titleFont.setItalic(true);
    titleFont.setPointSize(12);
    titleFont.setStyleHint(QFont::System);
    titleFont.setWeight(60);
    this->titleWidget->setFont(titleFont);

    layout->addWidget(this->titleWidget);
    layout->addWidget(this->dogsListWidget);

    auto *dogDetailsLayout = new QFormLayout{};
    dogDetailsLayout->addRow("&Name", this->nameLineEdit);
    dogDetailsLayout->addRow("&Breed", this->breedLineEdit);
    dogDetailsLayout->addRow("&Age", this->ageLineEdit);
    dogDetailsLayout->addRow("&Link", this->linkLineEdit);

    layout->addLayout(dogDetailsLayout);

    auto *buttonsLayout = new QGridLayout{};
    buttonsLayout->addWidget(this->addButton, 0, 0);
    buttonsLayout->addWidget(this->deleteButton, 0, 1);
    buttonsLayout->addWidget(this->updateButton, 0, 2);

    layout->addLayout(buttonsLayout);
}

void GUI::populateList()
{
    this->dogsListWidget->clear();
    std::vector<Dog> allDogs = this->service.getAllDogsService();
    for (Dog& dog: allDogs)
        this->dogsListWidget->addItem("Name: " + QString::fromStdString(dog.getName()) +
                                            "  ||  Breed: " + QString::fromStdString(dog.getBreed()) +
                                            "  ||  Age: " + QString::fromStdString(std::to_string(dog.getAge())) +
                                            "  ||  Photo: " + QString::fromStdString(dog.getPhoto()));
}

void GUI::connectSignalsAndSlots()
{
    QObject::connect(this->dogsListWidget, &QListWidget::itemSelectionChanged, [this]() {
        int selectedIndex = this->getSelectedIndex();
        if (selectedIndex < 0)
            return ;
        Dog dog = this->service.getAllDogsService()[selectedIndex];
        this->nameLineEdit->setText(QString::fromStdString(dog.getName()));
        this->breedLineEdit->setText(QString::fromStdString(dog.getBreed()));
        this->ageLineEdit->setText(QString::fromStdString(std::to_string(dog.getAge())));
        this->linkLineEdit->setText(QString::fromStdString(dog.getPhoto()));
    });

    QObject::connect(this->addButton, &QPushButton::clicked, this, &GUI::addDog);
    QObject::connect(this->deleteButton, &QPushButton::clicked, this, &GUI::deleteDog);
    QObject::connect(this->updateButton, &QPushButton::clicked, this, &GUI::updateDog);
}

int GUI::getSelectedIndex() const
{
    QModelIndexList selectedIndexes = this->dogsListWidget->selectionModel()->selectedIndexes();
    if (selectedIndexes.empty()) {
        this->nameLineEdit->clear();
        this->breedLineEdit->clear();
        this->ageLineEdit->clear();
        this->linkLineEdit->clear();
        return -1;
    }
    int selectedIndex = selectedIndexes.at(0).row();
    return selectedIndex;
}

void GUI::addDog()
{
    std::string breed = this->breedLineEdit->text().toStdString();
    std::string name = this->nameLineEdit->text().toStdString();
    std::string age_s = this->ageLineEdit->text().toStdString();
    std::string link = this->linkLineEdit->text().toStdString();
    int age;

    age = stoi(age_s);
    this->service.addDogService(breed, name, age, link);
    this->populateList();

}

void GUI::deleteDog()
{
    std::string name = this->nameLineEdit->text().toStdString();
    this->service.deleteDogService(name);
    this->populateList();
}

void GUI::updateDog()
{
    int index = this->getSelectedIndex();
    std::string old_name = this->service.getAllDogsService()[index].getName();
    std::string new_name = this->nameLineEdit->text().toStdString();
    std::string new_breed = this->breedLineEdit->text().toStdString();
    std::string age_s = this->ageLineEdit->text().toStdString();
    int age;
    std::string new_link = this->linkLineEdit->text().toStdString();
    age = stoi(age_s);
    this->service.updateService(old_name, new_breed, new_name, age, new_link);
    this->populateList();
}

GUI::GUI(Service &serv, Repository &repo)
    :service(serv), repository(repo)
{
    this->titleWidget = new QLabel(this);
    this->dogsListWidget = new QListWidget{};
    this->nameLineEdit = new QLineEdit{};
    this->breedLineEdit = new QLineEdit{};
    this->ageLineEdit = new QLineEdit{};
    this->linkLineEdit = new QLineEdit{};
    this->addButton = new QPushButton("Add");
    this->deleteButton = new QPushButton("Delete");
    this->updateButton = new QPushButton("Update");

    setWindowFlag(Qt::Window);
    this->initGUI();
    this->populateList();
    this->connectSignalsAndSlots();

    this->listModel = new DogListModel{this->repository};
}

GUI::~GUI() = default;
