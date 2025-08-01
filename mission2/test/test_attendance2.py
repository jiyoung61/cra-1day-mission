from mission2.attendance import input_file
from mission2.player import Player

def test_attendance_golden(capsys):
    input_file()
    out, err = capsys.readouterr()

    assert out == ('NAME : Umar, POINT : 48, GRADE : SILVER\n'
                   'NAME : Daisy, POINT : 45, GRADE : SILVER\n'
                   'NAME : Alice, POINT : 61, GRADE : GOLD\n'
                   'NAME : Xena, POINT : 91, GRADE : GOLD\n'
                   'NAME : Ian, POINT : 23, GRADE : NORMAL\n'
                   'NAME : Hannah, POINT : 127, GRADE : GOLD\n'
                   'NAME : Ethan, POINT : 44, GRADE : SILVER\n'
                   'NAME : Vera, POINT : 22, GRADE : NORMAL\n'
                   'NAME : Rachel, POINT : 54, GRADE : GOLD\n'
                   'NAME : Charlie, POINT : 58, GRADE : GOLD\n'
                   'NAME : Steve, POINT : 38, GRADE : SILVER\n'
                   'NAME : Nina, POINT : 79, GRADE : GOLD\n'
                   'NAME : Bob, POINT : 8, GRADE : NORMAL\n'
                   'NAME : George, POINT : 42, GRADE : SILVER\n'
                   'NAME : Quinn, POINT : 6, GRADE : NORMAL\n'
                   'NAME : Tina, POINT : 24, GRADE : NORMAL\n'
                   'NAME : Will, POINT : 36, GRADE : SILVER\n'
                   'NAME : Oscar, POINT : 13, GRADE : NORMAL\n'
                   'NAME : Zane, POINT : 1, GRADE : NORMAL\n'
                   '\n'
                   'Removed player\n'
                   '==============\n'
                   'Bob\n'
                   'Zane\n')

def test_check_list_reference_works():
    player_list = [Player("test")]
    player = player_list[0]
    player.points = 100

    assert player_list[0].points == 100

def test_check_player_attendance_week_initial_count():
    player = Player("test")
    assert len(player.attendance_week) == 7 # week days