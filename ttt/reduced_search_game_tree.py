import copy, math
from tic_tac_toe import *

class Node():
    
    def __init__(self, state, player_turn, player_number, depth):
        
        self.state = state
        self.player_turn = player_turn
        self.player_number = player_number
        self.depth = depth

        self.winner = self.check_for_winner()
        self.parents = []
        self.children = []
        self.score = None
    
    def get_rcd_combinations(self):
        return [
            [self.state[0][i] for i in range(3)],
            [self.state[1][i] for i in range(3)],
            [self.state[2][i] for i in range(3)],
            [self.state[i][0] for i in range(3)],
            [self.state[i][1] for i in range(3)],
            [self.state[i][2] for i in range(3)],
            [self.state[i][i] for i in range(3)],
            [self.state[i][2-i] for i in range(3)]
        ]

    def check_for_winner(self):
        
        rcd = self.get_rcd_combinations()
        valid_rcd = [item for item in rcd if None not in item]

        for row in valid_rcd:
            if len(set(row)) == 1:
                return row[0]
        
        return 'tie' if valid_rcd == rcd else None
    
    def set_score(self):
        
        if self.children == None or len(self.children) == 0:
        
            self.winner = self.check_for_winner()

            if self.winner:

                if self.winner == self.player_number:
                    self.score = 1
                elif self.winner == 3 - self.player_number:
                    self.score = -1
                elif self.winner == 'tie':
                    self.score = 0
            
            else:
            
                score = 0

                for row in self.get_rcd_combinations():
                    if row.count(self.player_number) == 2 and row.count(None) == 1:
                        score += 1
                    if row.count(3 - self.player_number) == 2 and row.count(None) == 1:
                        score -= 1
                
                self.score = score / 8

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

class ReducedSearchTree():
    
    def __init__(self, root_state, player_number, ply):
        self.root = Node(root_state, 1, player_number, 0)
        self.player_number = player_number
        self.current_nodes = [self.root]
        self.all_nodes = {str(self.root.state):self.root}
        self.ply = ply
    
    def create_node_children(self, node):

        # print(f'{node.winner = }')
        # print(f'{node.depth = }')
        # print(f'{len(node.children) = }')

        if (node.winner == None or node.depth + 1 == self.ply) and len(node.children) == 0:

            # print('b')
        
            children = []
            choices = [(i, j) for i in range(3) for j in range(3) if node.state[i][j] == None]

            # print('')
            # print(str(node.state))

            for choice in choices:

                state_copy = copy.deepcopy(node.state)
                state_copy[choice[0]][choice[1]] = node.player_turn

                if str(state_copy) not in list(self.all_nodes.keys()):
                    self.all_nodes[str(state_copy)] = Node(state_copy, 3 - node.player_turn, self.player_number, node.depth + 1)
                
                child = self.all_nodes[str(state_copy)]
                child.parents.append(node)
                children.append(child)

            # print(f'{len(children) = }')
            node.children = children
        
        for child in node.children:
            child.depth = node.depth + 1

    def build_tree(self):
        
        # print(f'{len(self.current_nodes) = }')
        # print(f'{self.current_nodes[0].depth = }')

        if len(self.current_nodes) == 0 or self.current_nodes[0].depth == self.ply:
            return

        # print(f'building children for layer {self.current_nodes[0].depth + 1}...')
        
        all_children = []
        for node in self.current_nodes:
            self.create_node_children(node)
            all_children += node.children
        
        self.current_nodes = all_children
        self.build_tree()

if __name__ == "__main__":

    # for i in [0, 1, 2]:
    for i in range(10):
        print(f'\nReduced Search Depth {i}-ply:')
        tree = ReducedSearchTree([[None for _ in range(3)] for _ in range(3)], 1, i)
        tree.build_tree()
        print(f'Total number of nodes: {len(list(tree.all_nodes.keys()))}')