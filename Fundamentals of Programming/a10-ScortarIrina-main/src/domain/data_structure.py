# from datetime import datetime
#
#
# class IterableException(Exception):
#     pass
#
#
# class Iterable:
#
#     def __init__(self):
#         self._data=[]
#         self._index=-1
#
#     def __len__(self):
#         return len(self._data)
#
#     def __getitem__(self, index):
#         return self._data[index]
#
#     def __setitem__(self, index, value):
#         if 0 <= index < len(self._data):
#             self._data[index]=value
#         else:
#             raise IterableException("Index out of range.")
#
#     def __delitem__(self, index):
#         del self._data[index]
#
#     def __iter__(self):
#         self._index=-1
#         return self
#
#     def __next__(self):
#         self._index += 1
#         if self._index>= len(self._data):
#             raise StopIteration
#         return self._data[self._index]
#
#     def append(self,item):
#         self._data.append(item)
#
#     def pop(self,index):
#         self._data.pop(index)
#
#     def get_list(self):
#         return self._data
#
#     def gnome_sort(self,comp_function):
#         index = 0
#         while index < len(self._data):
#             if index == 0:
#                 index = index + 1
#             if comp_function(self._data[index],self._data[index-1]):
#                 self._data[index], self._data[index - 1] = self._data[index - 1], self._data[index]
#                 index = index - 1
#             else:
#                 index=index+1
#         return self._data
#
#     def compare_id(self,x,y):
#         if x.id<y.id:
#             return True
#         else:
#             return False
#
#     def compare_grades(self,x,y):
#         if x.grade_value > y.grade_value:
#             return True
#         else:
#             return False
#
#     def filter(self,filter_function,pass_value):
#         filtered=[]
#         for item in self._data:
#             if filter_function(item,pass_value):
#                 filtered.append(item)
#         return filtered
#
#     def filter_by_a_id(self, item, pass_value):
#         if item.assignment_id == pass_value:
#             return True
#         else:
#             return False
#
#     @staticmethod
#     def filter_past_deadline(list_element):
#         if list_element.deadline < datetime.today():
#             return True
#         else:
#             return False



from datetime import datetime


class InvalidOperationException(Exception):
    pass


class IterableException(Exception):
    pass


class Iterable:
    def __init__(self):
        self._data = []
        self._iteration_index = 0

    def __iter__(self):
        self._iteration_index = 0
        return self

    def __next__(self):
        if self._iteration_index >= len(self._data):
            raise StopIteration
        result = self._data[self._iteration_index]
        self._iteration_index += 1
        return result

    def __len__(self):
        return len(self._data)

    def __setitem__(self, key, value):
        self._data[key] = value

    def __getitem__(self, item):
        return self._data[item]

    def __delitem__(self, key):
        del self._data[key]

    def append(self, value):
        self._data.append(value)

    def pop(self, index):
        self._data.pop(index)

    def get_list(self):
        return self._data

    def gnome_sort(self, comparison_function):
        """
        We parse the list from left to right.
        If the current element is larger or equal to the previous element, then we go to the next element.
        Otherwise, we swap these elements and go one step back.
        We repeat these steps until we get to the nd of the array.
        """
        index = 0
        while index < len(self._data):
            if index == 0:
                index += 1
            if comparison_function(self._data[index], self._data[index-1]):
                self._data[index], self._data[index-1] = self._data[index-1], self._data[index]
                index -= 1
            else:
                index += 1
        return self._data

    def filter(self, filter_function, pass_value):
        filtered = []
        for item in self._data:
            if filter_function(item, pass_value):
                filtered.append(item)
        return filtered

    @staticmethod
    def compare_id(item1, item2):
        if item1.id < item2.id:
            return True
        else:
            return False

    @staticmethod
    def compare_grades(item1, item2):
        if item1.grade_value > item2.grade_value:
            return True
        else:
            return False

    @staticmethod
    def filter_by_assignment_id(item, pass_value):
        if item.assignment_id == pass_value:
            return True
        else:
            return False

    @staticmethod
    def filter_past_deadline(list_element):
        if list_element.deadline < datetime.today():
            return True
        else:
            return False
