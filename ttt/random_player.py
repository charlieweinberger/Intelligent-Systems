import random

class RandomPlayer:

    def __init__(self):
        self.player_number = None
  
    def set_player_number(self, n):
        self.player_number = n

    def update_state(self, state):
        pass
  
    def choose_move(self, state):
        choices = [(i, j) for i in range(3) for j in range(3) if state[i][j] == None]
        choice = random.choice(choices)
        # print(f'random player class: {choice}')
        return choice