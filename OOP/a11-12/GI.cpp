//
// Created by irina on 08.05.2022.
//

#include "GUI.h"
#include <QVBoxLayout>
#include <QFormLayout>
#include <QErrorMessage>
#include <QMessageBox>

GUI::GUI(Service& service, UserService& userService, TutorialValidator& v, Repository& r)
        : ui(service), userService(userService), validator(v), r(r)
{
    this->titleWidget = new QLabel(this);
    this->adminButton = new QPushButton(this);
    this->userButton = new QPushButton(this);
    this->initGUI();
    this->connectSignalsAndSlots();
}

void GUI::initGUI()
{
    auto* layout = new QVBoxLayout(this);
    QFont titleFont = this->titleWidget->font();
    this->titleWidget->setText("<p style='text-align:center'><font color=#4D2D52>Welcome to Master C++! <br> Select your mode!</font></p>");
    titleFont.setItalic(true);
    titleFont.setPointSize(22);
    titleFont.setStyleHint(QFont::System);
    titleFont.setWeight(100);
    this->titleWidget->setFont(titleFont);
    layout->addWidget(this->titleWidget);
    this->adminButton->setText("Admin mode");
    layout->addWidget(this->adminButton);
    this->userButton->setText("User mode");
    layout->addWidget(this->userButton);
    this->setLayout(layout);
    this->setStyleSheet("background-color:#D9DBF1");
}

GUI::~GUI() = default;

void GUI::connectSignalsAndSlots()
{
    QObject::connect(this->adminButton, &QPushButton::clicked, this, &GUI::showAdmin);
    QObject::connect(this->userButton, &QPushButton::clicked, this, &GUI::showUser);
}

void GUI::showAdmin()
{
    auto* admin = new AdminGUI(this, this->ui, this->validator, this->r);
    admin->show();
}

AdminGUI::AdminGUI(QWidget* parent, Service &serv, TutorialValidator& validator1, Repository& repo)
        : ui{serv}, validator{validator1}, repo{repo}
{
    this->titleWidget = new QLabel(this);
    this->tutorialsListWidget = new QListWidget{};
    this->titleLineEdit = new QLineEdit{};
    this->presenterLineEdit = new QLineEdit{};
    this->durationLineEdit = new QLineEdit{};
    this->likesLineEdit = new QLineEdit{};
    this->linkLineEdit = new QLineEdit{};
    this->presenterFilteredLineEdit = new QLineEdit{};
    this->printAllButton = new QPushButton("Print all");
    this->addButton = new QPushButton("Add");
    this->deleteButton = new QPushButton("Delete");
    this->updateButton = new QPushButton("Update");
    this->filterButton = new QPushButton("Filter by presenter");
    this->backButton = new QPushButton("Back from filter");
    //    this->chartButton = new QPushButton("Display chart");
    setParent(parent);
    setWindowFlag(Qt::Window);
    this->initAdminGUI();
    this->populateList();
    this->connectSignalsAndSlots();
    this->listModel = new TutorialListModel{this->repo};
}

void AdminGUI::initAdminGUI()
{
    auto* layout = new QVBoxLayout(this);
    QFont titleFont = this->titleWidget->font();
    this->titleWidget->setText("<p style='text-align:center'><font color=#4D2D52>ADMIN MODE</font></p>");
    titleFont.setItalic(true);
    titleFont.setPointSize(10);
    titleFont.setStyleHint(QFont::System);
    titleFont.setWeight(63);
    this->titleWidget->setFont(titleFont);
    layout->addWidget(this->titleWidget);

    layout->addWidget(this->tutorialsListWidget);

    auto * tutorialDetailsLayout = new QFormLayout{};
    tutorialDetailsLayout->addRow("Title", this->titleLineEdit);
    tutorialDetailsLayout->addRow("Presenter", this->presenterLineEdit);
    tutorialDetailsLayout->addRow("Duration", this->durationLineEdit);
    tutorialDetailsLayout->addRow("Likes", this->likesLineEdit);
    tutorialDetailsLayout->addRow("Link", this->linkLineEdit);
    tutorialDetailsLayout->addRow("Presenter to filter by", this->presenterFilteredLineEdit);
    layout->addLayout(tutorialDetailsLayout);

    auto* buttonsLayout = new QVBoxLayout{};
    buttonsLayout->addWidget(this->addButton, 0, 0);
    buttonsLayout->addWidget(this->deleteButton, 0, 0);
    buttonsLayout->addWidget(this->updateButton, 0, 0);
    buttonsLayout->addWidget(this->filterButton, 0, 0);
    buttonsLayout->addWidget(this->backButton, 0, 0);
//    buttonsLayout->addWidget(this->chartButton, 0, 0);
    layout->addLayout(buttonsLayout);
}

