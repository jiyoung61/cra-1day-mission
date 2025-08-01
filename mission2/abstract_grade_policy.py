from abc import ABC, abstractmethod

from mission2.player import Player


class AbstractPlayerGradePolicy(ABC):
    @abstractmethod
    def get_grade(self, points: int):
        ...
