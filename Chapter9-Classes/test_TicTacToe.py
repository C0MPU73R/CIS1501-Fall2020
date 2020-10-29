from unittest import TestCase
from TicTacToe import TicTacToe

class TestTicTacToe(TestCase):
    def test_mark(self):
        # AAA

        # Arrange
        board = TicTacToe()

        # Act
        first_mark_works = board.mark(0, 0)
        second_mark_fails = board.mark(0, 0)

        # Assert
        self.assertTrue(first_mark_works)
        self.assertFalse(second_mark_fails)

    def test_cats_games(self):
        # AAA

        # Arrange
        board = TicTacToe()
        board.mark(0, 0)
        board.mark(0, 1)
        board.mark(0, 2)
        board.mark(1, 1)
        board.mark(1, 0)
        board.mark(2, 0)
        board.mark(2, 1)
        board.mark(1, 2)
        board.mark(2, 2)

        print(board)

        # Act
        is_cats_game = board.cats_game()

        # Assert
        self.assertTrue(is_cats_game)

    def test_has_winner_by_row(self):
        # AAA

        # Arrange
        board = TicTacToe()
        board.mark(0, 0)
        board.mark(1, 0)
        board.mark(0, 1)
        board.mark(1, 1)
        board.mark(0, 2)

        # Act
        has_winner = board.has_winner_by_row()

        # Assert
        self.assertTrue(has_winner)

    def test_has_winner_by_column(self):
        # AAA

        # Arrange
        board = TicTacToe()
        board.mark(0, 0)
        board.mark(0, 1)
        board.mark(1, 0)
        board.mark(1, 1)
        board.mark(2, 0)

        print(board)

        # Act
        has_winner = board.has_winner_by_column()

        # Assert
        self.assertTrue(has_winner)

    def test_has_winner_by_diagonal_down(self):
        # AAA

        # Arrange
        board = TicTacToe()
        board.mark(0, 0)
        board.mark(0, 1)
        board.mark(1, 1)
        board.mark(0, 2)
        board.mark(2, 2)

        # Act
        has_winner = board.has_winner_by_diagonal()

        # Assert
        self.assertTrue(has_winner)

    def test_has_winner_by_diagonal_up(self):
        # AAA

        # Arrange
        board = TicTacToe()
        board.mark(2, 0)
        board.mark(0, 1)
        board.mark(1, 1)
        board.mark(0, 0)
        board.mark(0, 2)

        print(board)

        # Act
        has_winner = board.has_winner_by_diagonal()

        # Assert
        self.assertTrue(has_winner)
