from abc import ABC, abstractmethod


class Tab(ABC):

    NAME: str

    @abstractmethod
    def write(self):
        pass
