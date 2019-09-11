import curses
from models.maze import Maze


def main(screen):
    maze_obj = Maze(15, 15)
    maze_obj.generate_board()

    maze_obj.place_items()

    # Turn off cursor blinking
    curses.curs_set(0)

    render_maze(screen, maze_obj)

    while 1:
        key = screen.getch()

        if key == curses.KEY_UP:
            maze_obj.move_mg(maze_obj.DIRECTION_UP)
            render_maze(screen, maze_obj)

        elif key == curses.KEY_DOWN:
            maze_obj.move_mg(maze_obj.DIRECTION_DOWN)
            render_maze(screen, maze_obj)

        elif key == curses.KEY_LEFT:
            maze_obj.move_mg(maze_obj.DIRECTION_LEFT)
            render_maze(screen, maze_obj)

        elif key == curses.KEY_RIGHT:
            maze_obj.move_mg(maze_obj.DIRECTION_RIGHT)
            render_maze(screen, maze_obj)

        elif key == curses.KEY_ENTER or key in [10, 13]:
            # If user press enter, exit the program
            exit()


def render_maze(screen, maze: Maze):
    if not (maze.get_game_over() or maze.get_game_won()):
        for x in range(len(maze.board)):
            for y in range(len(maze.board[x])):
                screen.addstr(y, x, maze.board[y][x])

        screen.addstr(maze.get_mg_xy_position()[1], maze.get_mg_xy_position()[0], '.')

        if not maze.get_a_collected():
            screen.addstr(maze.get_a_xy_position()[1], maze.get_a_xy_position()[0], 'A')
        else:
            screen.addstr(20, 0, 'A item collected')

        if not maze.get_b_collected():
            screen.addstr(maze.get_b_xy_position()[1], maze.get_b_xy_position()[0], 'B')
        else:
            screen.addstr(21, 0, 'B item collected')

    elif maze.get_game_over():
        screen.clear()
        screen.addstr(1, 1, 'Game over')

    elif maze.get_game_won():
        screen.clear()
        screen.addstr(1, 1, 'You win! Congrats!')


if __name__ == '__main__':
    curses.wrapper(main)
