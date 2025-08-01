import pytest

from mission2.attendance_manager import AttendanceManager
from mission2.default_grade_policy import DefaultPlayerGradePolicy
from mission2.default_point_policy import DefaultPlayerPointPolicy
from mission2.default_remove_policy import DefaultPlayerRemovePolicy
from mission2.player import Player

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