import sys, pickle
sys.path.append('ttt')
from tic_tac_toe import *
from random_player import *
from nn_player import *

final_gen_players = []

with open('fogel/nn_players.pickle', 'rb') as f:
    while True:
        try:
            final_gen_players.append(pickle.load(f))
        except EOFError:
            break

score = {'neural net': 0, 'random': 0, 'tie': 0}

for i in range(2):
    for j in range(25):

        print(f'Running game {j + i*25 + 1}...')

        players = [final_gen_players[0][0], RandomPlayer()]
        if i % 2 == 1: players = players[::-1]        

        game = TicTacToe(players)
        game.run_to_completion()

        winner_map = {
            1: 'neural net',
            2: 'random',
            'tie': 'tie'
        }

        score[winner_map[game.winner]] += 1

print(score)