void AdminGUI::populateList()
{
    this->tutorialsListWidget->clear();
    std::vector<Tutorial> allTutorials = this->ui.getTutorialsService();
    for (Tutorial& t: allTutorials)
        this->tutorialsListWidget->addItem(QString::fromStdString(t.getTitle()) + "   ||   " +
                                           QString::fromStdString(t.getPresenter()) + "   ||   " + QString::fromStdString(t.getDuration().toStringDuration())
                                           + "   ||   " + QString::fromStdString(std::to_string(t.getLikes())) + "   ||   " +
                                           QString::fromStdString(t.getLink()));
}

void AdminGUI::connectSignalsAndSlots()
{
    QObject::connect(this->tutorialsListWidget, &QListWidget::itemSelectionChanged, [this]()
    {
        int selectedIndex = this->getSelectedIndex();
        if (selectedIndex < 0)
            return;
        Tutorial t = this->ui.getTutorialsService()[selectedIndex];
        this->titleLineEdit->setText(QString::fromStdString(t.getTitle()));
        this->presenterLineEdit->setText(QString::fromStdString(t.getPresenter()));
        this->durationLineEdit->setText(QString::fromStdString(t.getDuration().toStringDuration()));
        this->likesLineEdit->setText(QString::fromStdString(std::to_string(t.getLikes())));
        this->linkLineEdit->setText(QString::fromStdString(t.getLink()));
    });

    QObject::connect(this->addButton, &QPushButton::clicked, this, &AdminGUI::addTutorial);
    QObject::connect(this->deleteButton, &QPushButton::clicked, this, &AdminGUI::deleteTutorial);
    QObject::connect(this->updateButton, &QPushButton::clicked, this, &AdminGUI::updateTutorial);
    QObject::connect(this->filterButton, &QPushButton::clicked, this, &AdminGUI::filterByPresenter);
    QObject::connect(this->backButton, &QPushButton::clicked, this, &AdminGUI::populateList);
//    QObject::connect(this->chartButton, &QPushButton::clicked, this, &AdminGUI::displayChart);
}

void AdminGUI::addTutorial()
{
    std::string title= this->titleLineEdit->text().toStdString();
    std::string presenter = this->presenterLineEdit->text().toStdString();
    std::string duration_string = this->durationLineEdit->text().toStdString();
    std::string likes_string = this->likesLineEdit->text().toStdString();
    std::string link = this->linkLineEdit->text().toStdString();
    int likes;
    try
    {
        this->validator.validateTitle(title);
        this->validator.validatePresenter(presenter);
        this->validator.validateDurationString(duration_string);
        likes = stoi(likes_string);
        this->validator.validateNrLikes(likes);
        this->validator.validateVideoLink(link);

        Duration duration;
        int minutes = (int(duration_string[0]) - '0') * 10 + (int(duration_string[1]) - '0');
        int seconds = (int(duration_string[3]) - '0') * 10 + (int(duration_string[4]) - '0');
        duration.setMinutes(minutes);
        duration.setSeconds(seconds);

        this->ui.addTutorialService(title, presenter, duration, likes, link);
        this->populateList();
    }
    catch (ValidationException& exc)
    {
        auto* error = new QMessageBox();
        error->setIcon(QMessageBox::Critical);
        error->setText(exc.what());
        error->setWindowTitle("Invalid input!");
        error->exec();
    }
    catch (RepoException& re)
    {
        auto* error = new QMessageBox();
        error->setIcon(QMessageBox::Critical);
        error->setText(re.what());
        error->setWindowTitle("Error at adding tutorial!");
        error->exec();
    }
}

