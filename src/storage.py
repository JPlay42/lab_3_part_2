class Repository:  # now it doesn't store any data
    def __init__(self):
        self.__entities = dict()
        self.__id = 0

    def create(self, entry):
        self.__id += 1
        self.__entities[self.__id] = entry
        return self.__id

    def read(self, entry_id: int):
        if entry_id not in self.__entities.keys():
            raise IndexError()

        return self.__entities[entry_id]

    def read_all(self):
        return self.__entities

    def update(self, entry_id: int, entry):
        if entry_id not in self.__entities.keys():
            raise IndexError()

        self.__entities[entry_id] = entry

    def delete(self, entry_id: int):
        del self.__entities[entry_id]


class Storage:
    def __init__(self):
        self.__teachers = Repository()
        self.__courses = Repository()

    @property
    def teachers(self):
        return self.__teachers

    @property
    def courses(self):
        return self.__courses
