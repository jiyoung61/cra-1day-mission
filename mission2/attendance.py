from mission2.attendance_manager import AttendanceManager
from mission2.default_grade_policy import DefaultPlayerGradePolicy
from mission2.default_point_policy import DefaultPlayerPointPolicy
from mission2.default_remove_policy import DefaultPlayerRemovePolicy

if __name__ == "__main__":
    """
    prepare dependencies
    """
    app = AttendanceManager(
        point_policy=DefaultPlayerPointPolicy(),
        grade_policy=DefaultPlayerGradePolicy(),
        remove_policy=DefaultPlayerRemovePolicy()
    )
    app.process()
