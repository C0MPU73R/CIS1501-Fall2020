import random

# mapping type - key and associated value

# key : value
grades = {'Eric': 97, 'Jeb': 95}

# [ ] reads as 'key of' - same notation is for add or upate
grades['Journey'] = 86

if 'Eric' in grades:
    print(grades["Eric"])

grades.pop('Eric')
print(grades)

name = input("enter a name")
print("Score for:", name, ":", grades.get(name, 0))

number_of_sides = int(input("How many sides on your die?"))
number_of_dice_to_roll = int(input("How many dice should we roll?"))
number_of_rolls = int(input("How many times should we roll the dice?"))

sums = {}

for roll in range(number_of_rolls):
    sum = 0
    for die in range(number_of_dice_to_roll):
        sum += random.randint(1, number_of_sides)
    if sum in sums:
        sums[sum] += 1
    else:
        sums[sum] = 1

for sum in sorted(sums.keys()):
    print(sum, ":", "*" * sums[sum])

print("The most common sum was found :", max(sums.values()))

number = 0

grid = []
for row_index in range(8):
    grid.append([])
    for column in range(8):
        grid[row_index].append(number)
        number+=1

for row in grid:
    print(row)

print(grid[2][7])


multiplication_chart = []

for row_index in range(0,11):
    multiplication_chart.append([])
    if row_index == 0:
        for number in range(0,11):
            multiplication_chart[row_index].append(number)
    else:
        multiplication_chart[row_index].append(row_index)

for row in multiplication_chart:
    print(row)

for row_index in range(1, 11):
    for column_index in range(1, 11):
        multiplication_chart[row_index].append(
            multiplication_chart[row_index][0] *
            multiplication_chart[0][column_index])

for row in multiplication_chart:
    for item in row:
        print(f'{item:3} ', end="")
    print()