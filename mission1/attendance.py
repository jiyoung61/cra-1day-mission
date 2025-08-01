player_ids = {}
id_cnt = 0

# dat[사용자ID][요일]
attendance_count = [[0] * 100 for _ in range(100)]
points = [0] * 100
grade = [0] * 100
player_names = [''] * 100
attendance_wed = [0] * 100
attendance_weekends = [0] * 100


def calculate_basic_point(player_name, attended_weekday):
    player_id = player_ids[player_name]

    add_point = 0
    weekday_index = 0

    if attended_weekday == "monday":
        weekday_index = 0
        add_point += 1
    elif attended_weekday == "tuesday":
        weekday_index = 1
        add_point += 1
    elif attended_weekday == "wednesday":
        weekday_index = 2
        add_point += 3
        attendance_wed[player_id] += 1
    elif attended_weekday == "thursday":
        weekday_index = 3
        add_point += 1
    elif attended_weekday == "friday":
        weekday_index = 4
        add_point += 1
    elif attended_weekday == "saturday":
        weekday_index = 5
        add_point += 2
        attendance_weekends[player_id] += 1
    elif attended_weekday == "sunday":
        weekday_index = 6
        add_point += 2
        attendance_weekends[player_id] += 1

    attendance_count[player_id][weekday_index] += 1
    points[player_id] += add_point


def add_new_player(player_name):
    global id_cnt
    if player_name not in player_ids:
        id_cnt += 1
        player_ids[player_name] = id_cnt
        player_names[id_cnt] = player_name


def input_file():
    try:
        with open("attendance_weekday_500.txt", encoding='utf-8') as f:
            for _ in range(500):
                line = f.readline()
                if not line:
                    break
                parts = line.strip().split()
                if len(parts) == 2:
                    add_new_player(parts[0])
                    calculate_basic_point(parts[0], parts[1])

        calculate_bonus_point()
        update_player_grade()

        print_player_info()
        print_removed_player()

    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")


def print_player_info():
    for i in range(1, id_cnt + 1):
        print(f"NAME : {player_names[i]}, POINT : {points[i]}, GRADE : ", end="")
        print_grade(i)


def update_player_grade():
    for i in range(1, id_cnt + 1):
        if points[i] >= 50:
            grade[i] = 1
        elif points[i] >= 30:
            grade[i] = 2
        else:
            grade[i] = 0


def calculate_bonus_point():
    for i in range(1, id_cnt + 1):
        if attendance_count[i][2] > 9:
            points[i] += 10
        if attendance_count[i][5] + attendance_count[i][6] > 9:
            points[i] += 10


def print_removed_player():
    print("\nRemoved player")
    print("==============")
    for i in range(1, id_cnt + 1):
        if grade[i] not in (1, 2) and attendance_wed[i] == 0 and attendance_weekends[i] == 0:
            print(player_names[i])


def print_grade(player_id):
    if grade[player_id] == 1:
        print("GOLD")
    elif grade[player_id] == 2:
        print("SILVER")
    else:
        print("NORMAL")


if __name__ == "__main__":
    input_file()
