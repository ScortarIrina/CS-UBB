import datetime


class Assignment:
    def __init__(self, __id, _description, _deadline):
        if type(_deadline) == str:
            _deadline = datetime.datetime.strptime(_deadline, "%Y-%m-%d")
        if type(__id) == str:
            __id = int(__id)

        self.__id = __id
        self._description = _description
        self._deadline = _deadline

    @property
    def id(self):
        return self.__id

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def deadline(self):
        return self._deadline

    @deadline.setter
    def deadline(self, value):
        self._deadline = value

    def __str__(self):
        return 'ID: ' + str(self.__id) + '     DESCRIPTION: ' + str(self._description) + '     DEADLINE: ' + \
               str(self._deadline)
