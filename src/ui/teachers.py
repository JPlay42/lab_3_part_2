from src.course_factory import CourseFactory
from src.storage import Storage
from src.ui.base_entry import BaseEntryUI


class TeachersUI(BaseEntryUI):
    def __init__(self, storage: Storage):
        super().__init__(storage.teachers)

    def get_entry(self):
        return CourseFactory().create_teacher(
            input('Teacher\'s name: ')
        )
