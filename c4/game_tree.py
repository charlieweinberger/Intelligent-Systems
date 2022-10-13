import copy, math
from c4 import *
from global_functions import *

class Node():
    
    def __init__(self, state, player_turn, player_number, depth):
        
        self.state = state
        self.player_turn = player_turn
        self.player_number = player_number
        self.depth = depth

        self.winner = check_for_winner(self.state)
        self.parents = []
        self.children = []
        self.score = None
    
    def set_score(self):
        
        if self.children == None or len(self.children) == 0:
        
            self.winner = check_for_winner(self.state)

            if self.winner:

                if self.winner == self.player_number:
                    self.score = 1
                elif self.winner == 3 - self.player_number:
                    self.score = -1
                elif self.winner == 'tie':
                    self.score = 0
            
            else:
            
                score = 0
                combinations = get_combinations(self.state)

                for row in combinations:
                    if row.count(self.player_number) == 3 and row.count(None) == 1:
                        score += 1
                    if row.count(3 - self.player_number) == 3 and row.count(None) == 1:
                        score -= 1
                
                self.score = score / len(combinations)

                if self.score > 0:
                    self.winner = self.player_number
                elif self.score < 0:
                    self.winner = 3 - self.player_number
                elif self.score == 0:
                    self.winner = 'tie'

        else:
            
            for child in self.children:
                child.set_score()
            
            child_scores = [child.score for child in self.children]

            if self.player_turn == self.player_number:
                self.score = max(child_scores)
            elif self.player_turn == 3 - self.player_number:
                self.score = min(child_scores)

class C4GameTree():
    
    def __init__(self, root_state, player_number, ply):
        self.root = Node(root_state, 1, player_number, 0)
        self.player_number = player_number
        self.current_nodes = [self.root]
        self.all_nodes = {str(self.root.state):self.root}
        self.ply = ply
    
    def create_node_children(self, node):

        if (node.winner == None or node.depth + 1 == self.ply) and len(node.children) == 0:
        
            children = []

            for move in get_moves(node.state):

                state_copy = copy.deepcopy(node.state)
                update_state(state_copy, move, node.player_turn)

                if str(state_copy) not in list(self.all_nodes.keys()):
                    self.all_nodes[str(state_copy)] = Node(state_copy, 3 - node.player_turn, self.player_number, node.depth + 1)
                
                child = self.all_nodes[str(state_copy)]
                child.parents.append(node)
                children.append(child)

            node.children = children
        
        for child in node.children:
            child.depth = node.depth + 1

    def build_tree(self):
        
        if len(self.current_nodes) == 0 or self.current_nodes[0].depth == self.ply:
            return
        
        all_children = []
        for node in self.current_nodes:
            self.create_node_children(node)
            all_children += node.children
        
        self.current_nodes = all_children
        self.build_tree()

if __name__ == "__main__":

    for i in range(10):
        print(f'\nReduced Search Depth {i}-ply:')
        tree = C4GameTree([[None for _ in range(7)] for _ in range(6)], 1, i)
        tree.build_tree()
        print(f'Total number of nodes: {len(list(tree.all_nodes.keys()))}')