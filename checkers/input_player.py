import random

class InputPlayer:

    def __init__(self):
        self.player_num = None
  
    def set_player_num(self, n):
        self.player_num = n

    def choose_move(self, state, moves):
        
        print(f'\nYour turn! You are player {self.player_num}\n')

        for row in state:
            print(row)
        
        print('\nPossible moves:')
        for move in moves:
            print(move)
        
        move_index = int(input("\nWhat move do you want to play? Input the index of the move. "))
        move = moves[move_index]

        print(f'\nYour move: {move}\n\n-----------------------------------------------------------------')

        return move