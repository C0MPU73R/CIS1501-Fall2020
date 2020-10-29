class Lamp:

    def __init__(self):
        self._is_on = False
        self._color = "white"

    def toggle(self):
        self._is_on = not self._is_on

    def is_on(self):
        return self._is_on

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color


class Square:

    def __init__(self, length_in_centimeters):
        self._side_length = length_in_centimeters

    def get_side_length(self):
        return self._side_length

    def get_perimeter(self):
        return self._side_length * 4

    def get_area(self):
        return self._side_length ** 2

    def __str__(self):
        return f"Side length: {self._side_length} " \
               f"- perimeter: {self.get_perimeter()} " \
               f"- area: {self.get_area()}"

    def __lt__(self, other):
        return self.get_side_length() < other.get_side_length()

    def __eq__(self, other):
        return self.get_side_length() == other.get_side_length()

    def __gt__(self, other):
        # shortcut - the efficent lazy way
        return not ( self == other or self < other )


class Can:

    def __init__(self, ounces=0):
        if ounces < 0:
            ounces = 0
        self._total_volume_in_ounces = ounces
        self._current_volume_in_ounces = ounces

    def drink(self, ounces_to_drink):
        self._current_volume_in_ounces -= ounces_to_drink
        if self._current_volume_in_ounces < 0:
            self._current_volume_in_ounces = 0
            return False
        else:
            return True

    def get_current_volume_in_ounces(self):
        return self._current_volume_in_ounces


# variable = what we are assigning
la_croix_can = Can(12)
la_croix_can.drink(1)
print(f'Can has {la_croix_can.get_current_volume_in_ounces()} ounces remaining')
la_croix_can.drink(1)
print(f'Can has {la_croix_can.get_current_volume_in_ounces()} ounces remaining')
la_croix_can.drink(1)
print(f'Can has {la_croix_can.get_current_volume_in_ounces()} ounces remaining')

ice_mountain_can = Can(12)
print(f'Ice mountain can has {ice_mountain_can.get_current_volume_in_ounces()} ounces remaining')

def print_square_info(square):
    print(f'This square has a side length of {square.get_side_length()} cm')
    print(f'This square has a perimeter of {square.get_perimeter()} cm')
    print(f'This square has an area of {square.get_area()} cm^2')


small_square = Square(2)
print_square_info(small_square)
big_square = Square(234)
print_square_info(big_square)
print(small_square)

print(f"small_square < big_square: {small_square < big_square}")
print(f"small_square == big_square: {small_square == big_square}")
print(f"small_square > big_square: {small_square > big_square}")

# this fails if we don't have the methods defined
#print(f'la_croix_can < ice_mountain_can: {la_croix_can < ice_mountain_can}')

# this checks if they are the same object in memory
print(f'la_croix_can == ice_mountain_can: {la_croix_can == ice_mountain_can}')

la_croix_can = ice_mountain_can
print(f'la_croix_can == ice_mountain_can: {la_croix_can == ice_mountain_can}')
la_croix_can.drink(2)
ice_mountain_can.drink(2)

#print(f'la_croix_can > ice_mountain_can: {la_croix_can > ice_mountain_can}')
