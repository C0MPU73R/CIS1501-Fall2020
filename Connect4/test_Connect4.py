from unittest import TestCase
from Connect4 import Connect4

class TestConnect4(TestCase):
    def test_drop_piece(self):
        # arrange
        game = Connect4()

        # act
        game.drop_piece(1)
        game.drop_piece(1)

        # assert
        self.assertEqual('X', game._board[5][1])
        self.assertEqual('O', game._board[4][1])

    def test_drop_piece_invalid_index_error(self):
        # arrange
        game = Connect4()

        # act

        # assert
        self.assertRaises(ValueError, game.drop_piece, 7)

    def test_drop_piece_column_full_error(self):
        # arrange
        game = Connect4()

        # act
        game.drop_piece(1)
        game.drop_piece(1)
        game.drop_piece(1)
        game.drop_piece(1)
        game.drop_piece(1)
        game.drop_piece(1)

        # assert
        self.assertRaises(ValueError, game.drop_piece, 1)

    def test_is_tied(self):
        # arrange
        game = Connect4()

        # act
        game._board = [
            ['X', 'O', 'X', 'O', 'X', 'O', 'X'],
            ['X', 'O', 'X', 'O', 'X', 'O', 'X'],
            ['X', 'O', 'X', 'O', 'X', 'O', 'X'],
            ['O', 'X', 'O', 'X', 'O', 'X', 'O'],
            ['O', 'X', 'O', 'X', 'O', 'X', 'O'],
            ['O', 'X', 'O', 'X', 'O', 'X', 'O'],
        ]

        # assert
        self.assertTrue(game.is_tied())
        self.assertTrue(game.is_game_over())

    def test_has_winner(self):
        # arrange
        game = Connect4()

        # act
        game.drop_piece(1)
        game.drop_piece(1)
        game.drop_piece(2)
        game.drop_piece(2)
        game.drop_piece(3)
        game.drop_piece(3)
        game.drop_piece(4)

        # assert
        self.assertTrue(game.has_winner())
        self.assertTrue(game._has_winner_by_row())
        self.assertTrue(game.is_game_over())

    def test__has_winner_by_column(self):
        # arrange
        game = Connect4()

        # act
        game.drop_piece(1)
        game.drop_piece(2)
        game.drop_piece(1)
        game.drop_piece(2)
        game.drop_piece(1)
        game.drop_piece(2)
        game.drop_piece(1)

        # assert
        self.assertTrue(game.has_winner())
        self.assertTrue(game._has_winner_by_column())
        self.assertTrue(game.is_game_over())

    def test__has_winner_by_diagonal_up(self):
        # arrange
        game = Connect4()

        # act
        game._board = [
            ['X', 'O', 'X', 'O', 'X', 'O', ' '],
            ['X', 'O', 'X', 'O', 'X', 'O', 'X'],
            ['X', 'O', 'X', 'O', 'X', 'O', 'X'],
            ['O', 'X', 'O', 'X', 'O', 'X', 'O'],
            ['O', 'X', 'X', 'X', 'O', 'X', 'O'],
            ['O', 'X', 'O', 'X', 'O', 'X', 'O'],
        ]

        # assert
        self.assertTrue(game.has_winner())
        self.assertTrue(game._has_winner_by_diagonal())
        self.assertTrue(game._has_winner_by_diagonal_up())
        self.assertTrue(game.is_game_over())

    def test__has_winner_by_diagonal_down(self):
        # arrange
        game = Connect4()

        # act
        game._board = [
            ['X', 'O', 'X', 'O', 'X', 'O', ' '],
            ['X', 'O', 'X', 'O', 'X', 'O', 'X'],
            ['X', 'O', 'X', 'O', 'X', 'O', 'X'],
            ['O', 'X', 'O', 'X', 'O', 'X', 'O'],
            ['O', 'X', 'O', 'X', 'X', 'X', 'O'],
            ['O', 'X', 'O', 'X', 'O', 'X', 'O'],
        ]

        # assert
        self.assertTrue(game.has_winner())
        self.assertTrue(game._has_winner_by_diagonal())
        self.assertTrue(game._has_winner_by_diagonal_down())
        self.assertTrue(game.is_game_over())
