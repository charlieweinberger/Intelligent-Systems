from ttt import *
from random_player import *
from input_player import *
from minimax_player import *

game_type = ['input', 'minimax'] # ['random', 'input', 'minimax']

score = {1: 0, 2: 0, 'tie':0}

for i in range(50):

    players = []
    for player in game_type:
        if player == 'random':  players.append(RandomPlayer())
        if player == 'input':   players.append(InputPlayer())
        if player == 'minimax': players.append(MinimaxPlayer())
    
    game = TicTacToe(players, second_player_first = (i % 2 == 1), see_board=('input' in game_type))
    game.run_to_completion()
    score[game.winner] += 1
    print(f'Score after game {i}: {score}')

print(score)