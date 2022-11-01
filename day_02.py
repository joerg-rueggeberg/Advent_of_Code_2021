import csv

horizontal = 0
depth = 0
aim = 0

# DATA
with open("day_02.csv", "r") as f:
    data = csv.reader(f)
    course = list(data)

while len(course) != 0:
    temp = course[0][0].split(";")

    if temp[0] == "forward":
        horizontal += int(temp[1])
        depth += aim * int(temp[1])
        print(f"{temp[0]}: {temp[1]} | total: {horizontal} horizontal - {aim} aim")
    elif temp[0] == "up":
        aim -= int(temp[1])
        # depth -= int(temp[1])
        print(f"{temp[0]}: {temp[1]} | total: {depth} depth - {aim} aim")
    else:
        aim += int(temp[1])
        # depth += int(temp[1])
        print(f"{temp[0]}: {temp[1]} | total: {depth} depth - {aim} aim")

    del course[0]

print(f"solution | horizontal: {horizontal} | depth: {depth} | multi: {horizontal * depth}")