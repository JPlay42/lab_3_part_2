from abc import abstractmethod

from src.interfaces.course import ICourse


class IOffsiteCourse(ICourse):
    @property
    @abstractmethod
    def town(self):
        pass

    @town.setter
    @abstractmethod
    def town(self, town: str):
        pass
