from src.interfaces.teacher import ITeacher


class Teacher(ITeacher):
    def __init__(self, name: str):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        if not isinstance(name, str):
            raise TypeError(f'name cannot be {type(name)} type')
        if name == '':
            raise ValueError(f'name cannot be empty')
        self.__name = name

    def __str__(self):
        return f'Teacher: Name={self.__name}'
