import field


class Checker:
    @staticmethod
    def get_neighbors(some_field, cell_address):
        field_matrix = some_field.matrix
        row, col = cell_address
        try:
            neighbors = [
                # up neighbors
                field_matrix[row - 1][col - 1], field_matrix[row - 1][col], field_matrix[row - 1][col + 1],
                #     left neighbor
                field_matrix[row][col - 1],
                #     right neighbor
                field_matrix[row][col + 1],
                #     down neighbors
                field_matrix[row + 1][col - 1], field_matrix[row + 1][col], field_matrix[row + 1][col + 1]
            ]
        except IndexError:
            neighbors = ['qwe']
        return neighbors

    def dead_iteration(self, some_field):
        dead_list = []

        for i in range(field.Field.FIELD_SIZE):
            row = some_field.matrix[i]
            for j in range(field.Field.FIELD_SIZE):
                cell = row[j]
                if cell == field.Field.ALIVE_CELL:
                    cell_address = [i, j]
                    cell_neighbors = self.get_neighbors(some_field, cell_address)
                    alive_neighbors = cell_neighbors.count(field.Field.ALIVE_CELL)
                    if alive_neighbors > 3 or alive_neighbors < 2:
                        dead_list.append(cell_address)

        return dead_list

    def alive_iteration(self, some_field):
        alive_list = []

        for i in range(field.Field.FIELD_SIZE):
            row = some_field.matrix[i]
            for j in range(field.Field.FIELD_SIZE):
                cell = row[j]
                if cell == field.Field.DEAD_CELL:
                    cell_address = [i, j]
                    cell_neighbors = self.get_neighbors(some_field, cell_address)
                    alive_neighbors = cell_neighbors.count(field.Field.ALIVE_CELL)
                    if alive_neighbors == 3:
                        alive_list.append(cell_address)

        return alive_list


