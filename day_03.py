# SOLUTION: PART 1

import csv

rows = []
row = -1
gamma = ""
epsilon = ""


def prep_data():
    with open("day_03.csv", "r") as f:
        data = csv.reader(f)
        binary_tmp = list(data)

    binary = [i[0] for i in binary_tmp]

    for i in range(len(binary[0])):
        global row
        row += 1
        rows.append([i[0][row] for i in binary_tmp])


def get_gamma(lst):
    global gamma
    for i in lst:
        gamma_temp = str((max(set(i), key=i.count)))
        gamma += gamma_temp


def get_epsilon(lst):
    global epsilon
    for i in lst:
        epsilon_temp = str((min(set(i), key=i.count)))
        epsilon += epsilon_temp


def bintodec(n):
    return int(n, 2)


prep_data()
get_gamma(rows)
get_epsilon(rows)

# solution print
print(f"gamma: {bintodec(gamma)} * epsilon: {bintodec(epsilon)} = {bintodec(gamma)*bintodec(epsilon)}")
