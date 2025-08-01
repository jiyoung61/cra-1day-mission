from mission2.abstract_grade_policy import AbstractPlayerGradePolicy


class DefaultPlayerGradePolicy(AbstractPlayerGradePolicy):
    def get_grade(self, points: int) -> int:
        if points >= 50:
            return 1
        elif points >= 30:
            return 2
        else:
            return 0