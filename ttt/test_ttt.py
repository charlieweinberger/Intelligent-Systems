from ttt import *
from random_player import *
from input_player import *
from minimax_player import *

game_type = ['random', 'minimax'] # ['random', 'input', 'minimax']

num_wins = {1: 0, 2: 0, 'tie':0}

for i in range(50):
    
    players = []

    players = []
    for player in game_type:
        if player == 'random':  players.append(RandomPlayer())
        if player == 'input':   players.append(InputPlayer())
        if player == 'minimax': players.append(MinimaxPlayer())
    
    game = TicTacToe(players, second_player_first = (i % 2 == 1), see_board=True)
    game.run_to_completion()
    num_wins[game.winner] += 1
    print(f'game {i} winner: {game.winner}')

print(num_wins)
