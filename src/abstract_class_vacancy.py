from abc import ABC, abstractmethod

class AbstractVacancy(ABC):
    """Вывод у человека"""
    @abstractmethod
    def attribute(self, **kwargs):
        pass

    @abstractmethod
    def site_connecting(self, **kwargs):
        pass

    @abstractmethod
    def to_json(self, **list_job):
        pass



