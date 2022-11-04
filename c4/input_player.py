from global_functions import *

class InputPlayer:
    
    def __init__(self, ply=None):
        self.player_number = None
  
    def set_player_number(self, n):
        self.player_number = n

    def choose_move(self, state, moves):
        
        print_board(state)
        
        answer = input(f'\nYou are player {self.player_number}.\nIn which column do you want to place a piece? ')

        if answer in '1234567':
            move = int(answer) - 1
        else:
            print('That move is not valid! Please try again.')
            return self.choose_move(state, moves)

        if move not in get_moves(state):
            print('That move is not valid! Please try again.')
            return self.choose_move(state, moves)
        
        return move

    def update_state(self, state):
        pass