void AdminGUI::deleteTutorial()
{
    std::string title= this->titleLineEdit->text().toStdString();
    std::string presenter = this->presenterLineEdit->text().toStdString();
    std::string duration_string = this->durationLineEdit->text().toStdString();
    std::string likes_string = this->likesLineEdit->text().toStdString();
    std::string link = this->linkLineEdit->text().toStdString();
    int likes;
    try
    {
        this->validator.validateTitle(title);
        this->validator.validatePresenter(presenter);
        this->validator.validateDurationString(duration_string);
        this->validator.validateNrLikesString(likes_string);
        likes = stoi(likes_string);
        this->validator.validateNrLikes(likes);
        this->validator.validateVideoLink(link);

        Duration duration;
        int minutes = (int(duration_string[0]) - '0') * 10 + (int(duration_string[1]) - '0');
        int seconds = (int(duration_string[3]) - '0') * 10 + (int(duration_string[4]) - '0');
        duration.setMinutes(minutes);
        duration.setSeconds(seconds);

        this->ui.deleteTutorialService(title, presenter, duration, likes, link);
        this->populateList();
    }
    catch (ValidationException& exc)
    {
        auto* error = new QMessageBox();
        error->setIcon(QMessageBox::Critical);
        error->setText(exc.what());
        error->setWindowTitle("Invalid input!");
        error->exec();
    }
    catch (RepoException& re)
    {
        auto* error = new QMessageBox();
        error->setIcon(QMessageBox::Critical);
        error->setText(re.what());
        error->setWindowTitle("Error at deleting tutorial!");
        error->exec();
    }
}

void AdminGUI::updateTutorial()
{
    int index = this->getSelectedIndex();
    try
    {
        if (index < 0)
        {
            auto* error = new QMessageBox();
            error->setIcon(QMessageBox::Critical);
            error->setText("No tutorial selected!");
            error->setWindowTitle("Selection error!");
            error->exec();
        }
        else
        {
            std::string title = this->ui.getTutorialsService()[index].getTitle();
            std::string presenter = this->ui.getTutorialsService()[index].getPresenter();
            Duration duration = this->ui.getTutorialsService()[index].getDuration();
            int old_likes = this->ui.getTutorialsService()[index].getLikes();
            std::string link = this->ui.getTutorialsService()[index].getLink();
            std::string new_likes_string= this->likesLineEdit->text().toStdString();
            int new_likes;
            this->validator.validateTitle(title);
            this->validator.validateNrLikesString(new_likes_string);
            new_likes = stoi(new_likes_string);
            this->ui.updateTutorialService(title, presenter, duration, old_likes, link, new_likes);
            this->populateList();
        }
    }
    catch (ValidationException& exc)
    {
        auto* error = new QMessageBox();
        error->setIcon(QMessageBox::Critical);
        error->setText(exc.what());
        error->setWindowTitle("Invalid input!");
        error->exec();
    }
    catch (RepoException& re)
    {
        auto* error = new QMessageBox();
        error->setIcon(QMessageBox::Critical);
        error->setText(re.what());
        error->setWindowTitle("Error at updating tutorial!");
        error->exec();
    }
}

int AdminGUI::getSelectedIndex() const
{
    QModelIndexList selectedIndexes = this->tutorialsListWidget->selectionModel()->selectedIndexes();
    if (selectedIndexes.empty())
    {
        this->titleLineEdit->clear();
        this->presenterLineEdit->clear();
        this->durationLineEdit->clear();
        this->likesLineEdit->clear();
        this->linkLineEdit->clear();
        return -1;
    }
    int selectedIndex = selectedIndexes.at(0).row();
    return selectedIndex;
}

