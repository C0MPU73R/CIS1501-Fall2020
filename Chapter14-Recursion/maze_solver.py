class Maze_Solver:

    def __init__(self, maze):
        self._maze = maze
        for row_index in range(len(maze)):
            for column_index in range(len(maze[row_index])):
                if maze[row_index][column_index] == "S":
                    self._current_row = row_index
                    self._current_column = column_index

    def solve(self):
        if self._maze[self._current_row][self._current_column] == 'E':
            print(self)
        else:
            self._maze[self._current_row][self._current_column] = '.'
            # up
            if self._can_go(self._current_row-1, self._current_column):
                self._current_row -= 1
                self.solve()
                self._current_row += 1
            # down
            if self._can_go(self._current_row+1, self._current_column):
                self._current_row += 1
                self.solve()
                self._current_row -= 1
            # left
            if self._can_go(self._current_row, self._current_column-1):
                self._current_column -= 1
                self.solve()
                self._current_column += 1
            # right
            if self._can_go(self._current_row, self._current_column+1):
                self._current_column += 1
                self.solve()
                self._current_column -= 1

            self._maze[self._current_row][self._current_column] = 'D'

    def _can_go(self, row_index, column_index):
        return 0 <= row_index < len(self._maze) \
            and 0 <= column_index < len(self._maze[row_index]) \
            and ( self._maze[row_index][column_index] == " " \
            or self._maze[row_index][column_index] == "E" )

    def __str__(self):
        output = ""
        for row in self._maze:
            output += "".join(row)
            output += '\n'
        return output