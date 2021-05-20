import numpy as np
from mastermind.master import master
#from mastermind.board import board


class solver():
    def __init__(self):
        self.master = master()
        self.guess_set = []
            
    def solve(self, board):
        while board.issolved == False:
            board.add_try(self.next_guess(board))
        if board.issolved:
            print('Solution is ' + str(board.try_list[-1][0]))


    def next_guess(self, board):
        if board.try_list == []:
            return self.get_first_guess(board.code_size, board.number_of_colors)
        else:
            self.set_guess_set(board)
            return self.guess_set[np.random.randint(len(self.guess_set))]


    def get_first_guess(self, code_size, nbr_color):
        if nbr_color > 0:
            return int(code_size/2)*[0] + (code_size - int(code_size/2))*[1]
        elif nbr_color == 0:
            return code_size*[0]

    def set_guess_set(self, board):
        if self.guess_set == []:
            self.initialize_combinaisons(board)         
        else:
            self.reduce_set(board.try_list[-1])
    
    
    def initialize_combinaisons(self, board):
        self.guess_set = self.combinaisons(board.code_size, board.number_of_colors)
        if board.try_list != []:
            for mtry in board.try_list:
                self.reduce_set(mtry)
        
    def reduce_set(self, mtry):
        self.guess_set = [possible_try for possible_try in self.guess_set if self.master.evaluate_guess(possible_try, mtry[0]) == mtry[1]]

    def combinaisons(self, code_size, number_of_colors):
        if code_size == 1:
            return [[x] for x in range(number_of_colors)]
        else:
            return [[i] + x for x in self.combinaisons(code_size - 1, number_of_colors) for i in range(number_of_colors)]

