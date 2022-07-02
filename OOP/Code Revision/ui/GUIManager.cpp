//
// Created by Irina Scortar on 02.07.2022.
//

#include "GUIManager.h"
#include "GUI.h"

GUIManager::GUIManager(Controller &controller) {
    std::vector<Member> members = controller.getAllMembers();

    for(const auto &m : members)
    {
        auto *user_window = new GUI(controller, m);
        controller.attachObserver(user_window);
        user_window->show();
    }
}
