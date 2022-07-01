//
// Created by Irina Scortar on 01.07.2022.
//

// You may need to build the project (run Qt uic code generator) to get "ui_gui.h" resolved

#include <QMessageBox>
#include "gui.h"
#include "ui_gui.h"


gui::gui(Controller &controller, Programmer programmer, QWidget *parent)
    : controller(controller), programmer(programmer), QWidget(parent), ui(new Ui::gui) \
{
    ui->setupUi(this);

    this->setWindowTitle(QString::fromStdString(this->programmer.getName()));

    this->connectSignalsAndSlots();

    this->populateList();

    this->update();
}

gui::~gui() {
    delete ui;
}

void gui::update() {
    this->ui->tasksListWidget->clear();
    std::vector<Task> tasks = this->controller.getTasksSortedByStatus();
    for(Task &t : tasks)
        this->ui->tasksListWidget->addItem(QString::fromStdString(t.getDescription()) + "   ||   " +
                                              QString::fromStdString(t.getStatus()) + "   ||   " +
                                              QString::fromStdString(std::to_string(t.getProgrammerId())));
}

void gui::populateList() {
    this->ui->tasksListWidget->clear();
    std::vector<Task> entities = this->controller.getTasksSortedByStatus();
    for (auto& entity : entities)
    {
        this->ui->tasksListWidget->addItem(QString::fromStdString(entity.getDescription()));
    }
}

void gui::connectSignalsAndSlots() {
    QObject::connect(this->ui->tasksListWidget, &QListWidget::itemSelectionChanged, [this]()
    {
        int selectedIndex = this->getSelectedIndex();
        if (selectedIndex < 0)
            return;
        Task s = this->controller.getTasksSortedByStatus()[selectedIndex];
        this->ui->descriptionLineEdit->setText(QString::fromStdString(s.getDescription()));
        this->ui->statusLineEdit->setText(QString::fromStdString(s.getStatus()));
        this->ui->programmerIdLineEdit->setText(QString::fromStdString(std::to_string(s.getProgrammerId())));
    });

    QWidget::connect(ui->addPushButton, &QPushButton::clicked, this, &gui::addTask);
    QWidget::connect(ui->removePushButton, &QPushButton::clicked, this, &gui::removeTask);
    QObject::connect(this->ui->tasksListWidget, &QListWidget::itemSelectionChanged, this, &gui::activateDoneButton);
    QWidget::connect(ui->donePushButton, &QPushButton::clicked, this, &gui::closeTask);
    QWidget::connect(ui->startPushButton, &QPushButton::clicked, this, &gui::startWorkingOnTask);
}

int gui::getSelectedIndex() const {
    QModelIndexList selectedIndexes = this->ui->tasksListWidget->selectionModel()->selectedIndexes();
    if (selectedIndexes.empty())
    {
        this->ui->descriptionLineEdit->clear();
        this->ui->statusLineEdit->clear();
        this->ui->programmerIdLineEdit->clear();
        return -1;
    }
    int selectedIndex = selectedIndexes.at(0).row();
    return selectedIndex;
}

void gui::addTask() {
    try {
        std::string description = this->ui->descriptionLineEdit->text().toStdString();
        this->controller.addTask(description, this->programmer);
    }
    catch (AppException &ae) {
        auto *error = new QMessageBox();
        error->setIcon(QMessageBox::Critical);
        error->setText(ae.what());
        error->exec();
    }
}

void gui::removeTask() {
    try {
        std::string description = this->ui->descriptionLineEdit->text().toStdString();
        this->controller.removeTask(description);
    }
    catch (AppException &ae) {
        auto *error = new QMessageBox();
        error->setIcon(QMessageBox::Critical);
        error->setText(ae.what());
        error->exec();
    }
}

void gui::closeTask() {
    try {
        std::string description = this->ui->descriptionLineEdit->text().toStdString();
        this->controller.updateTask(description, "CLOSED");
    }
    catch (AppException &ae) {
        auto *error = new QMessageBox();
        error->setIcon(QMessageBox::Critical);
        error->setText(ae.what());
        error->exec();
    }
}

void gui::startWorkingOnTask() {
    try {
        std::string description = this->ui->descriptionLineEdit->text().toStdString();
        this->controller.updateTask(description, "IN_PROGRESS");
    }
    catch (AppException &ae) {
        auto *error = new QMessageBox();
        error->setIcon(QMessageBox::Critical);
        error->setText(ae.what());
        error->exec();
    }
}

void gui::activateDoneButton() {
    int selectedIndex = this->getSelectedIndex();
    std::string filterString = this->ui->statusLineEdit->text().toStdString();
    if (selectedIndex != -1)
    {
        if (this->controller.getTasksSortedByStatus()[selectedIndex].getStatus() == "IN_PROGRESS")
            this->ui->donePushButton->setEnabled(true);
        else
            this->ui->donePushButton->setEnabled(false);
    }
}

void gui::activateStartButton() {
    int selectedIndex = this->getSelectedIndex();
    std::string filterString = this->ui->statusLineEdit->text().toStdString();
    if (selectedIndex != -1)
    {
        if (this->controller.getTasksSortedByStatus()[selectedIndex].getStatus() == "OPEN")
            this->ui->startPushButton->setEnabled(true);
        else
            this->ui->startPushButton->setEnabled(false);
    }
}
