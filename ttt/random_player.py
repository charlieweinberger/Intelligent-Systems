import random
import math

class RandomPlayer:
    def __init__(self):
        self.player_number = None
  
    def set_player_number(self, n):
        self.player_number = n
  
    def update_state(self, state):
        pass

    def choose_move(self, choices):
        return random.choice(choices)