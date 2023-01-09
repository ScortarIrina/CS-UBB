from src.repository.student_repository import StudentRepository


class StudentService:
    def __init__(self):
        self.__student_repository = StudentRepository()

    def generate_students(self):
        self.__student_repository.generate_students()

    def get_list_of_students(self):
        return self.__student_repository.get_list_of_students()

    def get_student_by_id(self, id):
        return self.__student_repository.get_student_by_id(id)

    def id_not_unique(self, id):
        return self.__student_repository.id_not_unique(id)

    def add_new_student(self, id, name, group):
        self.__student_repository.add_new_student(id, name, group)

    def remove_student_by_id(self, student_id):
        self.__student_repository.remove_student_by_id(student_id)

    def update_name(self, student_id, student_name):
        self.__student_repository.update_name(student_id, student_name)

    def update_group(self, student_id, student_group):
        self.__student_repository.update_group(student_id, student_group)
