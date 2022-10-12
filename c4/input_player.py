from global_functions import *

class InputPlayer:
    
    def __init__(self):
        self.player_number = None
  
    def set_player_number(self, n):
        self.player_number = n

    def choose_move(self, state):
        
        print_board(state)
        
        answer = input(f'\nYou are player {self.player_number}.\nIn which column do you want to place a piece? ')

        if answer in '1234567':
            choice = int(answer) - 1
        else:
            print('That move is not valid! Please try again.')
            return self.choose_move(state)

        if choice not in get_choices(state):
            print('That move is not valid! Please try again.')
            return self.choose_move(state)
        
        return choice

    def update_state(self, state):
        pass