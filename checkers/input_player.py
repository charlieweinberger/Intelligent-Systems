import random, sys
sys.path.append("./global_functions.py")
from global_functions import *

class InputPlayer:

    def __init__(self, print_data=False):
        self.player_number = None
        self.print_data = print_data
  
    def set_player_number(self, n):
        self.player_number = n

    def choose_move(self, state, moves):

        print(f'\nPlayer {self.player_number}\'s turn!')

        print_state(state)
        print_moves(moves)

        print('')

        move_index = self.input_move(moves)
        move = moves[move_index]

        print(f'\nYour move: {print_move(move)}\n\n-----------------------------------------------------------------')

        return move
    
    def input_move(self, moves):

        player_input = input("What move do you want to play? Input the index of the move. ")

        if player_input in [str(i) for i in range(len(moves))]:
            return int(player_input)
        else:
            print("That move is invalid. Please choose another move. ")
            return self.input_move(moves)