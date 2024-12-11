from gameparts import Board
from gameparts.exceptions import FieldIndexError


def main():
    game = Board()
    game.display()

    while True:
        try:
            row = int(input('Введите номер строки: '))
            if row < 0 or row >= game.field_size:
                raise FieldIndexError

            column = int(input('Введите номер столбца: '))
            if column < 0 or column >= game.field_size:
                raise FieldIndexError

        except FieldIndexError:
            print(
                'Значение должно быть неотрицательным и меньше '
                f'{game.field_size}.'
            )
            print('Пожалуйста, введите значения для строки и столбца заново.')
            continue

        else:
            break

    game.make_move(row, column, 'X')
    print('Ход сделан!')
    game.display()


if __name__ == '__main__':
    main()
