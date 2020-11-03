from unittest import TestCase
from main import Cup

class TestCup(TestCase):
    def test_add(self):
        # Arrange
        expected_current_volume = 50
        cup = Cup(expected_current_volume)

        # Act
        cup.add(expected_current_volume)
        actual_current_volume = cup.current_volume_in_milliliters

        # Assert
        self.assertEqual(expected_current_volume, actual_current_volume)

    def test_add_causes_exception(self):
        # Arrange
        expected_current_volume = 50
        cup = Cup(expected_current_volume)

        # Act
        # nothing here, we are asserting

        # Assert  -- type of error, name of method NO (), argument passed
        self.assertRaises(ValueError, cup.add, expected_current_volume*2)


    def test_drink(self):
        # Arrange
        expected_current_volume = 40
        cup = Cup(50)
        cup.add(50)

        # Act
        cup.drink(10)
        actual_current_volume = cup.current_volume_in_milliliters

        # Assert
        self.assertEqual(expected_current_volume, actual_current_volume)

    def test_drink_raises_exception(self):
        # Arrange
        cup = Cup(0)

        # Act
        # nothing here, it's in the assert

        # Assert
        self.assertRaises(ValueError, cup.drink, 1)
