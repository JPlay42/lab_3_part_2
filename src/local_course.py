from src.course import Course
from src.interfaces.local_course import ILocalCourse
from src.interfaces.teacher import ITeacher


class LocalCourse(Course, ILocalCourse):
    def __init__(self, lab: str, name: str, teacher: ITeacher):
        super().__init__(name, teacher)
        self.lab = lab

    @property
    def lab(self):
        return self.__lab

    @lab.setter
    def lab(self, lab: str):
        if not isinstance(lab, str):
            raise TypeError(f'lab cannot be {type(lab)} type')
        if lab == '':
            raise ValueError('lab cannot be empty')
        self.__lab = lab

    def __str__(self):
        return f'LocalCourse: Name:{self.__name}; Lab: {self.__lab}; ' \
               f'Teacher={self.__teacher}; Topics={self.__topics}'

