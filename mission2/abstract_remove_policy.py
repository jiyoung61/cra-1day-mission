from abc import ABC, abstractmethod

from mission2.player import Player


class AbstractPlayerRemovePolicy(ABC):
    @abstractmethod
    def valid_candidate(self, player: Player):
        ...
