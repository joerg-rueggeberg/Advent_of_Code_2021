import csv

boards = {}
board_win = []
draws_count = -1
draws_last = 0
draws = [18, 99, 39, 89, 0, 40, 52, 72, 61, 77, 69, 51, 30, 83, 20, 65, 93, 88, 29, 22, 14, 82, 53, 41, 76, 79, 46, 78,
         56, 57, 24, 36, 38, 11, 50, 1, 19, 26, 70, 4, 54, 3, 84, 33, 15, 21, 9, 58, 64, 85, 10, 66, 17, 43, 31, 27, 2,
         5, 95, 96, 16, 97, 12, 34, 74, 67, 86, 23, 49, 8, 59, 45, 68, 91, 25, 48, 13, 28, 81, 94, 92, 42, 7, 37, 75,
         32, 6, 60, 63, 35, 62, 98, 90, 47, 87, 73, 44, 71, 55, 80]
playing = True


def prep_data():
    global boards
    cnt = -1

    with open("day_04.csv", "r") as f:
        data = csv.reader(f)
        boards_tmp = list(data)
        boards_tmp = [i[0].split(" ") for i in boards_tmp]

        for i in range(len(boards_tmp)):
            for n in boards_tmp[i]:
                if n == "":
                    boards_tmp[i].remove(n)

        while len(boards_tmp) != 0:

            row_1 = [eval(i) for i in boards_tmp[0]]
            row_2 = [eval(i) for i in boards_tmp[1]]
            row_3 = [eval(i) for i in boards_tmp[2]]
            row_4 = [eval(i) for i in boards_tmp[3]]
            row_5 = [eval(i) for i in boards_tmp[4]]

            cnt += 1
            boards[cnt] = {
                "row_1": row_1,
                "row_1_check": ["", "", "", "", ""],
                "row_2": row_2,
                "row_2_check": ["", "", "", "", ""],
                "row_3": row_3,
                "row_3_check": ["", "", "", "", ""],
                "row_4": row_4,
                "row_4_check": ["", "", "", "", ""],
                "row_5": row_5,
                "row_5_check": ["", "", "", "", ""],
                "sum_unmarked": sum(row_1) + sum(row_2) + sum(row_3) + sum(row_4) + sum(row_5),
                "got_bingo": 0,
            }
            for i in range(5):
                del boards_tmp[0]


def draw_number():
    global draws_count
    global draws_last

    draws_count += 1
    draws_last = draws[draws_count]
    return draws[draws_count]


def check_board(num):
    global boards

    for i in boards:
        if boards[i]['got_bingo'] == 0:
            if num in boards[i]['row_1']:
                boards[i]['row_1_check'][boards[i]['row_1'].index(num)] = num
                boards[i]['sum_unmarked'] -= num
            elif num in boards[i]['row_2']:
                boards[i]['row_2_check'][boards[i]['row_2'].index(num)] = num
                boards[i]['sum_unmarked'] -= num
            elif num in boards[i]['row_3']:
                boards[i]['row_3_check'][boards[i]['row_3'].index(num)] = num
                boards[i]['sum_unmarked'] -= num
            elif num in boards[i]['row_4']:
                boards[i]['row_4_check'][boards[i]['row_4'].index(num)] = num
                boards[i]['sum_unmarked'] -= num
            elif num in boards[i]['row_5']:
                boards[i]['row_5_check'][boards[i]['row_5'].index(num)] = num
                boards[i]['sum_unmarked'] -= num


def check_bingo():
    global boards
    global board_win
    global playing

    for i in boards:
        if boards[i]['got_bingo'] == 0:
            if "" not in boards[i]['row_1_check'] or \
                    "" not in boards[i]['row_2_check'] or \
                    "" not in boards[i]['row_3_check'] or \
                    "" not in boards[i]['row_4_check'] or \
                    "" not in boards[i]['row_5_check'] or \
                    boards[i]['row_1_check'][0] != "" \
                    and boards[i]['row_2_check'][0] != "" \
                    and boards[i]['row_3_check'][0] != "" \
                    and boards[i]['row_4_check'][0] != "" \
                    and boards[i]['row_5_check'][0] != "" \
                    or boards[i]['row_1_check'][1] != "" \
                    and boards[i]['row_2_check'][1] != "" \
                    and boards[i]['row_3_check'][1] != "" \
                    and boards[i]['row_4_check'][1] != "" \
                    and boards[i]['row_5_check'][1] != "" \
                    or boards[i]['row_1_check'][2] != "" \
                    and boards[i]['row_2_check'][2] != "" \
                    and boards[i]['row_3_check'][2] != "" \
                    and boards[i]['row_4_check'][2] != "" \
                    and boards[i]['row_5_check'][2] != "" \
                    or boards[i]['row_1_check'][3] != "" \
                    and boards[i]['row_2_check'][3] != "" \
                    and boards[i]['row_3_check'][3] != "" \
                    and boards[i]['row_4_check'][3] != "" \
                    and boards[i]['row_5_check'][3] != "" \
                    or boards[i]['row_1_check'][4] != "" \
                    and boards[i]['row_2_check'][4] != "" \
                    and boards[i]['row_3_check'][4] != "" \
                    and boards[i]['row_4_check'][4] != "" \
                    and boards[i]['row_5_check'][4] != "":
                print(f"BINGO: board {i}")
                board_win = [i, draws_last]
                boards[i]['got_bingo'] = 1
                # playing = False


def calc_score():
    global boards
    winner = board_win[0]
    bingo_draw = board_win[1]
    boards[winner]['final_score'] = boards[winner]['sum_unmarked'] * bingo_draw

    print(
        f"SCORE | winner: {winner} - unmarked: {boards[winner]['sum_unmarked']} - "
        f"total: {boards[winner]['final_score']} ({bingo_draw})")


prep_data()

# while playing:
for b in range(len(draws)):
    check_board(draw_number())
    check_bingo()

calc_score()
