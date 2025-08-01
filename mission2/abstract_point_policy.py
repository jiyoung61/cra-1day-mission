from abc import ABC, abstractmethod

from mission2.player import Player
from mission2.weekdays import Weekdays


class AbstractPlayerPointPolicy(ABC):
    @abstractmethod
    def get_weekday_point(self, weekday: Weekdays):
        ...

    @abstractmethod
    def get_bonus_point(self, player: Player):
        ...
