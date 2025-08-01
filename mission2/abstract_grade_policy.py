from abc import ABC, abstractmethod


class AbstractPlayerGradePolicy(ABC):
    @abstractmethod
    def get_grade(self, points: int):
        ...
