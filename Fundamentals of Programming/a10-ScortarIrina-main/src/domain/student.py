class Student:
    def __init__(self, __id, _name, _group):
        if type(__id) is str:
            __id = int(__id)
        if type(_group) is str:
            _group = int(_group)
        self.__id = __id
        self._name = _name
        self._group = _group

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def group(self):
        return self._group

    @group.setter
    def group(self, value):
        self._group = value

    def __str__(self):
        return 'ID: ' + str(self.__id) + '     NAME: ' + str(self._name) + '     GROUP: ' + str(self._group)
