from mission2.abstract_remove_policy import AbstractPlayerRemovePolicy
from mission2.player import Player


class DefaultPlayerRemovePolicy(AbstractPlayerRemovePolicy):
    def valid_candidate(self, player: Player):
        if player.grade not in (1, 2) and player.attendance_wed == 0 and player.attendance_weekends == 0:
            return True
        return False
