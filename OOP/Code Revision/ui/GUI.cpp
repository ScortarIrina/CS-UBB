//
// Created by Irina Scortar on 02.07.2022.
//

// You may need to build the project (run Qt uic code generator) to get "ui_GUI.h" resolved

#include <QMessageBox>
#include "GUI.h"
#include "ui_GUI.h"


GUI::GUI(Controller &controller1, Member member1, QWidget *parent)
    : QWidget(parent), ui(new Ui::GUI), controller(controller1), member(member1)
{
    ui->setupUi(this);

    this->setWindowTitle(QString::fromStdString(this->member.getName()));

    this->connectSignalsAndSlots();

    this->ui->revisedFilesLineEdit->setText(QString::fromStdString(std::to_string(this->member.getRevisedFiles())));

    this->ui->leftToReviseLineEdit->setText(QString::fromStdString(std::to_string(this->member.getTotalFiles() - this->member.getRevisedFiles())));

    this->populateList();

    this->update();
}

GUI::~GUI() {
    delete ui;
}

void GUI::update() {
    this->ui->filesListWidget->clear();
    std::vector<SourceFile> files = this->controller.getFilesSortedByName();
    for(SourceFile &t : files)
        this->ui->filesListWidget->addItem(QString::fromStdString(t.getName()) + "   ||   " +
                                           QString::fromStdString(t.getStatus()) + "   ||   " +
                                           QString::fromStdString(t.getCreator()) + "   ||   " +
                                           QString::fromStdString(t.getReviewer()));
}

void GUI::connectSignalsAndSlots() {
    QObject::connect(this->ui->filesListWidget, &QListWidget::itemSelectionChanged, [this]()
    {
        int selectedIndex = this->getSelectedIndex();
        if (selectedIndex < 0)
            return;
        SourceFile s = this->controller.getFilesSortedByName()[selectedIndex];
        this->ui->nameLineEdit->setText(QString::fromStdString(s.getName()));
        this->ui->statusLineEdit->setText(QString::fromStdString(s.getStatus()));
        this->ui->cretaorLineEdit->setText(QString::fromStdString(s.getCreator()));
        this->ui->reviewerLineEdit->setText(QString::fromStdString(s.getReviewer()));
    });

    QWidget::connect(ui->addPushButton, &QPushButton::clicked, this, &GUI::addFile);
    QObject::connect(this->ui->filesListWidget, &QListWidget::itemSelectionChanged, this, &GUI::activateReviseButton);
    QWidget::connect(ui->revisePushButton, &QPushButton::clicked, this, &GUI::reviseFile);
}

void GUI::populateList() {
    this->ui->filesListWidget->clear();
    std::vector<SourceFile> entities = this->controller.getFilesSortedByName();
    for (auto& entity : entities)
    {
        this->ui->filesListWidget->addItem(QString::fromStdString(entity.getName()));
    }
}

void GUI::addFile() {
    try {
        std::string name = this->ui->nameLineEdit->text().toStdString();
        this->controller.addFile(name, this->member);
    }
    catch (AppException &ae) {
        auto *error = new QMessageBox();
        error->setIcon(QMessageBox::Critical);
        error->setText(ae.what());
        error->exec();
    }
}

void GUI::reviseFile() {
    try {
        std::string name = this->ui->nameLineEdit->text().toStdString();
        this->controller.reviseFile(name, this->member);
        this->member.setRevisedFiles(this->member.getRevisedFiles() + 1);
        this->ui->leftToReviseLineEdit->setText(QString::fromStdString(std::to_string(this->member.getTotalFiles() -
                                                                                              this->member.getRevisedFiles())));
        std::string left_to_revise = this->ui->leftToReviseLineEdit->text().toStdString();
        if (left_to_revise == "0") {
            auto *congratulations = new QMessageBox();
            congratulations->setIcon(QMessageBox::Information);
            congratulations->setStyleSheet("QLabel{ color: green}");
            congratulations->setText("Congratulations!\nYou reached your goal!");
            congratulations->exec();
        }
    }
    catch (AppException &ae) {
        auto *error = new QMessageBox();
        error->setIcon(QMessageBox::Critical);
        error->setText(ae.what());
        error->exec();
    }
}

void GUI::activateReviseButton() {
    int selectedIndex = this->getSelectedIndex();
    if (selectedIndex != -1)
    {
        if (this->controller.getFilesSortedByName()[selectedIndex].getStatus() == "not_revised" &&
                this->controller.getFilesSortedByName()[selectedIndex].getCreator() != this->member.getName())
            this->ui->revisePushButton->setEnabled(true);
        else
            this->ui->revisePushButton->setEnabled(false);
    }
}

int GUI::getSelectedIndex() const {
    QModelIndexList selectedIndexes = this->ui->filesListWidget->selectionModel()->selectedIndexes();
    if (selectedIndexes.empty())
    {
        this->ui->nameLineEdit->clear();
        this->ui->statusLineEdit->clear();
        this->ui->cretaorLineEdit->clear();
        this->ui->reviewerLineEdit->clear();
        return -1;
    }
    int selectedIndex = selectedIndexes.at(0).row();
    return selectedIndex;
}
