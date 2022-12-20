from src.course_factory import CourseFactory
from src.interfaces.teacher import ITeacher
from src.storage import Storage
from src.ui.base_entry import BaseEntryUI
from src.ui.teachers import TeachersUI


class CoursesUI(BaseEntryUI):
    def __init__(self, storage: Storage, teachers_ui: TeachersUI):
        self.__storage = storage
        super().__init__(storage.courses)
        self.__teachers_ui = teachers_ui

    def get_entry(self):
        print('1) Local course')
        print('2) Offsite course')
        is_local = self._input_options(2) == 1
        get_course = self.__get_local_course if is_local else self.__get_offsite_course
        course = get_course()
        print('Print topics or empty line to exit: ')
        while True:
            topic = input()
            if topic == '':
                break
            course.topics.append(topic)
        return course

    def __get_local_course(self):
        return CourseFactory().create_local_course(
            input('Enter lab: '),
            input('Enter name: '),
            self.__get_teacher()
        )

    def __get_offsite_course(self):
        return CourseFactory().create_offsite_course(
            input('Enter town: '),
            input('Enter name: '),
            self.__get_teacher()
        )

    def __get_teacher(self) -> ITeacher:
        print('Teachers:')
        self.__teachers_ui._read_all()
        return self.__storage.teachers.read(self._get_entry_id())
