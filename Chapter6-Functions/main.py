import random


def print_hello():
    print('Hello world')
    print("I am the computer, nice to meet you")


def count_down(number):
    while number > 0:
        print(number)
        number -= 1
    print("blast off!")


def area_of_a_rectangle(length, width):
    return length * width


print_hello()

print("Hi computer, I'm Eric")

print(f"pi rounded to 3 digits is: {round(3.14159, 2)}")

print_hello()
my_number = 10
count_down(my_number)
print(my_number)

# do not assign a function to a variable if it doesn't return a value
result = count_down(20)
# None for you!
print(result)

number_to_count_down_from = int(input("Enter a number to down down"))

count_down(number_to_count_down_from)

print(number_to_count_down_from)

print(f'area of a 4x5 rectangle is {area_of_a_rectangle(4,5)}')

print(f'area of a 4x5 rectangle is {area_of_a_rectangle("4",5)}')


print("TODO for Thursday - start with Functions as Objects 6.8")


def normal_greeting():
    print("Hello")


def borg_greeting():
    print("Prepare to be assimilated")


def pretend_to_talk_to_people(greeting):
    greeting()
    print("What is your name?")

# passing a function as an argument
if random.randint(0,1) == 0:
    pretend_to_talk_to_people(normal_greeting)
else:
    pretend_to_talk_to_people(borg_greeting)
