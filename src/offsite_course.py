from src.course import Course
from src.interfaces.offsite_course import IOffsiteCourse
from src.interfaces.teacher import ITeacher


class OffsiteCourse(Course, IOffsiteCourse):

    def __init__(self, town: str, name: str, teacher: ITeacher):
        super().__init__(name, teacher)
        self.town = town

    @property
    def town(self):
        return self.__town

    @town.setter
    def town(self, town: str):
        if not isinstance(town, str):
            raise TypeError(f'lab cannot be {type(town)} type')
        if town == '':
            raise ValueError('lab cannot be empty')
        self.__town = town

    def __str__(self):
        return f'OffsiteCourse: Name:{self.__name}; Town: {self.__town}; ' \
               f'Teacher={self.__teacher}; Topics={self.__topics}'

