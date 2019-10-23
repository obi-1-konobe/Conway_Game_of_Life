from checker import Checker


class Field:
    ALIVE_CELL = '0'
    DEAD_CELL = ' '
    FIELD_SIZE = 40

    def __init__(self):
        self.matrix = []

        for _ in range(self.FIELD_SIZE):
            some_list = []
            for _ in range(self.FIELD_SIZE):
                some_list.append(self.DEAD_CELL)
            self.matrix.append(some_list)

    def __str__(self):
        indent = ' ' * 20
        str_matrix = indent + ' ' + ' 0' * 10 + ' 1' * 10 + ' 2' * 10 + ' 3' * 10 + '\n' + indent
        str_matrix += ' ' + ' 0 1 2 3 4 5 6 7 8 9' * 4 + '\n' + indent
        for i in range(self.FIELD_SIZE):
            if i < 10:
                str_matrix += f'0{i}'
            else:
                str_matrix += f'{i}'
            for j in range(self.FIELD_SIZE):
                str_matrix += f'{self.matrix[i][j]} '
            str_matrix += '\n' + indent
        return str_matrix

    def matrix_fill(self, address, symbol):
        row, col = address
        self.matrix[row][col] = symbol

    def get_new_condition(self):
        checker = Checker()
        dead_cells = checker.dead_iteration(self)
        alive_cells = checker.alive_iteration(self)
        for cell_address in dead_cells:
            self.matrix_fill(cell_address, self.DEAD_CELL)
        for cell_address in alive_cells:
            self.matrix_fill(cell_address, self.ALIVE_CELL)

        return self


