from random import shuffle, randint

import constants
from models.macgyver import MacGyver
from models.maze import Maze
from models.item import Item


class Controller:
    DIRECTION_UP = 1
    DIRECTION_RIGHT = 2
    DIRECTION_DOWN = 3
    DIRECTION_LEFT = 4

    def __init__(self):
        """
        Creates a full maze board context
        """
        self.__maze = Maze(constants.MAZE_WIDTH, constants.MAZE_HEIGHT)
        self.__objects = []
        self.__game_won = False
        self.__game_over = False

        file = open('maze.mz', 'r')
        lines = file.readlines()
        self.__maze.load_string(lines)
        file.close()

        self.__macgyver = MacGyver(self.__maze.get_entrance_position())

        free_blocks_xy_positions: [(int, int)] = []

        # Getting all empty blocks of board
        for x in range(constants.MAZE_WIDTH):
            for y in range(constants.MAZE_HEIGHT):
                if self.__maze.get_board()[y][x] == ' ':
                    free_blocks_xy_positions.append((x, y))

        # Popping first and last list item (MacGyver and Guardian positions respectively)
        free_blocks_xy_positions.pop(0)
        free_blocks_xy_positions.pop(len(free_blocks_xy_positions) - 1)

        # Shuffling the array to mix the positions
        shuffle(free_blocks_xy_positions)

        # Randomize zones
        zone_length = (len(free_blocks_xy_positions) - 1) // constants.OBJECTS

        # Choosing place of each object
        for index in range(constants.OBJECTS):
            element_index = randint(index * zone_length, (index + 1) * zone_length)
            self.__objects.append(Item(free_blocks_xy_positions[element_index]))

    def move_mg(self, direction: int):
        """
        Handles the movement of MacGyver on the board
        :param direction: must be DIRECTION_UP or DIRECTION_RIGHT or DIRECTION_DOWN or DIRECTION_LEFT
        """
        board = self.__maze.get_board()
        macgyver = self.__macgyver

        check_final_state = False

        if direction == self.DIRECTION_UP:
            if macgyver.get_position()[1] > 0:
                content = board[macgyver.get_position()[1] - 1][macgyver.get_position()[0]]

                if content == ' ':
                    macgyver.move(macgyver.DIRECTION_UP)
                elif content == 'G':
                    check_final_state = True

        elif direction == self.DIRECTION_RIGHT:
            if macgyver.get_position()[0] < constants.MAZE_WIDTH - 1:
                content = board[macgyver.get_position()[1]][macgyver.get_position()[0] + 1]

                if content == ' ':
                    macgyver.move(macgyver.DIRECTION_RIGHT)
                elif content == 'G':
                    check_final_state = True

        elif direction == self.DIRECTION_DOWN:
            if macgyver.get_position()[1] < constants.MAZE_HEIGHT - 1:
                content = board[macgyver.get_position()[1] + 1][macgyver.get_position()[0]]

                if content == ' ':
                    macgyver.move(macgyver.DIRECTION_DOWN)
                elif content == 'G':
                    check_final_state = True

        elif direction == self.DIRECTION_LEFT:
            if macgyver.get_position()[0] > 0:
                content = board[macgyver.get_position()[1]][macgyver.get_position()[0] - 1]

                if content == ' ':
                    macgyver.move(macgyver.DIRECTION_LEFT)
                if content == 'G':
                    check_final_state = True

        for obj in self.__objects:
            if macgyver.get_position() == obj.get_position():
                obj.collect()

        if check_final_state:
            objects_collected = []
            for obj in self.__objects:
                objects_collected.append(obj.collected())
            self.__game_won = all(objects_collected)
            self.__game_over = not all(objects_collected)

    def get_maze(self) -> Maze:
        """
        Returns the maze object
        :return: the maze object
        """
        return self.__maze

    def get_macgyver(self) -> MacGyver:
        """
        Returns the MacGyver object
        :return: the MacGyver object
        """
        return self.__macgyver

    def get_objects(self) -> [Item]:
        """
        Returns the list of objects to collect
        :return: the list of objects to collect
        """
        return self.__objects

    def get_game_over(self) -> bool:
        """
        Returns game over state
        :return: true if game over, false otherwise
        """
        return self.__game_over

    def get_game_won(self) -> bool:
        """
        Return game won state
        :return: true if game is won, false otherwise
        """
        return self.__game_won
