from abc import ABC, abstractmethod

class AbstractVacancy(ABC):
    """Вывод у человека"""
    @abstractmethod
    def conclusion_in_humans(self):
        pass

