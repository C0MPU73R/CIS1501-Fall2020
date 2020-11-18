class Connect4:

    def __init__(self):
        self._board = []
        for row_index in range(6):
            self._board.append([])
            for column in range(7):
                self._board[row_index].append(' ')
        self._current_player = 'X'

    def get_current_player(self):
        return self._current_player

    def drop_piece(self, column_index):
        if column_index < 0 or column_index >= 7:
            raise ValueError('column_index must be 0-6')
        for row_index in range(5, -1, -1):
            if self._board[row_index][column_index] == ' ':
                self._board[row_index][column_index] = self._current_player
                if self._current_player == 'X':
                    self._current_player = 'O'
                else:
                    self._current_player = 'X'
                return
        raise ValueError('column was already full')

    def is_game_over(self):
        return self.is_tied() or self.has_winner()

    def is_tied(self):
        for row in self._board:
            if ' ' in row:
                return False
        return not (self.has_winner())

    def has_winner(self):
        return self._has_winner_by_column() or \
                    self._has_winner_by_row() or \
                    self._has_winner_by_diagonal()

    def _has_winner_by_row(self):
        for row in self._board:
            for column_index in range(0, 4):
                if row[column_index] != ' ' and \
                        row[column_index] == row[column_index + 1] and \
                        row[column_index] == row[column_index + 2] and \
                        row[column_index] == row[column_index + 3]:
                    return True
        return False

    def _has_winner_by_column(self):
        for column_index in range(0, 7):
            for row_index in range(0, 3):
                if self._board[row_index][column_index] != ' ' and \
                        self._board[row_index][column_index] == self._board[row_index + 1][column_index] and \
                        self._board[row_index][column_index] == self._board[row_index + 2][column_index] and \
                        self._board[row_index][column_index] == self._board[row_index + 3][column_index]:
                    return True
        return False

    def _has_winner_by_diagonal(self):
        return self._has_winner_by_diagonal_up() or self._has_winner_by_diagonal_down()

    def _has_winner_by_diagonal_down(self):
        for row_index in range(0, 3):
            for column_index in range(0, 4):
                if self._board[row_index][column_index] != ' ' and \
                        self._board[row_index][column_index] == self._board[row_index + 1][column_index + 1] and \
                        self._board[row_index][column_index] == self._board[row_index + 2][column_index + 2] and \
                        self._board[row_index][column_index] == self._board[row_index + 3][column_index + 3]:
                    return True
        return False

    def _has_winner_by_diagonal_up(self):
        for row_index in range(3, 6):
            for column_index in range(0, 4):
                if self._board[row_index][column_index] != ' ' and \
                        self._board[row_index][column_index] == self._board[row_index - 1][column_index + 1] and \
                        self._board[row_index][column_index] == self._board[row_index - 2][column_index + 2] and \
                        self._board[row_index][column_index] == self._board[row_index - 3][column_index + 3]:
                    return True
        return False