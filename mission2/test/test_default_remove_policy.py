import pytest

from mission2.default_remove_policy import DefaultPlayerRemovePolicy
from mission2.player import Player
from mission2.weekdays import Weekdays

TEST_PLAYER = "TEST"

@pytest.fixture
def policy():
    return DefaultPlayerRemovePolicy()

def test_valid_candidate(policy):
    player = Player(TEST_PLAYER)
    assert policy.valid_candidate(player)

def test_invalid_candidate_wednesday(policy):
    player = Player(TEST_PLAYER)
    player.attend(Weekdays.WEDNESDAY)
    assert not policy.valid_candidate(player)

def test_invalid_candidate_weekends1(policy):
    player = Player(TEST_PLAYER)
    player.attend(Weekdays.SATURDAY)
    assert not policy.valid_candidate(player)

def test_invalid_candidate_weekends2(policy):
    player = Player(TEST_PLAYER)
    player.attend(Weekdays.SUNDAY)
    assert not policy.valid_candidate(player)