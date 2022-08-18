from ttt import *
from random_player import *
from input_player import *
from minimax_player import *

game_type = ['random', 'random'] # ['random', 'input', 'minimax']

num_wins = {1: 0, 2: 0, 'tie':0}

for i in range(100):
    
    players = [RandomPlayer(), RandomPlayer()]

    players = []
    for player in game_type:
        if player == 'random':  players.append(RandomPlayer())
        if player == 'input':   players.append(InputPlayer())
        if player == 'minimax': players.append(MinimaxPlayer())
    
    game = TicTacToe(players, second_player_first = (i % 2 == 1))
    game.run_to_completion()
    num_wins[game.winner] += 1

print(num_wins)

# game = TicTacToe(players, second_player_first=False, see_board=True)
# game.run_to_completion()
# game.print_board()
# print("\nwinner:", game.winner)