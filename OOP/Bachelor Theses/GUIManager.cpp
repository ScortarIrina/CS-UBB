//
// Created by Irina Scortar on 01.07.2022.
//

#include "GUIManager.h"
#include "GUI.h"


GUIManager::GUIManager(Controller &controller) {
    std::vector<Teacher> teachers = controller.getAllTeachers();

    for(const auto &teacher : teachers)
    {
        auto *user_window = new GUI(controller, teacher);
        controller.attachObserver(user_window);
        user_window->show();
    }
}