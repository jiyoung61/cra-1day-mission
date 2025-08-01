import pytest

from mission2.default_grade_policy import DefaultPlayerGradePolicy

GRADE_GOLD = 1
GRADE_SILVER = 2
GRADE_DEFAULT = 0

@pytest.fixture
def policy():
    return DefaultPlayerGradePolicy()

@pytest.mark.parametrize("point,grade",[
    (0, GRADE_DEFAULT),
    (10, GRADE_DEFAULT),
    (30, GRADE_SILVER),
    (40, GRADE_SILVER),
    (50, GRADE_GOLD),
    (60, GRADE_GOLD)
])
def test_default_policy(policy, point, grade):
    assert policy.get_grade(point) == grade