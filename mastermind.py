import random


class Game:
    def __init__(self, colour=6, pos=4):
        self.__colour = colour
        self.__pos = pos
        self.__ans = []
        for i in range(pos):
            self.__ans.append(int(random.randint(1, colour)))

    @property
    def guess(self):
        return self.__guess

    @guess.setter
    def guess(self, guess=int):
        self.__guess = list(guess)

    @property
    def check_colour(self):
        return self.__colour

    @check_colour.setter
    def check_colour(self, colour):
        self.__colour = colour
        if 1 > colour > 8:
            raise ValueError('colour can only be 1-8')

    @property
    def check_pos(self):
        return self.__pos

    @check_pos.setter
    def check_pos(self, pos):
        self.__pos = pos
        if 1 > pos > 10:
            raise ValueError('positions can only be 1-10')

    def display(self):
        print(f"Playing Mastermind with {self.x} colour and {self.y} positions")


start = Game()
start.display()
