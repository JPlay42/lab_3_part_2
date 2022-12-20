from src.storage import Storage
from src.ui.root import RootUI

if __name__ == '__main__':
    storage = Storage()
    RootUI(storage).execute()
