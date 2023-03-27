import random, sys
sys.path.append("./global_functions.py")
from global_functions import *

class InputPlayer:

    def __init__(self):
        self.player_number = None
  
    def set_player_number(self, n):
        self.player_number = n
    
    def choose_move(self, state, moves):

        print_state(state)

        print(f"\nInput player's turn!")

        player_color = "blue" if self.player_number == 1 else "red"
        print(f"The input player is player {self.player_number} ({player_color}).")

        print_moves(moves)

        move_index = self.input_move(moves)
        move = moves[move_index]

        print(f"Chosen move: {print_move(move)}\n")
        
        return move
    
    def get_move(self, state, moves):
        return random.choice(moves)

    def input_move(self, moves):

        player_input = input("\nWhat move do you want to play? Input the index of the move. ")

        if player_input in [str(i) for i in range(len(moves))]:
            return int(player_input)
        else:
            print("That move is invalid. Please choose another move. ")
            return self.input_move(moves)