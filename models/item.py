class Item:
    def __init__(self, xy_position: tuple):
        """
        Created a new object that MacGyver must collect on maze board
        :param xy_position: tuple containing object XY position on maze board
        """
        self.__xy_position = xy_position
        self.__collected = False

    def collect(self):
        """
        Marks an object as collected
        :return:
        """
        self.__collected = True

    def collected(self) -> bool:
        """
        Returns collected state
        :return: true if collected, false otherwise
        """
        return self.__collected

    def get_position(self) -> (int, int):
        """
        Returns object XY position on maze board
        :return: tuple containing object XY position on maze board
        """
        return self.__xy_position
