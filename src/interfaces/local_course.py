from abc import abstractmethod

from src.interfaces.course import ICourse


class ILocalCourse(ICourse):
    @property
    @abstractmethod
    def lab(self):
        pass

    @lab.setter
    @abstractmethod
    def lab(self, lab: str):
        pass
