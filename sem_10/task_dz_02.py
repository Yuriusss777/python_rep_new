# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать “больше” или “меньше” после каждой попытки.


class NumberGame:
    def __init__(self):
        self.target_number = 0
        self.guesses_left = 10

    def generate_target_number(self):
        import random
        self.target_number = random.randint(0, 1000)

    def check_guess(self, guess):
        if guess == self.target_number:
            return "Поздравляю! Вы угадали число."
        elif guess < self.target_number:
            return "Загаданное число больше."
        else:
            return "Загаданное число меньше."

    def play(self):
        self.generate_target_number()
        print("У вас есть 10 попыток чтобы угадать число от 0 до 1000.")

        while self.guesses_left > 0:
            guess = int(input("\nВведите вашу догадку: "))
            result = self.check_guess(guess)
            print(result)

            self.guesses_left -= 1
            print("Осталось попыток:", self.guesses_left)

        print("\nИгра окончена. Загаданное число было:", self.target_number)


game = NumberGame()
game.play()
