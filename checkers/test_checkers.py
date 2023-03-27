from checkers import *
from random_player import *
from input_player import *
from intelligent_player import *

# EDIT THIS

# combine the 4 if statements into 1 code segment

game_mode = 'intelligent' # random, input, intelligent, custom
num_random_games = 100
print_data_for_random = False

# DON'T EDIT THIS

if game_mode == 'random': # random players

    print(f"Running {num_random_games} random games...")

    score = { 1: 0, 2: 0, 'tie': 0 }

    for i in range(num_random_games):
        players = [RandomPlayer(print_data_for_random), RandomPlayer(print_data_for_random)]
        game = Checkers(players)
        game.run_to_completion()
        score[game.winner] += 1

    print(f"{score = }")

elif game_mode == 'input': # input players

    # Move order to test chain capturing: 00174263

    players = [InputPlayer(), InputPlayer()]
    game = Checkers(players)
    game.run_to_completion()

    if game.winner == "tie":
        print("\nTie game!\n")
    else:
        print(f'\nWinner: Player {game.winner}!\n')

elif game_mode == 'intelligent': # intelligent player

    print(f"\nRunning {num_random_games} game{'s' if num_random_games != 1 else ''} of intelligent vs. random player...\n")

    score = { 1: 0, 2: 0, 'tie': 0 }

    for i in range(num_random_games):
        players = [IntelligentPlayer(print_data_for_random), RandomPlayer(print_data_for_random)]
        game = Checkers(players)
        game.run_to_completion()
        score[game.winner] += 1

    print(f"{score = }")

elif game_mode == 'custom': # custom game state

    custom_state = [
        [ 0,  0,  0,  0,  0,  0,  0,  0],
        [ 0,  0,  0,  0,  1,  0,  0,  0],
        [ 0,  0,  0,  0,  0,  0,  0,  0],
        [ 0,  0,  0,  0,  0,  0,  0,  0],
        [ 0, -2,  0,  2,  0, -2,  0,  0],
        [ 0,  0,  0,  0,  0,  0,  0,  0],
        [ 0, -2,  0,  0,  0,  0,  0,  0],
        [-1,  0,  0,  0,  0,  0,  0,  0],
    ]

    players = [InputPlayer(), InputPlayer()]
    game = Checkers(players)
    possible_moves = game.get_possible_moves(game.players[0], custom_state)

    print_state(custom_state)
    print_moves(possible_moves)