import random
from global_functions import *

class Connect4:
    
    def __init__(self, players, show_board=False):

        self.players = players
        self.show_board = show_board
        self.set_player_numbers()
        self.state = [[None for _ in range(7)] for _ in range(6)]
        self.player_turn = 1
        self.winner = None

    def set_player_numbers(self): 
        self.players[0].set_player_number(1)
        self.players[1].set_player_number(2)

    def complete_round(self):
        
        for player in self.players:
            
            move = player.choose_move(self.state)
            update_state(self.state, move, player.player_number)
            
            for player in self.players:
                player.update_state(self.state)

            self.winner = check_for_winner(self.state)

            if self.winner:
                if self.show_board:
                    print_board(self.state)
                    print(f'Winner: Player {self.winner}\n')
                break
    
        self.player_turn += 1
        
    def run_to_completion(self):
        while self.winner == None:
            self.complete_round()