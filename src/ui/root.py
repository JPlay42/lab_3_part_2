from src.storage import Storage
from src.ui.courses import CoursesUI
from src.ui.teachers import TeachersUI
from src.ui.ui import UI


class RootUI(UI):
    def __init__(self, storage: Storage):
        self.__storage = storage

    def run(self):
        print('Which entities should you work with?')
        print('1) Courses')
        print('2) Teachers')

        teachers_ui = TeachersUI(self.__storage)
        courses_ui = CoursesUI(self.__storage, teachers_ui)

        match self._input_options(2):
            case 1:
                courses_ui.run()
            case 2:
                teachers_ui.run()
