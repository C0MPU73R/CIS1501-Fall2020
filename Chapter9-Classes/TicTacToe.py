class TicTacToe:

    def __init__(self):
        self._board = [[' ', ' ', ' '],
                       [' ', ' ', ' '],
                       [' ', ' ', ' ']]
        self._current_player = 'X'

    def mark(self, row, column):
        if self._board[row][column] == ' ':
            self._board[row][column] = self._current_player
            if self._current_player == 'X':
                self._current_player = 'O'
            else:
                self._current_player = 'X'
            return True
        else:
            return False

    def game_over(self):
        return self.cats_game() or self.has_winner()

    def cats_game(self):
        for row in self._board:
            if " " in row:
                return False
        return True

    def has_winner(self):
        return self.has_winner_by_row() or \
               self.has_winner_by_column() or \
               self.has_winner_by_diagonal()

    def has_winner_by_row(self):
        for row in self._board:
            if row[0] == row[1] == row[2] and row[0] != ' ':
                return True
        return False

    def has_winner_by_column(self):
        for column_index in range(len(self._board)):
            if self._board[0][column_index] == self._board[1][column_index] == self._board[2][column_index] and self._board[0][column_index] != ' ':
                return True
        return False

    def has_winner_by_diagonal(self):
        return (self._board[0][0] == self._board[1][1] == self._board[2][2]
                or self._board[0][2] == self._board[1][1] == self._board[2][0]) \
                and self._board[1][1] != ' '

    def __str__(self):
        board_string = ""
        for row in self._board:
            board_string += "|".join(row)
            board_string += "\n"
            board_string += "-----" + "\n"
        return board_string[:-6]


if __name__ == '__main__':
    play_again = 'y'
    while play_again == 'y':
        board = TicTacToe()

        while not board.game_over():
            print(board)
            location = input('Enter a row and column to mark (0 0)')
            row = int(location[0])
            column = int(location[2])
            did_mark = board.mark(row, column)
            if not did_mark:
                print('invalid mark, try again')
        print(board)
        print('game over!')
        play_again = input('Play again? y/n').lower()
