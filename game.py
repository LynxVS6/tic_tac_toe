import pygame

from gameparts import Board
from interface import draw_lines, draw_figures, CELL_SIZE


def save_result(result):
    with open('results.txt', 'a', encoding='utf-8') as file:
        file.write(result + '\n')

def main():
    game = Board()
    current_player = 'X'
    running = True
    draw_lines()

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_y = event.pos[0]
                mouse_x = event.pos[1]

                clicked_row = mouse_x // CELL_SIZE
                clicked_col = mouse_y // CELL_SIZE

                if game.board[clicked_row][clicked_col] == ' ':
                    game.make_move(clicked_row, clicked_col, current_player)

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
                    draw_figures(game.board)

        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()
