import field


class Game:
    HEADER = ' ' * 20 + 30 * '=' + "CONWAY'S GAME OF LIFE" + 30 * '='

    def play_game(self):
        while True:
            my_field = field.Field()
            self.print_menu()
            command = input('>')

            if command == '1':
                my_field.matrix_fill([18, 18], field.Field.ALIVE_CELL)
                my_field.matrix_fill([18, 19], field.Field.ALIVE_CELL)
                my_field.matrix_fill([18, 20], field.Field.ALIVE_CELL)
                my_field.matrix_fill([17, 18], field.Field.ALIVE_CELL)
                my_field.matrix_fill([17, 19], field.Field.ALIVE_CELL)
                my_field.matrix_fill([17, 20], field.Field.ALIVE_CELL)
                my_field.matrix_fill([19, 18], field.Field.ALIVE_CELL)
                my_field.matrix_fill([19, 20], field.Field.ALIVE_CELL)
                print(self.HEADER)
                print(my_field)
                self.start_iterations(my_field)

            elif command == '2':
                address = None
                while address != 'start':
                    print(self.HEADER)
                    print(my_field)
                    print('Input cell address in format "row col". If ready input "start"')
                    address = input('>')
                    try:
                        address = list(map(int, address.split()))
                        row, col = address
                        if row > field.Field.FIELD_SIZE or col > field.Field.FIELD_SIZE:
                            raise Exception
                    except Exception:
                        print('Invalid input format, try again')
                        continue
                    my_field.matrix_fill(address, field.Field.ALIVE_CELL)

                print(self.HEADER)
                print(my_field)
                self.start_iterations(my_field)

            elif command == '3':
                print('bye bye!')
                break
            else:
                print('invalid command, try again')

    @staticmethod
    def print_menu():
        print(Game.HEADER)
        print('''\n                 Main menu

                1 - choose a default figure
                2 - create your figure
                3 - exit
                ''')

    @staticmethod
    def start_iterations(some_field):
        while True:
            command_2 = input('press Enter to continue, or input "exit" to exit\n')
            some_field.get_new_condition()
            print(Game.HEADER)
            print(some_field)
            if command_2 == 'exit':
                break
