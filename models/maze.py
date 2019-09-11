from random import shuffle, randint
from typing import List


class Maze:
    DIRECTION_UP = 1
    DIRECTION_RIGHT = 2
    DIRECTION_DOWN = 3
    DIRECTION_LEFT = 4

    def __init__(self, width: int, height: int):
        self.width: int = width
        self.height: int = height
        self.board = [['' for _ in range(self.width)] for _ in range(self.height)]
        self.__mg_xy_position = (0, 1)
        self.__a_xy_position = (0, 0)
        self.__a_collected = False
        self.__b_xy_position = (0, 0)
        self.__b_collected = False
        self.__game_won = False
        self.__game_over = False

    def generate_board(self):
        w: int = int((self.width - 1) / 2)
        h: int = int((self.height - 1) / 2)

        visited = [[False] * w + [True] for _ in range(h)] + [[True] * (w + True)]
        vertical = [["# "] * w + ['#'] for _ in range(h)] + [[]]
        horizontal = [["##"] * w + ['#'] for _ in range(h + 1)]

        def walk(board_x, board_y):
            visited[board_y][board_x] = True

            directions = [
                (board_x - 1, board_y),
                (board_x, board_y + 1),
                (board_x + 1, board_y),
                (board_x, board_y - 1)
            ]

            shuffle(directions)
            for (direction_x, direction_y) in directions:
                if visited[direction_y][direction_x]:
                    continue
                if direction_x == board_x:
                    horizontal[max(board_y, direction_y)][board_x] = "# "
                if direction_y == board_y:
                    vertical[board_y][max(board_x, direction_x)] = "  "
                walk(direction_x, direction_y)

        walk(0, 0)

        curr_y = 1

        for (a, b) in zip(horizontal, vertical):
            if a:
                self.board[curr_y - 1] = list(''.join(a))
                curr_y += 1
            if b:
                self.board[curr_y - 1] = list(''.join(b))
                curr_y += 1

        # Making the maze entry and exit
        self.board[1][0] = ' '

        # Placing the guardian
        self.board[self.height - 2][self.width - 1] = 'G'

    def place_items(self):
        # Step 0 : init
        free_blocks_xy_positions: List[(int, int)] = []

        # Step 1 : getting all empty blocks of board
        for y in range(len(self.board)):
            for x in range(len(self.board[y])):
                if self.board[y][x] == ' ':
                    free_blocks_xy_positions.append((x, y))

        # Shuffle the array to mix the positions
        shuffle(free_blocks_xy_positions)

        # Step 2 : choosing place of element A
        element_a_index = randint(0, len(free_blocks_xy_positions) // 2)
        self.__a_xy_position = free_blocks_xy_positions[element_a_index]

        # Step 3 : choosing place of element B
        element_b_index = randint(len(free_blocks_xy_positions) // 2, len(free_blocks_xy_positions) - 1)
        self.__b_xy_position = free_blocks_xy_positions[element_b_index]

    def move_mg(self, direction: int):
        if direction == self.DIRECTION_UP:
            if self.board[self.__mg_xy_position[1] - 1][self.__mg_xy_position[0]] == ' ':
                self.__mg_xy_position = (self.__mg_xy_position[0], self.__mg_xy_position[1] - 1)

        elif direction == self.DIRECTION_RIGHT:
            # This line prevents out of range exception at maze exit
            if self.__mg_xy_position[0] < len(self.board[0]) - 1:
                if self.board[self.__mg_xy_position[1]][self.__mg_xy_position[0] + 1] == 'G':
                    if self.get_a_collected() and self.get_b_collected():
                        self.__game_won = True
                    else:
                        self.__game_over = True

                elif self.board[self.__mg_xy_position[1]][self.__mg_xy_position[0] + 1] == ' ':
                    self.__mg_xy_position = (self.__mg_xy_position[0] + 1, self.__mg_xy_position[1])

        elif direction == self.DIRECTION_DOWN:
            if self.board[self.__mg_xy_position[1] + 1][self.__mg_xy_position[0]] == ' ':
                self.__mg_xy_position = (self.__mg_xy_position[0], self.__mg_xy_position[1] + 1)

        elif direction == self.DIRECTION_LEFT:
            if self.board[self.__mg_xy_position[1]][self.__mg_xy_position[0] - 1] == ' ':
                self.__mg_xy_position = (self.__mg_xy_position[0] - 1, self.__mg_xy_position[1])

        if self.__mg_xy_position == self.__a_xy_position:
            self.__a_collected = True

        if self.__mg_xy_position == self.__b_xy_position:
            self.__b_collected = True

    def get_mg_xy_position(self) -> (int, int):
        return self.__mg_xy_position

    def get_a_xy_position(self) -> (int, int):
        return self.__a_xy_position

    def get_a_collected(self) -> bool:
        return self.__a_collected

    def get_b_xy_position(self) -> (int, int):
        return self.__b_xy_position

    def get_b_collected(self) -> bool:
        return self.__b_collected

    def get_game_won(self) -> bool:
        return self.__game_won

    def get_game_over(self) -> bool:
        return self.__game_over
