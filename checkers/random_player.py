import random

class RandomPlayer:

    def __init__(self):
        self.player_num = None
  
    def set_player_num(self, n):
        self.player_num = n

    def choose_move(self, state, moves):

        print(f'\nPlayer {self.player_num}\'s turn!\n')

        for row in state:
            print(row)

        move = random.choice(moves)

        print(f'\nPlayer {self.player_num}\'s move: {move}\n\n-----------------------------------------------------------------')

        return move