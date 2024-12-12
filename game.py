from gameparts import Board
from gameparts.exceptions import CellOccupiedError, FieldIndexError


def save_result(result):
    with open('results.txt', 'a', encoding='utf-8') as file:
        file.write(result + '\n')


def main():
    game = Board()
    current_player = 'X'
    running = True
    game.display()

    while running:
        print(f'Ход делают {current_player}')

        while True:
            try:
                row = int(input('Введите номер строки: '))
                if row < 0 or row >= game.field_size:
                    raise FieldIndexError

                column = int(input('Введите номер столбца: '))
                if column < 0 or column >= game.field_size:
                    raise FieldIndexError
                
                if game.board[row][column] != ' ':
                    raise CellOccupiedError

            except FieldIndexError:
                print(
                    'Значение должно быть неотрицательным и меньше '
                    f'{game.field_size}.'
                )
                print('Пожалуйста, введите значения для строки и столбца заново.')
                continue
            
            except CellOccupiedError:
                print('Ячейка занята')
                print('Введите другие координаты.')
                continue

            except ValueError:
                print('Вводить можно только целые числа.')
                print('Пожалуйста, введите значения для строки и столбца заново.')
                continue

            except Exception as e:
                print(f'Возникла ошибка: {e}')
                print('Попробуйте ещё раз.')

            else:
                break

        game.make_move(row, column, current_player)
        game.display()

        if game.check_win(current_player):
            result = f'Победили {current_player}.'
            print(result)
            save_result(result)
            running = False

        elif game.is_board_full():
            result = 'Ничья!'
            print(result)
            save_result(result)
            running = False

        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == '__main__':
    main()
