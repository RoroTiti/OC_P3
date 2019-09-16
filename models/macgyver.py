class MacGyver:
    DIRECTION_UP = (0, -1)
    DIRECTION_RIGHT = (1, 0)
    DIRECTION_DOWN = (0, 1)
    DIRECTION_LEFT = (-1, 0)

    def __init__(self, xy_position: tuple):
        self.__xy_position = xy_position

    def move(self, direction: tuple):
        self.__xy_position = tuple(map(lambda x, y: x + y, self.__xy_position, direction))

    def get_position(self) -> (int, int):
        return self.__xy_position
