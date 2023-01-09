class DataStructure:
    def __init__(self):
        self.__data = []
        self.__iteration_list = None
        

    def __setitem__(self, key, value):
        self.__data[key] = value