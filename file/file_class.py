from abc import ABC, abstractmethod


class File(ABC):
    @abstractmethod
    def load(self):
        pass

    def print(self):
        pass

    def read(self):
        pass

    def save(self, output, data):
        pass
