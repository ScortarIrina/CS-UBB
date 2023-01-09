class UndoRedoExceptions(Exception):
    pass


class UndoRedoService:
    def __init__(self):
        self._history = []
        self._index = -1
        self._record_flag = True

    def undo(self):
        self._record_flag = False
        if self._index > -1:
            self._history[self._index].undo()
            self._index -= 1
        else:
            raise UndoRedoExceptions("Can't perform anymore undo operations.")
        self._record_flag = True

    def redo(self):
        self._record_flag = False
        if self._index + 1 < len(self._history):
            self._history[self._index + 1].redo()
            self._index = self._index + 1
        else:
            raise UndoRedoExceptions("Can't perform anymore redo operations.")
        self._record_flag = True

    def add(self, operation):
        if self._record_flag is True:
            self._history.append(operation)
            self._index = len(self._history) - 1

    def __getitem__(self, item):
        return self._history[item]

    def __len__(self):
        return len(self._history)


class Operation:
    def __init__(self, undo_call, redo_call):
        self._undo_call = undo_call
        self._redo_call = redo_call

    def undo(self):
        self._undo_call.call()

    def redo(self):
        self._redo_call.call()


class CascadedOperation:
    def __init__(self):
        self._operations = []
        self._add_flag = True

    def add(self, operation):
        if self._add_flag is True:
            self._operations.append(operation)

    def undo(self):
        self._add_flag = False
        for operation in self._operations:
            operation.undo()
        self._add_flag = True

    def redo(self):
        self._add_flag = False
        for operation in self._operations:
            operation.redo()
        self._add_flag = True

    def __str__(self):
        return str(self._operations)

    def __len__(self):
        return len(self._operations)


class Call:

    def __init__(self, function_name, *function_params):
        self._function_name = function_name
        self._function_params = function_params

    def call(self):
        self._function_name(*self._function_params)
