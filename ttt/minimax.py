from node import *
from ttt_tree import *

class Minimax():

    def __init__(self):
        self.tree = TicTacToeTree(1)
        self.tree.build_tree()
        
    def score_nodes():

        i = 0
        current_nodes = []
        parent_nodes = []

        while self.tree.root.score == '':
            
            if i == 0: self.score_leaf_nodes(parent_nodes)
            else:

                pass
    
    def score_leaf_nodes():

        for node in list(self.tree.nodes.values()):
                
            winner = node.check_for_winner()

            if winner == 'tie':
                node.score = 0
            elif winner == self.tree.player_number:
                node.score = 1
            else:
                node.score = -1
            
            parent_nodes += node.parent_nodes