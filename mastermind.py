import random, copy


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
        Game(self.__pos, self.__colour)

    @property
    def check_pos(self):
        return self.__pos

    @check_pos.setter
    def check_pos(self, pos):
        self.__pos = pos
        if 1 > pos > 10:
            raise ValueError('positions can only be 1-10')
        Game(self.__pos, self.__colour)

    @property
    def give_hint(self):
        hint = []
        list = []
        if len(self.__guess) != len(self.__ans):
            raise AssertionError \
                ('Your guess must be the same length as your puzzle length')
        guess_temp = copy.deepcopy(self.__guess)
        answer_temp = copy.deepcopy(self.__ans)
        for i in range(len(self.__guess)):
            if guess_temp[i] == answer_temp[i]:
                hint.append('*')
                list.append(i)
        list.sort()
        list.reverse()
        for i in list:
            guess_temp.pop(i)
            answer_temp.pop(i)
        for i in range(len(guess_temp)):
            if guess_temp[i] in answer_temp:
                hint.append('o')
                answer_temp.remove(guess_temp[i])
        return ''.join(hint)

    def display(self):
        print(f"Playing Mastermind with {self.__colour} colour and {self.__pos} positions")
        turn_count = 0
        while True:
            turn_count += 1
            self.__guess = input('Enter your guess: ')
            if self.__guess == 'giveup':
                print(f"The answer is {self.__ans}")
                break
            print(self.give_hint)
            if self.give_hint == ('*' * self.__pos):
                print(f"You solve it after {turn_count} rounds")
                break


start = Game()
end = False
while end == False:
    print('Game Options')
    print('1. Start the game')
    print('2. Set puzzle length')
    print('3. Set the amount of colors')
    print('4. Quit')
    op = int(input('Enter your option: '))
    if op == 1:
        start.display()
        again = input('Play Again? (y/n): ')
        if again == 'n':
            end = True
    elif op == 2:
        start.check_pos = int(input('Set the length form 1 to 10: '))
    elif op == 3:
        start.check_colour = int(input('Set the colors from 1 to 8: '))
    elif op == 4:
        end = True