AdminGUI::~AdminGUI() = default;

void GUI::showUser()
{
    auto* user = new UserGUI(this, this->ui, this->userService, this->validator);
    user->show();
}

UserGUI::UserGUI(QWidget* parent, Service& serv, UserService &userserv, TutorialValidator& validator1)
        : service{serv}, userService{userserv}, validator{validator1}
{
    this->titleWidget = new QLabel(this);
    this->tutorialsListWidget = new QListWidget{};
    this->watchlistWidget = new QListWidget{};
    this->titleLineEdit = new QLineEdit{};
    this->presenterLineEdit = new QLineEdit{};
    this->durationLineEdit = new QLineEdit{};
    this->likesLineEdit = new QLineEdit{};
    this->linkLineEdit = new QLineEdit{};
    this->presenterFilterLineEdit = new QLineEdit{};
    this->addButton = new QPushButton("Add to the watchlist");
    this->filterButton = new QPushButton("Filter");
    this->openListButton = new QPushButton("Open file");
    this->csvButton = new QRadioButton("CSV");
    this->htmlButton = new QRadioButton("HTML");
    this->repoTypeSelected = false;
    this->filtered = false;
    setParent(parent);
    setWindowFlag(Qt::Window);
    this->initUserGUI();
    this->populateTutorialList();
    this->connectSignalsAndSlots();
}

void UserGUI::initUserGUI()
{
    auto* layout = new QVBoxLayout(this);
    QFont titleFont = this->titleWidget->font();
    this->titleWidget->setText("<p style='text-align:center'><font color=#4D2D52>USER MODE <br> Select the type of file you want for saving your tutorials!</font></p>");
    titleFont.setItalic(true);
    titleFont.setPointSize(12);
    titleFont.setStyleHint(QFont::System);
    titleFont.setWeight(63);
    this->titleWidget->setFont(titleFont);
    layout->addWidget(this->titleWidget);

    auto* radioButtonsLayout = new QGridLayout(this);
    radioButtonsLayout->addWidget(this->csvButton, 0, 0);
    radioButtonsLayout->addWidget(this->htmlButton, 1, 0);
    radioButtonsLayout->addWidget(this->openListButton, 0, 1);
    layout->addLayout(radioButtonsLayout);

    auto* listLayout = new QGridLayout(this);
    listLayout->addWidget(this->tutorialsListWidget, 0, 0);
    listLayout->addWidget(this->watchlistWidget, 0, 1);
    layout->addLayout(listLayout);

    auto * tutorialDetailsLayout = new QFormLayout{};
    tutorialDetailsLayout->addRow("Title", this->titleLineEdit);
    tutorialDetailsLayout->addRow("Presenter", this->presenterLineEdit);
    tutorialDetailsLayout->addRow("Duration", this->durationLineEdit);
    tutorialDetailsLayout->addRow("Likes", this->likesLineEdit);
    tutorialDetailsLayout->addRow("Link", this->linkLineEdit);
    tutorialDetailsLayout->addRow(this->addButton);
    layout->addLayout(tutorialDetailsLayout);


    auto *filterTitle = new QLabel("<p style='text-align:center'><font color=#4D2D52><br>Filter the tutorials by presenter</font></p>");
    QFont filterFont = filterTitle->font();
    filterFont.setPointSize(10);
    filterFont.setStyleHint(QFont::System);
    filterFont.setWeight(63);
    filterTitle->setFont(filterFont);
    layout->addWidget(filterTitle);

    auto *filterDetailsLayout = new QFormLayout{};
    filterDetailsLayout->addRow("Presenter", this->presenterFilterLineEdit);
    filterDetailsLayout->addRow(this->filterButton);
    layout->addLayout(filterDetailsLayout);
}

