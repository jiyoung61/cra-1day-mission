from mission2.abstract_grade_policy import AbstractPlayerGradePolicy
from mission2.abstract_point_policy import AbstractPlayerPointPolicy
from mission2.abstract_remove_policy import AbstractPlayerRemovePolicy
from mission2.player import Player
from mission2.weekdays import Weekdays

"""
system constraints
"""
MAX_INPUT_LINE = 500


class AttendanceManager:
    def __init__(self,
                 point_policy: AbstractPlayerPointPolicy,
                 grade_policy: AbstractPlayerGradePolicy,
                 remove_policy: AbstractPlayerRemovePolicy):
        self.player_list: list[Player] = []
        self.point_policy = point_policy
        self.grade_policy = grade_policy
        self.remove_policy = remove_policy

    def add_player(self, name):
        if name not in [player.name for player in self.player_list]:
            self.player_list.append(Player(name))

    def get_player(self, name):
        for player in self.player_list:
            if player.name == name:
                return player
        raise ValueError(f"Unknown Player. name={name}")

    def update_attendance_count(self, name, weekday: Weekdays):
        player = self.get_player(name)
        player.attend(weekday)

    def calculate_basic_point(self, name, weekday):
        player = self.get_player(name)
        player.points += self.point_policy.get_weekday_point(weekday)

    def calculate_bonus_point(self):
        for player in self.player_list:
            player.points += self.point_policy.get_bonus_point(player)

    def update_player_grade(self):
        for player in self.player_list:
            player.grade = self.grade_policy.get_grade(player.points)

    def print_player_info(self):
        for player in self.player_list:
            print(f"NAME : {player.name}, POINT : {player.points}, GRADE : ", end="")
            if player.grade == 1:
                print("GOLD")
            elif player.grade == 2:
                print("SILVER")
            else:
                print("NORMAL")

    def print_removed_player(self):
        print("\nRemoved player")
        print("==============")
        for player in self.player_list:
            if self.remove_policy.valid_candidate(player):
                print(player.name)

    def input_file(self):
        try:
            with open("attendance_weekday_500.txt", encoding='utf-8') as f:
                for _ in range(MAX_INPUT_LINE):
                    line = f.readline()
                    if not line:
                        break
                    parts = line.strip().split()
                    if len(parts) == 2:
                        name, weekday = parts[0], Weekdays[parts[1].upper()]
                        self.add_player(name)
                        self.update_attendance_count(name, weekday)
                        self.calculate_basic_point(name, weekday)
                    else:
                        print(f"parse error.line={line}")
                        continue
        except FileNotFoundError:
            print("파일을 찾을 수 없습니다.")

    def process(self):
        self.input_file()

        self.calculate_bonus_point()
        self.update_player_grade()

        self.print_player_info()
        self.print_removed_player()
