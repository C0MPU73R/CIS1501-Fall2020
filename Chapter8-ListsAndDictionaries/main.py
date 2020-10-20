import random

my_list = [1, 1, 2, 3, 5, 8, 13]

print(my_list[:])

#del my_list[4]

print(my_list[:])

# index position, value
my_list.insert(0, 0)
print(my_list[:])

my_list.remove(1)

print(my_list[:])

my_list.insert(1, 1)

my_list.pop()

new_list = []

for value in range(20):
    new_list.append(random.randint(1, 100))

print(new_list)

# modify the list
new_list.sort()

print(new_list)

new_list.reverse()

print(new_list)


for index in range(len(new_list)):
    print(index+new_list[index])

print()

for index, value in enumerate(new_list):
    print(index + value)

list_of_lists = []
number = 0
for row in range(5):
    list_of_lists.append([])
    for item in range(5):
        list_of_lists[row].append(number)
        number += 1

print(list_of_lists)

print()

for row in list_of_lists:
    print(row)

print(list_of_lists[3][1])

for row_index in range(len(list_of_lists)):
    for column_index in range(len(list_of_lists[row_index])):
        print(list_of_lists[row_index][column_index], end=" ")
    print()

for row in list_of_lists:
    for item in row:
        print(item, end=" ")
    print()

print(new_list)

original_list = new_list[:]

# when removing items, always iterate over a copy
for item in new_list[:]:
    if item % 2 == 1:
        new_list.remove(item)

print(new_list)

print(original_list)

odds = [ number for number in original_list if (number % 2) == 1 ]
evens = [ number for number in original_list if (number % 2) == 0 ]

print(odds)
print(evens)

# sorted creates a new list
sorted_odds = sorted(odds)