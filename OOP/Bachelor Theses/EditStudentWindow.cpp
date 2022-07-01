//
// Created by Irina Scortar on 01.07.2022.
//

// You may need to build the project (run Qt uic code generator) to get "ui_EditStudentWindow.h" resolved

#include "EditStudentWindow.h"
#include "ui_EditStudentWindow.h"


EditStudentWindow::EditStudentWindow(Controller &controller, Teacher teacher, QWidget *parent)
    : controller(controller), teacher(teacher), QWidget(parent), ui(new Ui::EditStudentWindow)
{
    ui->setupUi(this);

    this->populateList();

    this->connectSignalsAndSlots();
}

EditStudentWindow::~EditStudentWindow() = default;

void EditStudentWindow::populateList() {
    this->ui->studentsListWidget->clear();
    std::vector<Student> entities = this->controller.getAllStudentsByCoordinator(this->teacher.getName());
    for (auto& entity : entities)
    {
        this->ui->studentsListWidget->addItem(QString::fromStdString(entity.getId() + " - " + entity.getName() + " - " + entity.getEmail() + " - " + std::to_string(entity.getYear()) + " - " + entity.getTitle() + " - " + entity.getCoordinator()));
    }
}

void EditStudentWindow::connectSignalsAndSlots() {
    QWidget::connect(this->ui->savePushButton, &QPushButton::clicked, this, &EditStudentWindow::editStudent);
}

void EditStudentWindow::update() {
    this->populateList();
}

void EditStudentWindow::editStudent() {
    std::string newEmail = this->ui->emailLineEdit->text().toStdString();
    std::string newTitle = this->ui->titleLineEdit->text().toStdString();
    int selectedIndex = this->getSelectedIndex();

    if (!newEmail.empty()) {
        this->controller.updateEmail(this->controller.getAllStudentsByCoordinator(this->teacher.getName())[selectedIndex].getId(), newEmail);
    }
    if (!newTitle.empty()) {
        this->controller.updateTitle(this->controller.getAllStudentsByCoordinator(this->teacher.getName())[selectedIndex].getId(), newTitle);
    }
}

int EditStudentWindow::getSelectedIndex() const {
    QModelIndexList selectedIndices = this->ui->studentsListWidget->selectionModel()->selectedIndexes();
    if (selectedIndices.empty())
    {
        return -1;
    }
    int selectedIndex = selectedIndices.at(0).row();
    return selectedIndex;
}
