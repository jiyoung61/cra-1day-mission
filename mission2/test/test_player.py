import pytest

from mission2.player import Player
from mission2.weekdays import Weekdays

TEST_NAME = "test"
DEFAULT_POINTS = 0
DEFAULT_GRADE = 0

@pytest.fixture
def player():
    return Player(TEST_NAME)

def test_player_init(player):
    assert player.name == TEST_NAME
    assert len(player.attendance_week) == 7  # weekdays
    assert player.attendance_week == [0, 0, 0, 0, 0, 0, 0]
    assert player.points == DEFAULT_POINTS
    assert player.grade == DEFAULT_GRADE

def test_attend_wednesday(player):
    assert player.attendance_wed == 0

    player.attend(Weekdays.WEDNESDAY)

    assert player.attendance_wed == 1

def test_attend_weekends(player):
    assert player.attendance_weekends == 0

    player.attend(Weekdays.SATURDAY)

    assert player.attendance_weekends == 1

    player.attend(Weekdays.SUNDAY)

    assert player.attendance_weekends == 2
