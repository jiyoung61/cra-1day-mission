from mission2.abstract_point_policy import AbstractPlayerPointPolicy
from mission2.player import Player
from mission2.weekdays import Weekdays


class DefaultPlayerPointPolicy(AbstractPlayerPointPolicy):
    BONUS_POINT_WEEKENDS = 10
    BONUS_POINT_WEDNESDAY = 10

    def get_weekday_point(self, weekday: Weekdays) -> int:
        if weekday == Weekdays.WEDNESDAY:
            return 3
        elif weekday == Weekdays.SATURDAY or weekday == Weekdays.SUNDAY:
            return 2
        else:
            return 1

    def get_bonus_point(self, player: Player):
        bonus_points = 0
        if player.attendance_week[Weekdays.WEDNESDAY] > 9:
            bonus_points += DefaultPlayerPointPolicy.BONUS_POINT_WEDNESDAY
        if player.attendance_week[Weekdays.SATURDAY] + player.attendance_week[Weekdays.SUNDAY] > 9:
            bonus_points += DefaultPlayerPointPolicy.BONUS_POINT_WEEKENDS
        return bonus_points
