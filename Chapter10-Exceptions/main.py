

class Cup:

    def __init__(self, capacity_in_milliliters):
        if capacity_in_milliliters < 0:
            raise ValueError('Capacity may not be negative')

        self.capacity_in_milliliters = capacity_in_milliliters
        self.current_volume_in_milliliters = 0

    def add(self, milliliters_to_add):
        if milliliters_to_add + self.current_volume_in_milliliters > self.capacity_in_milliliters:
            raise ValueError('Cup is not large enough')
        self.current_volume_in_milliliters += milliliters_to_add

    def drink(self, milliliters_to_drink):
        if milliliters_to_drink > self.current_volume_in_milliliters:
            raise ValueError('Not enough in the cup to drink')
        self.current_volume_in_milliliters -= milliliters_to_drink


class MyCustomException(Exception):

    def __init__(self, value):
        self.value = value

if __name__ == '__main__':

    try_again = 'y'

    while try_again.lower() == 'y':
        try:
            temp_in_f = int(input("Enter the temp in F degrees"))
            print(f'temp in c: {(temp_in_f - 32) * 5 / 9}')
        except ValueError:
            print("That's not a valid number")
        try_again = input("Try again? y/n")



    mug = Cup(250)
    try:
        impossible = Cup(-10)
    except ValueError as exception:
        print(exception)



    try:
        mug.add(500)
    except ValueError as exception:
        print(exception)

    try:
        mug.drink(1)
    except ValueError as exception:
        print(exception)


    numbers = ( 1, 1, 2, 3, 5, 8, 13, 21, 34, 55 )
    try:
        numbers[2] = 7
    except TypeError as exception:
        print(exception)

    number = int(input("enter a number"))
    if number < 100:
        raise MyCustomException("Number can't be less than 100")