void UserGUI::populateTutorialList()
{
    this->tutorialsListWidget->clear();
    std::vector<Tutorial> allDogs = this->service.getTutorialsService();
    for (Tutorial& t: allDogs)
        this->tutorialsListWidget->addItem(QString::fromStdString(t.getTitle()));
}

void UserGUI::populateWatchlist()
{
    this->watchlistWidget->clear();
    std::vector<Tutorial> tutorials = this->userService.getAllUserService();
    for (Tutorial& t: tutorials)
        this->watchlistWidget->addItem(QString::fromStdString(t.getTitle()));
}

void UserGUI::connectSignalsAndSlots()
{
    QObject::connect(this->tutorialsListWidget, &QListWidget::itemClicked, [this]()
    {
        std::string title = this->tutorialsListWidget->selectedItems().at(0)->text().toStdString();
        int index = this->service.getByTitle(title);
        Tutorial t = this->service.getTutorialsService()[index];
        this->titleLineEdit->setText(QString::fromStdString(t.getTitle()));
        this->presenterLineEdit->setText(QString::fromStdString(t.getPresenter()));
        this->durationLineEdit->setText(QString::fromStdString(t.getDuration().toStringDuration()));
        this->linkLineEdit->setText(QString::fromStdString(t.getLink()));
        system(("firefox " + t.getLink()).c_str());
    });

    QObject::connect(this->csvButton, &QRadioButton::clicked, [this]()
    {
        this->userService.repositoryType("csv");
        this->repoTypeSelected = true;
    });

    QObject::connect(this->htmlButton, &QRadioButton::clicked, [this]()
    {
        this->userService.repositoryType("html");
        this->repoTypeSelected = true;
    });

    QObject::connect(this->openListButton, &QPushButton::clicked, [this]()
    {
        if (!this->repoTypeSelected) {
            auto* error = new QMessageBox();
            error->setIcon(QMessageBox::Warning);
            error->setText("Please select the type of file you want!");
            error->setWindowTitle("File type warning!");
            error->exec();
        } else {
            std::string link = std::string("start ").append(this->userService.getFileService());
            system(link.c_str());
        }
    });

    QObject::connect(this->addButton, &QPushButton::clicked, this, &UserGUI::addTutorial);
    QObject::connect(this->filterButton, &QPushButton::clicked, this, &UserGUI::filterTutorials);
}

int UserGUI::getSelectedIndex() const
{
    QModelIndexList selectedIndexes = this->tutorialsListWidget->selectionModel()->selectedIndexes();
    if (selectedIndexes.empty())
    {
        this->titleLineEdit->clear();
        this->presenterLineEdit->clear();
        this->durationLineEdit->clear();
        this->likesLineEdit->clear();
        this->linkLineEdit->clear();
        return -1;
    }
    int selectedIndex = selectedIndexes.at(0).row();
    return selectedIndex;
}

void UserGUI::addTutorial()
{
    if (!this->repoTypeSelected) {
        auto *error = new QMessageBox();
        error->setIcon(QMessageBox::Warning);
        error->setText("Please select the type of file you want!");
        error->setWindowTitle("File type warning!");
        error->exec();
    }
    else
    {
        std::string title = this->titleLineEdit->text().toStdString();
        std::string presenter = this->presenterLineEdit->text().toStdString();
        std::string duration_string = this->durationLineEdit->text().toStdString();
        std::string likes_string = this->linkLineEdit->text().toStdString();
        std::string link = this->linkLineEdit->text().toStdString();
        int likes;
        try
        {
            this->validator.validateTitle(title);
            this->validator.validatePresenter(presenter);
            this->validator.validateDurationString(duration_string);
            likes = stoi(likes_string);
            this->validator.validateNrLikes(likes);
            this->validator.validateVideoLink(link);
            Duration duration;
            int minutes = (int(duration_string[0]) - '0') * 10 + (int(duration_string[1]) - '0');
            int seconds = (int(duration_string[3]) - '0') * 10 + (int(duration_string[4]) - '0');
            duration.setMinutes(minutes);
            duration.setSeconds(seconds);
            Tutorial t = Tutorial(title, presenter, duration, likes, link);
            this->userService.addUserService(t);
            if (!this->filtered)
                this->populateTutorialList();
            else
                this->watchlistWidget->addItem(this->watchlistWidget->takeItem(this->getSelectedIndex()));
            this->populateWatchlist();
        }
        catch (ValidationException& exc)
        {
            auto* error = new QMessageBox();
            error->setIcon(QMessageBox::Critical);
            error->setText(exc.what());
            error->setWindowTitle("Invalid input!");
            error->exec();
        }
        catch (RepoException& re)
        {
            auto* error = new QMessageBox();
            error->setIcon(QMessageBox::Critical);
            error->setText(re.what());
            error->setWindowTitle("Error at adding tutorial!");
            error->exec();
        }
    }
}

