from mission2.weekdays import Weekdays


class Player:
    def __init__(self, name):
        self.name = name
        self.attendance_week = [0, 0, 0, 0, 0, 0, 0]
        self.points = 0
        self.grade = 0

    @property
    def attendance_wed(self):
        return self.attendance_week[Weekdays.WEDNESDAY]

    @property
    def attendance_weekends(self):
        return self.attendance_week[Weekdays.SATURDAY] + self.attendance_week[Weekdays.SUNDAY]

    def attend(self, weekday: Weekdays):
        self.attendance_week[weekday] += 1