import csv
from collections import Counter

binary = []
rows = []
row = -1
gamma = ""
epsilon = ""
oxygen = ""
co2 = ""


def prep_data():
    global binary

    with open("day_03.csv", "r") as f:
        data = csv.reader(f)
        binary_tmp = list(data)

    binary = [i[0] for i in binary_tmp]

    for i in range(len(binary[0])):
        global row
        row += 1
        rows.append([i[0][row] for i in binary_tmp])


def bin_to_dec(n):
    return int(n, 2)


def get_gamma(lst):
    global gamma

    for i in lst:
        cnt = Counter(i)
        gamma += cnt.most_common(1)[0][0]

    return gamma


def get_epsilon():
    global epsilon

    for i in gamma:
        if i == "0":
            epsilon += "1"
        else:
            epsilon += "0"

    return epsilon


def get_oxygen(lst_r, lst_b):
    global oxygen
    cnt = -1
    oxygen = lst_b

    while len(oxygen) != 1:
        cnt += 1
        zero = 0
        one = 0
        higher = "0"

        for n in oxygen:
            if n[cnt] == "0":
                zero += 1
            else:
                one += 1

        if one == zero:
            higher = "1"
        elif one > zero:
            higher = "1"

        oxygen = [n for n in oxygen if n[cnt] == higher]

    return oxygen[0]


def get_co2(lst_r, lst_b):
    global co2

    cnt = -1
    co2 = binary

    while len(co2) != 1:
        cnt += 1
        zero = 0
        one = 0
        lesser = "0"

        for n in co2:
            if n[cnt] == "0":
                zero += 1
            else:
                one += 1

        if one == zero:
            lesser = "0"
        elif one < zero:
            lesser = "1"

        co2 = [n for n in co2 if n[cnt] == lesser]

    return co2[0]


prep_data()

gamma_dec = bin_to_dec(get_gamma(rows))
epsilon_dec = bin_to_dec(get_epsilon())
oxygen_dec = bin_to_dec(get_oxygen(rows, binary))
co2_dec = bin_to_dec(get_co2(rows, binary))


# SOLUTION
print(f"PART 1 | Gamma: {gamma_dec} - Epsilon: {epsilon_dec} - Multiplier: {gamma_dec * epsilon_dec}")
print(f"PART 2 | Oxygen: {oxygen_dec} - CO2: {co2_dec} - Multiplier: {oxygen_dec * co2_dec}")
