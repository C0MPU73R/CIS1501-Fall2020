import random

hours = 0
minutes = 0
seconds = 0

while hours < 24:
    minutes = 0
    # for every run of the hour loop, the inner loop runs from start to finish
    while minutes < 60:
        seconds = 0
        while seconds < 60:
            print(f'{hours:02d}:{minutes:02d}:{seconds:02d}')
            seconds += 1
        minutes += 1
    hours += 1

# if you like for loops instead of while loops
for hours in range(24):
    for minutes in range(60):
        for seconds in range(60):
            print(f'{hours:02d}:{minutes:02d}:{seconds:02d}')

# this is a bad loop!
while True:
    answer = input("What is the answer to life, the universe and everything?")
    if answer == "42":
        break

for number in range(100):
    if number % 15 == 0:
        print("fizzbuzz")
    elif number % 3 == 0:
        print("fizz")
    elif number % 5 == 0:
        print("buzz")
    else:
        print(number)

for number in range(100):
    if number % 15 == 0:
        print("fizzbuzz")
        continue

    if number % 3 == 0:
        print("fizz")
        continue

    if number % 5 == 0:
        print("buzz")
        continue

    print(number)


magic_number = random.randint(1, 100)

guess = 0

while guess != magic_number:
    guess = int(input("Enter a number between 1-100 or -1 to give up"))

    if guess == -1:
        break

    if guess < magic_number:
        print("too low!")
    elif guess > magic_number:
        print("too high!")
else:
    print("You got it right!")


names = ['Eric', 'John', 'Bob', 'Mary']

for index in range(len(names)):
    print(f"At index {index}: {names[index]}")

for index, value in enumerate(names):
    print(f"At index {index}: {value}")


number_of_7s_rolled = 0
for roll in range(36):

    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)

    sum_of_dice = die1 + die2

    if sum_of_dice == 7:
        number_of_7s_rolled += 1

print(f'In 36 simulated rolls, a 7 was rolled {number_of_7s_rolled} times')


