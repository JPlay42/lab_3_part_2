from abc import abstractmethod, ABC, abstractproperty

from src.interfaces.teacher import ITeacher


class ICourse(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

    @name.setter
    @abstractmethod
    def name(self, name: str):
        pass

    @property
    @abstractmethod
    def teacher(self):
        pass

    @teacher.setter
    @abstractmethod
    def teacher(self, teacher: ITeacher):
        pass

    @abstractmethod
    def add_topic(self, topic: str):
        pass

    @abstractmethod
    def __str__(self):
        pass
