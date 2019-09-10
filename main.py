import curses
from models.maze import Maze


def main(screen):
    maze_obj = Maze(15, 15)
    maze_obj.generate_board()

    maze_obj.place_items()

    # turn off cursor blinking
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
            # if user press enter, exit the program
            exit()


def render_maze(screen, maze: Maze):
    for x in range(len(maze.board)):
        for y in range(len(maze.board[x])):
            screen.addstr(y, x, maze.board[y][x])

    screen.addstr(maze.get_mg_xy_position()[1], maze.get_mg_xy_position()[0], '.')
    screen.addstr(maze.get_a_xy_position()[1], maze.get_a_xy_position()[0], 'A')
    screen.addstr(maze.get_b_xy_position()[1], maze.get_b_xy_position()[0], 'B')


if __name__ == '__main__':
    curses.wrapper(main)
