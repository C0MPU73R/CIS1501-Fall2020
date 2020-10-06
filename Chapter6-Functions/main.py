

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

count_down(10)

# do not assign a function to a variable if it doesn't return a value
result = count_down(20)
# None for you!
print(result)

number_to_count_down_from = int(input("Enter a number to down down"))

count_down(number_to_count_down_from)

print(number_to_count_down_from)

print(f'area of a 4x5 rectangle is {area_of_a_rectangle(4,5)}')

print(f'area of a 4x5 rectangle is {area_of_a_rectangle("4",5)}')


print("TODO for Thursday - start with Functions as Objections 6.8")
