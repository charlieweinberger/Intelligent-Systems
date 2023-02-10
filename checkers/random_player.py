import random, sys
sys.path.append("./global_functions.py")
from global_functions import *

class RandomPlayer:

    def __init__(self, print_data=False):
        self.player_num = None
        self.print_data = print_data
 
    def set_player_num(self, n):
        self.player_num = n

    def choose_move(self, state, moves, first_time):

        if (self.print_data):
            print(f'\nPlayer {self.player_num}\'s turn!')
            print_state(state)

        move = random.choice(moves)

        if (self.print_data):
            print(f'\nPlayer {self.player_num}\'s move: {print_move(move)}\n\n-----------------------------------------------------------------')

        return move