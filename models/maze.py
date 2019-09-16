from random import shuffle


class Maze:
    def __init__(self, width: int, height: int):
        self.width: int = width
        self.height: int = height
        self.__board = [['' for _ in range(self.width)] for _ in range(self.height)]

    def generate_board(self):
        """
        Generate a maze board
        Set the board property of the class
        """

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

        current_y = 1

        for (a, b) in zip(horizontal, vertical):
            if a:
                self.__board[current_y - 1] = list(''.join(a))
                current_y += 1
            if b:
                self.__board[current_y - 1] = list(''.join(b))
                current_y += 1

        # Making the maze entry and exit
        self.__board[1][0] = ' '

        # Placing the guardian
        self.__board[self.height - 2][self.width - 1] = 'G'

    def load_string(self, file_lines: [str]):
        current_y = 1

        for line in file_lines:
            self.__board[current_y - 1] = list(line)
            current_y += 1

    def get_board(self) -> [[str]]:
        return self.__board
