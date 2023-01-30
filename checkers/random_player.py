import random, sys
sys.path.append("./global_functions.py")
from global_functions import *

class RandomPlayer:

    def __init__(self):
        self.player_num = None
  
    def set_player_num(self, n):
        self.player_num = n

    def choose_move(self, state, moves):

        print(f'\nPlayer {self.player_num}\'s turn!')

        print_state(state)

        move = random.choice(moves)

        print(f'\nPlayer {self.player_num}\'s move: {print_move(move)}\n\n-----------------------------------------------------------------')

        return move