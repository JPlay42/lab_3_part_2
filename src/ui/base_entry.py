from abc import ABC, abstractmethod

from src.storage import Repository
from src.ui.ui import UI


class BaseEntryUI(UI, ABC):
    def __init__(self, repo: Repository):
        self._repo = repo

    def run(self):
        print('Select an action: ')
        print('1) Create new entry with auto-generated ID')
        print('2) Read entry by ID')
        print('3) Read all entries')
        print('4) Update existing entry')
        print('5) Delete entry')
        try:
            match self._input_options(6):
                case 1:
                    self._create()
                case 2:
                    self._read()
                case 3:
                    self._read_all()
                case 4:
                    self._update()
                case 5:
                    self._delete()
        except IndexError:
            print('No such entry')

    def _create(self):
        self._repo.create(self.get_entry())

    def _read(self):
        print(self._repo.read(self._get_entry_id()))

    def _read_all(self):
        entries = self._repo.read_all()
        for entry_id in entries:
            print(f'{entry_id}: {entries[entry_id]}')

    def _update(self):
        self._repo.update(self._get_entry_id(), self.get_entry())

    def _delete(self):
        self._repo.delete(self._get_entry_id())

    @abstractmethod
    def get_entry(self):
        pass

    @staticmethod
    def _get_entry_id():
        return int(input('ID: '))
