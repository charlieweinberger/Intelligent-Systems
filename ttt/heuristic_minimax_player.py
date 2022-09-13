from game_tree import *

class HeuristicMinimaxPlayer():
    
    def __init__(self, n_ply):
        self.player_number = None
        self.n_ply = n_ply
    
    def set_player_number(self, player_number):
        self.player_number = player_number
        self.game = ReducedTicTacToeTree([[None for _ in range(3)] for _ in range(3)], self.player_number)
        self.game.build_tree()
        self.game.root.set_score()
    
    def update_state(self, state):
        if self.game.root.state != state:
            for child in self.game.root.children:
                if child.state == state:
                    self.game.root = child
    
    def choose_move(self, state):

        for node in self.game.root.children:
            if node.score == max(node.score for node in self.game.root.children):
                
                for i in range(3):
                    for j in range(3):
                        if self.game.root.state[i][j] != node.state[i][j]:
                            return (i, j)