from src.services.services import Services


class TestFunctions:
    def __init__(self):
        self.test_add_new_student__valid_student__successful_addition()
        self.test_id_not_unique__id_unique__false()
        self.test_id_not_unique__id_not_unique__true()

    def test_add_new_student__valid_student__successful_addition(self):
        test_services = Services()
        test_services.add_new_student('1', 'Maria', '234')
        assert len(test_services.get_list_of_students()) == 1

    def test_id_not_unique__id_unique__false(self):
        test_services = Services()
        assert test_services.id_not_unique(201) == False

    def test_id_not_unique__id_not_unique__true(self):
        test_services = Services()
        test_services.add_new_student('1', 'Maria', '234')
        assert test_services.id_not_unique('1')
