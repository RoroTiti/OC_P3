class Object:
    def __init__(self, xy_position: tuple):
        self.__xy_position = xy_position
        self.__collected = False

    def collect(self):
        self.__collected = True

    def is_collected(self) -> bool:
        return self.__collected

    def get_position(self) -> (int, int):
        return self.__xy_position
