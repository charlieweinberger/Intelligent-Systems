import random, sys
sys.path.append("./global_functions.py")
from global_functions import *

class InputPlayer:

    def __init__(self):
        self.player_num = None
  
    def set_player_num(self, n):
        self.player_num = n

    def choose_move(self, state, moves, first_time):
        
        print("\n--------------------------------------------------------------")

        if first_time:
            print(f'\nPlayer {self.player_num}\'s turn!')
        else:
            print("\nYou can move again!")

        print_state(state)
        print_moves(moves)

        print('')

        move_index = self.input_move(moves, first_time)
        move = moves[move_index]

        print(f'\nYour move: {print_move(move)}')

        return move
    
    def input_move(self, moves, first_time):

        if first_time:
            player_input = input("What move do you want to play? Input the index of the move. ")
        else:
            player_input = input("Input the index of the move you'd like to play. ")

        if player_input in [str(i) for i in range(len(moves))]:
            return int(player_input)
        else:
            print("That move is invalid. Please choose another move. ")
            return self.input_move(moves)