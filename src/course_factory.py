from src.interfaces.course_factory import ICourseFactory
from src.interfaces.teacher import ITeacher
from src.local_course import LocalCourse
from src.offsite_course import OffsiteCourse
from src.teacher import Teacher


class CourseFactory(ICourseFactory):
    def create_teacher(self, name: str):
        return Teacher(name)

    def create_local_course(self, lab: str, name: str, teacher: ITeacher):
        return LocalCourse(lab, name, teacher)

    def create_offsite_course(self, town: str, name: str, teacher: ITeacher):
        return OffsiteCourse(town, name, teacher)
