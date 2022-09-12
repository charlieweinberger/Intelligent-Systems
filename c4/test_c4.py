from c4 import *
from input_player import *

players = [InputPlayer(), InputPlayer()]

game = Connect4(players, show_board = True)
game.run_to_completion()