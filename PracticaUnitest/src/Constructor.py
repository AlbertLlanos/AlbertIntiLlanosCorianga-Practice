class Average():

    def __init__(self, high, less, avg):
        self.__higher = high
        self.__lesser = less
        self.__average = avg

    def get_higher(self):
        return self.__higher

    def get_lesser(self):
        return self.__lesser

    def get_average(self):
        return self.__average