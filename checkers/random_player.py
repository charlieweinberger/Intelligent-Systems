import random, sys
sys.path.append("./global_functions.py")
from global_functions import *

class RandomPlayer:

    def __init__(self, print_data=False):
        self.player_number = None
        self.print_data = print_data
 
    def set_player_number(self, n):
        self.player_number = n

    def choose_move(self, state, moves):

        if (self.print_data):
            print(f'\nPlayer {self.player_number}\'s turn!')
            print_state(state)

        move = random.choice(moves)

        if (self.print_data):
            print(f'\nPlayer {self.player_number}\'s move: {print_move(move)}\n\n-----------------------------------------------------------------')

        return move