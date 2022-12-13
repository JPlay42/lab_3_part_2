from abc import ABC, abstractmethod

from src.interfaces.teacher import ITeacher


class ICourseFactory(ABC):
    @abstractmethod
    def create_teacher(self, name: str):
        pass

    @abstractmethod
    def create_local_course(self, name: str, teacher: ITeacher, lab: str):
        pass

    @abstractmethod
    def create_offsite_course(self, name: str, teacher: ITeacher, town: str):
        pass
