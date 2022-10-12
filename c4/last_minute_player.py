
import copy, random
from global_functions import *

class LastMinutePlayer:
    
    def __init__(self):
        self.player_number = None
  
    def set_player_number(self, n):
        self.player_number = n

    def choose_move(self, state):
        
        moves = get_choices(state)

        for move in moves:

            capture_win_state = copy.deepcopy(state)
            block_loss_state = copy.deepcopy(state)

            for i in range(5, -1, -1):
                if state[i][move] == None:
                    capture_win_state[i][move] = self.player_number
                    block_loss_state[i][move] = 3 - self.player_number
                    break

            if check_for_winner(capture_win_state) or check_for_winner(block_loss_state):
                return move

        return random.choice(moves)

    def update_state(self, state):
        pass