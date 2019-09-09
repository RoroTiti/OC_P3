from random import shuffle
import curses


def make_maze(w=7, h=7):
    visited = [[False] * w + [True] for _ in range(h)] + [[True] * (w + True)]
    vertical = [["# "] * w + ['#'] for _ in range(h)] + [[]]
    horizontal = [["##"] * w + ['#'] for _ in range(h + 1)]

    def walk(board_x, board_y):
        visited[board_y][board_x] = True

        directions = [(board_x - 1, board_y), (board_x, board_y + 1), (board_x + 1, board_y), (board_x, board_y - 1)]
        shuffle(directions)
        for (direction_x, direction_y) in directions:
            if visited[direction_y][direction_x]:
                continue
            if direction_x == board_x:
                horizontal[max(board_y, direction_y)][board_x] = "# "
            if direction_y == board_y:
                vertical[board_y][max(board_x, direction_x)] = "  "
            walk(direction_x, direction_y)

    # walk(randrange(w), randrange(h))
    walk(0, 0)

    string = ""
    for (a, b) in zip(horizontal, vertical):
        if a:
            string += ''.join(a + ['\n'])
        if b:
            string += ''.join(b + ['\n'])

    string = string[:- 1]

    lines = string.split('\n')

    maze = [['' for _ in range(len(lines[0]) + 2)] for _ in range(len(lines))]

    curr_y = 1

    for line in lines:
        maze[curr_y - 1] = list(line)
        curr_y += 1

    # making the maze input and output
    maze[1][0] = ' '
    maze[len(lines[0]) - 2][len(lines) - 1] = ' '

    return maze


def main(screen):
    maze = make_maze()

    # turn off cursor blinking
    curses.curs_set(0)

    for x in range(len(maze)):
        for y in range(len(maze[x])):
            screen.addstr(y, x, maze[y][x])

    # X / Y position
    dot_pos = (0, 1)

    screen.addstr(dot_pos[1], dot_pos[0], '.')

    screen.refresh()

    while 1:
        key = screen.getch()

        if key == curses.KEY_UP:
            if not maze[dot_pos[1] - 1][dot_pos[0]] == '#':
                screen.addstr(dot_pos[1], dot_pos[0], ' ')
                dot_pos = (dot_pos[0], dot_pos[1] - 1)
                screen.addstr(dot_pos[1], dot_pos[0], '.')

        elif key == curses.KEY_DOWN:
            if not maze[dot_pos[1] + 1][dot_pos[0]] == '#':
                screen.addstr(dot_pos[1], dot_pos[0], ' ')
                dot_pos = (dot_pos[0], dot_pos[1] + 1)
                screen.addstr(dot_pos[1], dot_pos[0], '.')

        elif key == curses.KEY_LEFT:
            if not maze[dot_pos[1]][dot_pos[0] - 1] == '#':
                screen.addstr(dot_pos[1], dot_pos[0], ' ')
                dot_pos = (dot_pos[0] - 1, dot_pos[1])
                screen.addstr(dot_pos[1], dot_pos[0], '.')

        elif key == curses.KEY_RIGHT:
            if not maze[dot_pos[1]][dot_pos[0] + 1] == '#':
                screen.addstr(dot_pos[1], dot_pos[0], ' ')
                dot_pos = (dot_pos[0] + 1, dot_pos[1])
                screen.addstr(dot_pos[1], dot_pos[0], '.')

        elif key == curses.KEY_ENTER or key in [10, 13]:
            # if user selected last row, exit the program
            exit()


if __name__ == '__main__':
    curses.wrapper(main)
