from unittest import TestCase

# from 'name of py file with main.py' import 'class name'
from main import Square


class TestSquare(TestCase):
    def test_get_side_length(self):
        # AAA method - Arrange - Act - Assert

        # arrange the variables we need to test
        expected_side_length = 3

        # act on the code ( call the function )
        square = Square(expected_side_length)
        actual_side_length = square.get_side_length()

        # assert we got the expected results
        self.assertEqual(expected_side_length, actual_side_length)

    def test_get_perimeter(self):
        # AAA method - Arrange - Act - Assert

        # arrange the variables we need to test
        side_length = 3
        expected_perimeter = side_length * 4

        # act on the code ( call the function )
        square = Square(side_length)
        actual_perimeter = square.get_perimeter()

        # assert we got the expected results
        self.assertEqual(expected_perimeter, actual_perimeter)

    def test_get_area(self):
        # AAA method - Arrange - Act - Assert

        # arrange the variables we need to test
        side_length = 3
        expected_area = side_length * side_length

        # act on the code ( call the function )
        square = Square(side_length)
        actual_area = square.get_area()

        # assert we got the expected results
        self.assertEqual(expected_area, actual_area)
