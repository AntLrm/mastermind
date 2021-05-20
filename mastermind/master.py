import numpy as np

class master():
    def __init__(self):
        pass

    def evaluate_guess(self, guess, code):
        matches_matrix = self.get_match_matrix(guess, code)
        nbr_of_matches = sum(matches_matrix)
        remaining_guess = self.remove_matches(guess, matches_matrix)
        remaining_secret = self.remove_matches(code, matches_matrix)
        nbr_of_misplaced = self.get_nbr_of_common(remaining_guess, remaining_secret)
        return nbr_of_matches*[2] + nbr_of_misplaced*[1] + (len(guess)-nbr_of_misplaced-nbr_of_matches)*[0]

    @staticmethod
    def get_match_matrix(list1, list2):
        match_matrix = len(list1) * [0]
        for i in range(len(list1)):
            if list1[i] == list2[i]:
                match_matrix[i] = 1
        return match_matrix
    
    @staticmethod
    def remove_matches(input_list, match_matrix):
        return [input_list[i] for i in range(len(match_matrix)) if match_matrix[i] == 0]
        

    @staticmethod
    def get_nbr_of_common(list1, list2):
        number_of_common = 0
        i = 0
        while i < len(list1):
            try:
                common_index = list2.index(list1[i])
                list2.pop(common_index)
                list1.pop(i)
                number_of_common +=1
            except ValueError:
                i += 1
        return number_of_common