from c4 import *
from game_tree import *

class HeuristicPlayer():
    
    def __init__(self, ply):
        self.player_number = None
        self.ply = ply
    
    def set_player_number(self, player_number):
        self.player_number = player_number
        self.game = C4GameTree([[None for _ in range(7)] for _ in range(6)], self.player_number, self.ply)
        self.game.build_tree()
        self.game.root.set_score()

    def get_choices(self, state):

        choices = []

        for row in state:
            for i, space in enumerate(row):
                if space == None:
                    choices.append(i)
        
        return list(set(choices))

    def choose_move(self, state):
        
        for node in self.game.root.children:
            if node.score == max(node.score for node in self.game.root.children):  
                
                for move in get_choices(self.game.root.state):
                    for i in range(5, -1, -1):
                        if self.game.root.state[i][move] != node.state[i][move]:
                            return move
        
    def update_state(self, state):

        for child in self.game.root.children:
            if child.state == state:

                self.game.root = child
                self.game.root.depth = 0
                
                self.game.player_number = self.player_number
                self.game.current_nodes = [self.game.root]
                self.game.all_nodes = {str(state):self.game.root}
                
                self.game.build_tree()
                self.game.root.set_score()
                
                break