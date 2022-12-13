from src.interfaces.course import ICourse
from src.interfaces.teacher import ITeacher


class Course(ICourse):
    def __init__(self, name: str, teacher: ITeacher):
        self.name = name
        self.teacher = teacher
        self.__topics = list()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        if not isinstance(name, str):
            raise TypeError(f'name cannot have {type(name)} type')
        if name == '':
            raise ValueError('name cannot be empty')
        self.__name = name

    @property
    def teacher(self):
        return self.__teacher

    @teacher.setter
    def teacher(self, teacher: ITeacher):
        if not isinstance(teacher, ITeacher):
            raise TypeError(f'teacher cannot have {type(teacher)} type')
        self.__teacher = teacher

    @property
    def topics(self):
        return self.__topics

    def add_topic(self, topic: str):
        if not isinstance(topic, str):
            raise TypeError(f'topic cannot have {type(topic)} type')
        if topic == '':
            raise ValueError('topic cannot be empty')
        self.__topics.append(topic)

    def __str__(self):
        return f'Course: Name={self.__name}; Teacher={self.__teacher}; Topics={self.__topics}'
