import numpy as np
from mastermind.master import master

class board():
    def __init__(self, code_size, number_of_colors):
        self.code_size = code_size
        self.number_of_colors = number_of_colors
        self.secret_code = np.random.randint(number_of_colors, size= code_size)
        self.try_list = []
        self.master = master()
        self.issolved = False

    def __init__(self, code_size, number_of_colors, secret_code):
        self.code_size = code_size
        self.number_of_colors = number_of_colors
        self.secret_code = secret_code
        self.try_list = []
        self.master = master()
        self.issolved = False 

    def add_full_try(self, guess, evaluation):
        self.try_list.append([guess, evaluation])

    def add_try(self, guess):
        if self.is_guess_format_valid(guess):
            self.try_list.append([guess, self.master.evaluate_guess(guess, self.secret_code)])
            if self.try_list[-1][1] == self.code_size * [2]:
                self.issolved = True
                print('Board solved in ' + str(len(self.try_list)) + ' tries!')
        else:
            print('guess not valid')

    def is_guess_format_valid(self, guess):
        return (len(guess) == self.code_size and max(guess) < self.number_of_colors and min(guess) >= 0)
    
    def set_secret(self, secret_code):
        if self.is_guess_format_valid(secret_code):
            self.secret_code = secret_code
        else:
            print('secret not valid')


