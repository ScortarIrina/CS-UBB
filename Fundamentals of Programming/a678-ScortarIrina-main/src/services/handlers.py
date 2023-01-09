from enum import Enum


def add_new_student_handler(student_service, student_id):
    student_service.remove_student_by_id(student_id)


def remove_student_handler(student_service, student_id, student_name, student_group):
    student_service.add_new_student(student_id, student_name, student_group)


def add_new_assignment_handler(assignment_service, assignment_id):
    assignment_service.remove_assignment_from_assignments_by_id(assignment_id)


def remove_assignment_handler(assignment_service, assignment_id, assignment_description, assignment_deadline):
    assignment_service.add_new_assignment(assignment_id, assignment_description, assignment_deadline)


class UndoHandler(Enum):
    ADD_STUDENT = add_new_student_handler
    REMOVE_STUDENT = remove_student_handler
    ADD_ASSIGNMENT = add_new_assignment_handler
    REMOVE_ASSIGNMENT = remove_assignment_handler


class RedoHandler(Enum):
    ADD_STUDENT = remove_student_handler
    REMOVE_STUDENT = add_new_student_handler
    ADD_ASSIGNMENT = remove_assignment_handler
    REMOVE_ASSIGNMENT = add_new_assignment_handler
