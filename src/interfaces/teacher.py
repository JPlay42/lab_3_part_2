from abc import ABC, abstractmethod


class ITeacher(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

    @name.setter
    @abstractmethod
    def name(self, name: str):
        pass

    @abstractmethod
    def __str__(self):
        pass
