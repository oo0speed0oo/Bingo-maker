class BingoLogic:
    def __init__(self, size):
        self.size = size  # For 3x3 or 4x4 boards
        #self.pressed = [[False for col in range(size)] for row in range(size)]
        self.pressed = []
        for row in range(size):
            new_row = []
            for col in range(size):
                new_row.append(False)
            self.pressed.append(new_row)

    def mark_pressed(self, row, col):
        """Mark a cell as pressed."""
        self.pressed[row][col] = True

    def can_press(self, called_label, cell_label):
        return called_label == cell_label

    def check_win(self):
        """Check all rows, columns, and diagonals for a win."""
        return (
            self.check_rows() or
            self.check_columns() or
            self.check_diagonals()
        )

    def check_rows(self):
        for row in self.pressed:
            if all(row):
                return True
        return False

    def check_columns(self):
        for col in range(self.size):
            if all(self.pressed[row][col] for row in range(self.size)):
                return True
        return False

    def check_diagonals(self):
        # Top-left to bottom-right
        if all(self.pressed[i][i] for i in range(self.size)):
            return True
        # Top-right to bottom-left
        if all(self.pressed[i][self.size - 1 - i] for i in range(self.size)):
            return True
        return False

