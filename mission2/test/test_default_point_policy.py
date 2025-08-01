import pytest

from mission2.default_point_policy import DefaultPlayerPointPolicy
from mission2.player import Player
from mission2.weekdays import Weekdays

WEEKDAY_POINT_DEFAULT = 1
WEEKDAY_POINT_WEDNESDAY = 3
WEEKDAY_POINT_WEEKENDS = 2

TEST_PLAYER = "TEST"


@pytest.fixture
def policy():
    return DefaultPlayerPointPolicy()


@pytest.mark.parametrize("weekday,point", [
    (Weekdays.MONDAY, WEEKDAY_POINT_DEFAULT),
    (Weekdays.WEDNESDAY, WEEKDAY_POINT_WEDNESDAY),
    (Weekdays.SATURDAY, WEEKDAY_POINT_WEEKENDS),
    (Weekdays.SUNDAY, WEEKDAY_POINT_WEEKENDS)
])
def test_weekday_point(policy, weekday, point):
    assert policy.get_weekday_point(weekday) == point


def test_bonus_point_wednesday(policy):
    player = Player(TEST_PLAYER)

    assert policy.get_bonus_point(player) == 0

    for _ in range(9):
        player.attend(Weekdays.WEDNESDAY)

    assert policy.get_bonus_point(player) == 0

    player.attend(Weekdays.WEDNESDAY)

    assert policy.get_bonus_point(player) == DefaultPlayerPointPolicy.BONUS_POINT_WEDNESDAY


def test_bonus_point_weekends(policy):
    player = Player(TEST_PLAYER)

    assert policy.get_bonus_point(player) == 0

    for _ in range(4):
        player.attend(Weekdays.SATURDAY)

    assert policy.get_bonus_point(player) == 0

    for _ in range(4):
        player.attend(Weekdays.SUNDAY)

    assert policy.get_bonus_point(player) == 0

    player.attend(Weekdays.SATURDAY)
    player.attend(Weekdays.SUNDAY)

    assert policy.get_bonus_point(player) == DefaultPlayerPointPolicy.BONUS_POINT_WEEKENDS
