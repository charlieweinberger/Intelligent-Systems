from checkers import *
from random_player import *
from input_player import *

# EDIT THIS

game_mode = 'input' # random, input, custom
num_random_games = 100

# DON'T EDIT THIS

if game_mode == 'random': # random players

    score = { 1: 0, 2: 0, 'tie': 0 }

    for i in range(num_random_games):
        players = [RandomPlayer(), RandomPlayer()]
        game = Checkers(players)
        game.run_to_completion()
        score[game.winner] += 1

    print(score)

elif game_mode == 'input': # input players

    players = [InputPlayer(), InputPlayer()]
    game = Checkers(players)
    game.run_to_completion()

    print(game.winner)

elif game_mode == 'custom': # custom game state

    custom_state = [ # [0, 0, 0, 0, 0, 0, 0, 0],
        [ 0,  0,  0,  0,  0,  0,  0,  0],
        [ 0,  0,  0,  0,  0,  0,  0,  0],
        [ 0, -2,  0, -2,  0,  0,  0,  0],
        [ 0,  0,  0,  0,  0,  0,  0,  0],
        [ 0, -2,  0,  0,  0,  0,  0,  0],
        [-1,  0,  0,  0,  0,  0,  0,  0],
        [ 0,  0,  0,  0,  0,  0,  0,  0],
        [ 0,  0,  0,  0,  0,  0,  0,  0],
    ]

    players = [InputPlayer(), InputPlayer()]
    game = Checkers(players)
    possible_moves = game.get_possible_moves(game.players[0], custom_state)

    print('\nstate:')
    for row in custom_state:
        print(row)

    print('\npossible moves:')
    for move in possible_moves:
        print(move)