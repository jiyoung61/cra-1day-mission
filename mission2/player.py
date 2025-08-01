from dataclasses import dataclass

class Player:
    def __init__(self, name):
        self.name = name
        self.attendance_week = [0,0,0,0,0,0,0]
        self.attendance_wed = 0
        self.attendance_weekends = 0
        self.points = 0
        self.grade = 0

