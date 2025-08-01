"""
system constraints
"""
MAX_INPUT_LINE = 500

"""
global variables
"""
# player_list = { "name": id, ... }
player_list = {}
id_cnt = 0

# attendance_count[player_id][weekday_index]
attendance_count = [[0] * 100 for _ in range(100)]
points = [0] * 100
grade = [0] * 100
player_names = [''] * 100
attendance_wed = [0] * 100
attendance_weekends = [0] * 100


def add_new_player(name):
    global id_cnt
    if name not in player_list:
        id_cnt += 1
        player_list[name] = id_cnt
        player_names[id_cnt] = name


def get_player_id(name):
    return player_list[name]


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
    player_id = get_player_id(name)
    weekday_index = get_weekday_index(weekday)
    attendance_count[player_id][weekday_index] += 1

    if weekday == "wednesday":
        attendance_wed[player_id] += 1
    elif weekday == "saturday" or weekday == "sunday":
        attendance_weekends[player_id] += 1


def get_point(weekday: str) -> int:
    if weekday == "wednesday":
        return 3
    elif weekday == "saturday" or weekday == "sunday":
        return 2
    else:
        return 1


def calculate_basic_point(name, weekday):
    player_id = get_player_id(name)
    points[player_id] += get_point(weekday)


def calculate_bonus_point():
    for i in range(1, id_cnt + 1):
        if attendance_count[i][2] > 9:
            points[i] += 10
        if attendance_count[i][5] + attendance_count[i][6] > 9:
            points[i] += 10


def update_player_grade():
    for i in range(1, id_cnt + 1):
        if points[i] >= 50:
            grade[i] = 1
        elif points[i] >= 30:
            grade[i] = 2
        else:
            grade[i] = 0


def print_player_info():
    for player_id in range(1, id_cnt + 1):
        print(f"NAME : {player_names[player_id]}, POINT : {points[player_id]}, GRADE : ", end="")
        if grade[player_id] == 1:
            print("GOLD")
        elif grade[player_id] == 2:
            print("SILVER")
        else:
            print("NORMAL")


def print_removed_player():
    print("\nRemoved player")
    print("==============")
    for i in range(1, id_cnt + 1):
        if grade[i] not in (1, 2) and attendance_wed[i] == 0 and attendance_weekends[i] == 0:
            print(player_names[i])


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
