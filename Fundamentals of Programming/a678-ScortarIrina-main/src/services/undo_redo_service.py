from dataclasses import dataclass


@dataclass
class UndoOperation:
    target_objects: list  # will be a service: student, assignment or grade
    handlers: list  # the converse operation
    redo_operation: object
    arguments_of_handlers: list


class UndoManager:
    __undo_operations = []

    @classmethod
    def register_operation5(cls, target_object, handler, redo_operation, *arguments_of_handler):
        cls.__undo_operations.append(UndoOperation(target_object, handler, redo_operation, arguments_of_handler))

    @classmethod
    def register_operation2(cls, undo_operation):
        cls.__undo_operations.append(undo_operation)

    @staticmethod
    def undo():
        if len(UndoManager.__undo_operations) == 0:
            raise ValueError('You cannot undo anymore')
        undo_operation = UndoManager.__undo_operations.pop()
        if undo_operation is not None:
            redo_operation = undo_operation.redo_operation
            redo_operation.undo_operation = undo_operation
            RedoManager.register_operation(redo_operation)
        for i in range(len(undo_operation.target_objects)):
            arguments = undo_operation.arguments_of_handlers[i]
            try:
                iter(arguments)
            except TypeError as te:
                arguments = [*undo_operation.arguments_of_handlers[i]]
            undo_operation.handlers[i](undo_operation.target_objects[i], *arguments)


@dataclass
class RedoOperation:
    target_objects: list  # will be a service: student, assignment or grade
    handlers: list  # the converse operation
    undo_operation: object
    arguments_of_handlers: list


class RedoManager:
    __redo_operations = []

    @classmethod
    def register_operation(cls, target_object, handler, *arguments_of_handler):
        cls.__redo_operations.append(RedoOperation(target_object, handler, arguments_of_handler))

    @classmethod
    def register_operation(cls, redo_operation):
        cls.__redo_operations.append(redo_operation)

    @staticmethod
    def redo():
        if len(RedoManager.__redo_operations) == 0:
            raise ValueError('You cannot redo anymore')
        redo_operation = RedoManager.__redo_operations.pop()
        if redo_operation is not None:
            undo_operation = redo_operation.undo_operation
            undo_operation.redo_operation = redo_operation
            UndoManager.register_operation2(undo_operation)
        for i in range(len(redo_operation.target_objects)):
            argument = redo_operation.arguments_of_handlers[i]
            try:
                iter(argument)
            except TypeError as te:
                argument = [redo_operation.arguments_of_handlers[i]]
            redo_operation.handlers[i](redo_operation.target_objects[i], *argument)
