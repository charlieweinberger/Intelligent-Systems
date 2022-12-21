import sys
sys.path.append("ttt")
from tic_tac_toe import *
from random_player import *
from nn_player import *
from np_player import *

def run_ttt(game_type, num_games_per_player):

    score = {game_type[0]: 0, game_type[1]: 0, 'tie': 0}

    for i in range(2):
        for j in range(num_games_per_player):

            print(f'Running game {j + i*num_games_per_player + 1}...')

            players = []
            for player in game_type:
                if player == 'random':       players.append(RandomPlayer())
                if player == 'near perfect': players.append(NearPerfectPlayer())
                if player == 'neural net':   players.append(NeuralNetPlayer())

            if i % 2 == 1: players = players[::-1]        

            game = TicTacToe(players)
            game.run_to_completion()

            winner_map = {
                1: game_type[i],
                2: game_type[1 - i],
                'tie': 'tie'
            }

            score[winner_map[game.winner]] += 1

    return score

game_type = ['random', 'near perfect']
num_games_per_player = 500

print(run_ttt(game_type, num_games_per_player))