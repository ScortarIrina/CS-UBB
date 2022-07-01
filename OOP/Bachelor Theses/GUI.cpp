//
// Created by Irina Scortar on 01.07.2022.
//

// You may need to build the project (run Qt uic code generator) to get "ui_GUI.h" resolved

#include <QMessageBox>
#include "GUI.h"
#include "ui_GUI.h"
#include "EditStudentWindow.h"


GUI::GUI(Controller &controller, const Teacher &teacher, QWidget *parent)
    : QWidget(parent), ui(new Ui::GUI), controller(controller), teacher(teacher)
{
    ui->setupUi(this);

    this->setWindowTitle(QString::fromStdString(teacher.getName()));
    this->setMinimumWidth(750);

    this->connectSignalsAndSlots();

    this->populateList();

    this->update();
}

void GUI::update() {
    this->ui->studentsListWidget->clear();
    std::vector<Student> students = this->controller.sortStudents();
    for(Student &t : students)
        this->ui->studentsListWidget->addItem(QString::fromStdString(t.getId()) + "   ||   " +
                                              QString::fromStdString(t.getName()) + "   ||   " +
                                              QString::fromStdString(t.getEmail()) + "   ||   " +
                                              QString::fromStdString(std::to_string(t.getYear())) + "   ||   " +
                                              QString::fromStdString(t.getTitle()) + "   ||   " +
                                              QString::fromStdString(t.getCoordinator()));
}

GUI::~GUI() {
    delete ui;
}

void GUI::populateList() {
    this->ui->studentsListWidget->clear();
    std::vector<Student> entities = this->controller.getAllStudentsByCoordinator(name);
    for (auto& entity : entities)
    {
        this->ui->studentsListWidget->addItem(QString::fromStdString(entity.getName()));
    }
}

int GUI::getSelectedIndex() const {
    QModelIndexList selectedIndexes = this->ui->studentsListWidget->selectionModel()->selectedIndexes();
    if (selectedIndexes.empty())
    {
        this->ui->idLineEdit->clear();
        this->ui->nameLineEdit->clear();
        this->ui->yearLineEdit->clear();
        this->ui->emailLineEdit->clear();
        this->ui->titleLineEdit->clear();
        this->ui->coordinatorLineEdit->clear();
        return -1;
    }
    int selectedIndex = selectedIndexes.at(0).row();
    return selectedIndex;
}

void GUI::connectSignalsAndSlots() {
    QObject::connect(this->ui->studentsListWidget, &QListWidget::itemSelectionChanged, [this]()
    {
        int selectedIndex = this->getSelectedIndex();
        if (selectedIndex < 0)
            return;
        Student s = this->controller.getAllStudents()[selectedIndex];
        this->ui->idLineEdit->setText(QString::fromStdString(s.getId()));
        this->ui->nameLineEdit->setText(QString::fromStdString(s.getName()));
        this->ui->yearLineEdit->setText(QString::fromStdString(std::to_string(s.getYear())));
        this->ui->emailLineEdit->setText(QString::fromStdString(s.getEmail()));
        this->ui->titleLineEdit->setText(QString::fromStdString(s.getTitle()));
        this->ui->coordinatorLineEdit->setText(QString::fromStdString(s.getCoordinator()));
    });

    QWidget::connect(ui->coordinatepPushButton, &QPushButton::clicked, this, &GUI::addAsCoordinator);
    QWidget::connect(ui->searchLineEdit, &QLineEdit::textChanged, this, &GUI::filterList);
    QWidget::connect(ui->editPushButton, &QPushButton::clicked, this, &GUI::editStudent);
}

void GUI::addAsCoordinator() {
    try {
        int selectedIndex = this->getSelectedIndex();
        std::string filterString = this->ui->searchLineEdit->text().toStdString();
        std::string studentId = this->controller.filterStudentByNameOrId(filterString)[selectedIndex].getId();
        this->controller.addTeacherAsCoordinator(studentId, teacher.getName());
    }
    catch (AppException &ae) {
        auto *error = new QMessageBox();
        error->setIcon(QMessageBox::Warning);
        error->setText(ae.what());
        error->exec();
    }
}

void GUI::editStudent() {
    auto* window = new EditStudentWindow{ this->controller, this->teacher };
    this->controller.attachObserver(window);
    window->show();
}

void GUI::filterList() {
    this->ui->studentsListWidget->clear();
    std::string filterString = this->ui->searchLineEdit->text().toStdString();
    std::vector<Student> entities = this->controller.filterStudentByNameOrId(filterString);
    for (auto& entity : entities)
    {
        this->ui->studentsListWidget->addItem(QString::fromStdString(entity.getId() + " - " + entity.getName() + " - " + entity.getEmail() + " - " + std::to_string(entity.getYear()) + " - " + entity.getTitle() + " - " + entity.getCoordinator()));
    }
}
