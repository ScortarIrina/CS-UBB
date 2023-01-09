import copy

from src.services.undo_redo_service import Operation, Call


class StudentService:
    def __init__(self, repository, undo_redo_service):
        self._student_repository = repository
        self._undo_redo = undo_redo_service

    def generate_students(self):
        for student in range(10):
            self._student_repository.generate_student()

    def get_list_of_students(self):
        return self._student_repository.get_list_of_students()

    def get_student_by_id(self, id):
        return copy.deepcopy(self._student_repository.get_student_by_id(id))

    def id_not_unique(self, id):
        return self._student_repository.id_not_unique(id)

    def add_new_student(self, id, name, group):
        if self._student_repository.id_not_unique(id) is False:
            self._student_repository.add_new_student(id, name, group)
            self._undo_redo.add(Operation(Call(self.remove_student_by_id, id), Call(self.add_new_student, id, name, group)))
        else:
            raise ValueError("Student id must be unique")

    def remove_student_by_id(self, student_id):
        student = self.get_student_by_id(student_id)
        self._student_repository.remove_student_by_id(student_id)
        self._undo_redo.add(Operation(Call(self.add_new_student, student.id, student.name, student.group), Call(self.remove_student_by_id, student_id)))

    def update_name(self, student_id, student_name):
        student = self.get_student_by_id(student_id)
        self._undo_redo.add(Operation(Call(self.update_name, student.id, student.name), Call(self.update_name, student.id, student_name)))
        self._student_repository.update_name(student_id, student_name)

    def update_group(self, student_id, student_group):
        student = self.get_student_by_id(student_id)
        self._undo_redo.add(Operation(Call(self.update_group, student.id, student.group), Call(self.update_group, student.id, student_group)))
        self._student_repository.update_group(student_id, student_group)