void UserGUI::filterTutorials()
{
    try
    {
        std::string presenter_filter = this->presenterLineEdit->text().toStdString();

        if (presenter_filter.empty())
        {
            this->filtered = false;
            this->populateWatchlist();
        }
        else
        {
            this->validator.validatePresenter(presenter_filter);
            std::vector<Tutorial> validTutorials;
            std::vector<int> positions;
            this->service.getByPresenter(presenter_filter, positions);

            if (validTutorials.empty())
            {
                std::string error;
                error += std::string("The list of valid tutorials is empty!");
                if(!error.empty())
                    throw UserException(error);
            }
            else
            {
                this->filtered = true;
                this->tutorialsListWidget->clear();
                for (Tutorial& t: validTutorials)
                    this->tutorialsListWidget->addItem(QString::fromStdString(t.getTitle()));
            }
        }
    }
    catch (ValidationException& ve)
    {
        auto *error = new QMessageBox();
        error->setIcon(QMessageBox::Critical);
        error->setText(ve.what());
        error->setWindowTitle("Validation error!");
        error->exec();
    }
    catch (UserException& ue)
    {
        auto *error = new QMessageBox();
        error->setIcon(QMessageBox::Critical);
        error->setText(ue.what());
        error->setWindowTitle("Filter error!");
        error->exec();
    }
}

int TutorialListModel::rowCount(const QModelIndex &parent) const
{
    return this->repository.getTutorialsRepo().size();
}

QVariant TutorialListModel::data(const QModelIndex &index, int role) const {
    int row = index.row();
    Tutorial currentTutorial = this->repository.getTutorialsRepo()[row];
    if (role == Qt::DisplayRole) {
        return QString::fromStdString(currentTutorial.getTitle());
    }
    return QVariant();
}

UserGUI::~UserGUI() = default;

void AdminGUI::filterByPresenter()
{
    std::string presenter_to_filter_by = this->presenterFilteredLineEdit->text().toStdString();
    std::vector<Tutorial> tutorials = this->ui.getTutorialsService();
    QListWidget *filteredTutorials = new QListWidget;
    int found = 0;
    // presenter field is empty
    if (presenter_to_filter_by == "\0")
        for (Tutorial t: tutorials)
        {
            filteredTutorials->addItem(QString::fromStdString(t.getTitle() + "   ||   " + t.getPresenter()));
            found = 1;
        }

    else {
        for (Tutorial t: tutorials) {
            if (t.getPresenter() == presenter_to_filter_by) {
                filteredTutorials->addItem(QString::fromStdString(t.getTitle() + "   ||   " + t.getPresenter()));
                found = 1;
            }
        }
    }
    // no presenter with the name was found
    if (!found)
    {
        auto *error = new QMessageBox();
        error->setIcon(QMessageBox::Warning);
        error->setWindowTitle("No such presenter in the database!");
        error->exec();
    }
    else
        filteredTutorials->show();
}
