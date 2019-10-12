class MacGyver:
    DIRECTION_UP = (0, -1)
    DIRECTION_RIGHT = (1, 0)
    DIRECTION_DOWN = (0, 1)
    DIRECTION_LEFT = (-1, 0)

    def __init__(self, xy_position: tuple):
        """
        Creates a MacGyver object with its position on maze board
        :param xy_position: tuple containing MacGyver XY position on maze board
        """
        self.__xy_position = xy_position

    def move(self, direction: tuple):
        """
        Moves MacGyver on maze board
        :param direction: must be DIRECTION_UP or DIRECTION_RIGHT or DIRECTION_DOWN or DIRECTION_LEFT
        :return:
        """
        self.__xy_position = tuple(map(lambda x, y: x + y, self.__xy_position, direction))

    def get_position(self) -> (int, int):
        """
        Returns MacGyver XY position on maze board
        :return: tuple containing MacGyver XY position on maze board
        """
        return self.__xy_position
