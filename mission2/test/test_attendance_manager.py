import pytest

from mission2.attendance_manager import AttendanceManager
from mission2.default_grade_policy import DefaultPlayerGradePolicy
from mission2.default_point_policy import DefaultPlayerPointPolicy
from mission2.default_remove_policy import DefaultPlayerRemovePolicy
from mission2.weekdays import Weekdays

TEST_PLAYER = "TEST"


@pytest.fixture
def manager():
    return AttendanceManager(
        point_policy=DefaultPlayerPointPolicy(),
        grade_policy=DefaultPlayerGradePolicy(),
        remove_policy=DefaultPlayerRemovePolicy()
    )


def test_init(manager):
    assert True


def test_add_player(manager):
    assert len(manager.player_list) == 0

    manager.add_player(TEST_PLAYER)

    assert len(manager.player_list) == 1
    assert manager.player_list[0].name == TEST_PLAYER


def test_get_invalid_player(manager):
    with pytest.raises(ValueError):
        manager.get_player(TEST_PLAYER)


def test_get_valid_player(manager):
    manager.add_player(TEST_PLAYER)
    new_player = manager.get_player(TEST_PLAYER)
    assert new_player.name == TEST_PLAYER


def test_update_attendance_count(manager):
    manager.add_player(TEST_PLAYER)
    assert manager.get_player(TEST_PLAYER).attendance_wed == 0

    manager.update_attendance_count(TEST_PLAYER, Weekdays.WEDNESDAY)
    assert manager.get_player(TEST_PLAYER).attendance_wed == 1


def test_calculate_basic_point(manager):
    manager.add_player(TEST_PLAYER)
    assert manager.get_player(TEST_PLAYER).points == 0

    manager.calculate_basic_point(TEST_PLAYER, Weekdays.MONDAY)
    assert manager.get_player(TEST_PLAYER).points == 1


def test_calculate_bonus_point(manager):
    manager.add_player(TEST_PLAYER)
    assert manager.get_player(TEST_PLAYER).points == 0

    for _ in range(10):
        manager.get_player(TEST_PLAYER).attend(Weekdays.SUNDAY)
    manager.calculate_bonus_point()
    assert manager.get_player(TEST_PLAYER).points == 10


def test_update_player_grade(manager):
    manager.add_player(TEST_PLAYER)
    assert manager.get_player(TEST_PLAYER).points == 0

    for _ in range(10):
        manager.get_player(TEST_PLAYER).attend(Weekdays.SUNDAY)
    manager.update_player_grade()

    assert manager.get_player(TEST_PLAYER).grade == 0
