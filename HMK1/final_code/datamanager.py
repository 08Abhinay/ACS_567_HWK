# datamanager.py
from data import Data

class DataManager:
    _instance = None

    def __new__(cls, filename):
        if cls._instance is None:
            cls._instance = super(DataManager, cls).__new__(cls)
            cls._instance.data = Data(filename)
        return cls._instance
