from tic_tac_toe import *
from game_tree import *
from reduced_search_game_tree import *
from random_player import *
from input_player import *
from minimax_player import *
from heuristic_minimax_player import *

# change these variables

game_type = ['random', '3-ply']
num_games_if_no_human = 10

# don't change below

human_is_playing = 'input' in game_type
num_games = 1 if human_is_playing else num_games_if_no_human

score = {game_type[0]: 0, game_type[1]: 0, 'tie': 0}

for i in range(2):

    if human_is_playing and i > 0: continue

    for j in range(num_games):

        if human_is_playing and j > 0: continue

        print(f'\nRunning game {j + i*num_games_if_no_human + 1}...')

        players = []
        for player in game_type:
            if player == 'random':  players.append(RandomPlayer())
            if player == 'input':   players.append(InputPlayer())
            if player == 'minimax': players.append(MinimaxPlayer())
            if player[1:] == '-ply': players.append(HeuristicMinimaxPlayer(int(player[0])))

        if i % 2 == 1: players = players[::-1]        

        game = TicTacToe(players, show_board = human_is_playing)
        game.run_to_completion()

        winner_map = {
            1: game_type[i],
            2: game_type[1 - i],
            'tie': 'tie'
        }

        score[winner_map[game.winner]] += 1

print(score)