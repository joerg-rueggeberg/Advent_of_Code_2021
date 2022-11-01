import csv
sol = 0

# GENERATE DATA
measurements = []

with open("day_01.csv", "r") as f:
    data = csv.reader(f)
    measurements_raw = list(data)

for i in measurements_raw:
    measurements.append(i[0])

# CHECK INCREASE
while len(measurements) != 3:
    a = measurements[0]
    b = measurements[1]
    c = measurements[2]

    sum_1 = int(a) + int(b) + int(c)

    del measurements[0]

    a = measurements[0]
    b = measurements[1]
    c = measurements[2]
    sum_2 = int(a) + int(b) + int(c)

    if sum_2 > sum_1:
        print(f"{sum_2} (increased)")
        sol += 1
    elif sum_2 == sum_1:
        print(f"{sum_2} (no change)")
    else:
        print(f"{sum_2} (decreased)")

print(sol)
