import random

class Game:
    def __init__(self):
        self.secret_number = random.randint(1, 10)
        self.num_guesses = 0

    def guess(self, number):
        if number == self.secret_number:
            return True
        else:
            self.num_guesses += 1
            return False

    def is_over(self):
        return self.num_guesses == 10

    def get_num_guesses(self):
        return self.num_guesses

    def get_secret_number(self):
        return self.secret_number

def main():
    game = Game()

    while not game.is_over():
        guess = int(input("Guess a number between 1 and 10: "))

        if game.guess(guess):
            print("Correct!")
            break
        else:
            print("Incorrect. You have {} guesses left.".format(10 - game.get_num_guesses()))

    if game.is_over():
        print("Game over. The secret number was {}.".format(game.get_secret_number()))

if __name__ == "__main__":
    main()
