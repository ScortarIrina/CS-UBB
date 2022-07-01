//
// Created by Irina Scortar on 01.07.2022.
//

#include "GUIManager.h"
#include "gui.h"


GUIManager::GUIManager(Controller &controller) {
    std::vector<Programmer> programmers = controller.getAllProgrammers();

    for(const auto &t : programmers)
    {
        auto *user_window = new gui(controller, t);
        controller.attachObserver(user_window);
        user_window->show();
    }

}
