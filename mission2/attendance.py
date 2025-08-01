from mission2.attendance_manager import AttendanceManager
from mission2.default_remove_policy import DefaultPlayerRemovePolicy

if __name__ == "__main__":
    """
    prepare dependencies
    """
    app = AttendanceManager(
        remove_policy=DefaultPlayerRemovePolicy()
    )
    app.process()
