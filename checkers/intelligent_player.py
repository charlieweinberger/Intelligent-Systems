import random, sys
sys.path.append("./global_functions.py")
from global_functions import *

class IntelligentPlayer:

    def __init__(self, print_data=False):
        self.player_number = None
        self.print_data = print_data
 
    def set_player_number(self, n):
        self.player_number = n

    def choose_move(self, state, moves):
        
        move = self.get_move(state, moves)

        if (self.print_data):
            player_color = "blue" if self.player_number == 1 else "red"
            print_state(state)
            print(f"\nIntelligent player's turn!")
            print(f"The intelligent player is player {self.player_number} ({player_color}).")
            print(f"Chosen move: {print_move(move)}\n")

        return move
    
    def get_move(self, state, moves):
        
        capture_move = moves[0]
        
        for move in moves:
            if len(move[2]) > len(capture_move[2]):
                capture_move = move
        
        if len(capture_move[2]) != 0:
            return capture_move
        
        return random.choice(moves)