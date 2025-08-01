from mission2.player import Player

"""
system constraints
"""
MAX_INPUT_LINE = 500

player_list: list[Player] = []


def add_new_player(name):
    if name not in [player.name for player in player_list]:
        player_list.append(Player(name))


def get_player_id(name):
    for player_id, player in enumerate(player_list):
        if player.name == name:
            return player_id
    raise ValueError(f"Unknown Player. name={name}")


def get_player(name):
    for player in player_list:
        if player.name == name:
            return player
    raise ValueError(f"Unknown Player. name={name}")


def get_weekday_index(weekday: str) -> int:
    if weekday == "monday":
        return 0
    elif weekday == "tuesday":
        return 1
    elif weekday == "wednesday":
        return 2
    elif weekday == "thursday":
        return 3
    elif weekday == "friday":
        return 4
    elif weekday == "saturday":
        return 5
    elif weekday == "sunday":
        return 6

    raise ValueError(f"attended_weekday={weekday}")


def update_attendance_count(name, weekday):
    player = get_player(name)
    weekday_index = get_weekday_index(weekday)
    player.attendance_week[weekday_index] += 1

    if weekday == "wednesday":
        player.attendance_wed += 1
    elif weekday == "saturday" or weekday == "sunday":
        player.attendance_weekends += 1


def get_point(weekday: str) -> int:
    if weekday == "wednesday":
        return 3
    elif weekday == "saturday" or weekday == "sunday":
        return 2
    else:
        return 1


def calculate_basic_point(name, weekday):
    player = get_player(name)
    player.points += get_point(weekday)


def calculate_bonus_point():
    for player in player_list:
        if player.attendance_week[2] > 9:
            player.points += 10
        if player.attendance_week[5] + player.attendance_week[6] > 9:
            player.points += 10


def update_player_grade():
    for player in player_list:
        if player.points >= 50:
            player.grade = 1
        elif player.points >= 30:
            player.grade = 2
        else:
            player.grade = 0


def print_player_info():
    for player in player_list:
        print(f"NAME : {player.name}, POINT : {player.points}, GRADE : ", end="")
        if player.grade == 1:
            print("GOLD")
        elif player.grade == 2:
            print("SILVER")
        else:
            print("NORMAL")


def print_removed_player():
    print("\nRemoved player")
    print("==============")
    for player in player_list:
        if player.grade not in (1, 2) and player.attendance_wed == 0 and player.attendance_weekends == 0:
            print(player.name)


def input_file():
    try:
        with open("attendance_weekday_500.txt", encoding='utf-8') as f:
            for _ in range(MAX_INPUT_LINE):
                line = f.readline()
                if not line:
                    break
                parts = line.strip().split()
                if len(parts) == 2:
                    name, weekday = parts[0], parts[1]
                    add_new_player(name)
                    update_attendance_count(name, weekday)
                    calculate_basic_point(name, weekday)
                else:
                    print(f"parse error.line={line}")
                    continue

        calculate_bonus_point()
        update_player_grade()

        print_player_info()
        print_removed_player()

    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")


if __name__ == "__main__":
    input_file()
