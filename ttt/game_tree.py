import copy

class Node():
    
    def __init__(self, state, player_turn, player_number):
        self.state = state
        self.player_turn = player_turn
        self.player_number = player_number
        self.winner = self.check_for_winner()
        self.previous = []
        self.children = []
        self.score = None
    
    def check_for_winner(self):
        
        rcd = [
            [self.state[0][i] for i in range(3)],
            [self.state[1][i] for i in range(3)],
            [self.state[2][i] for i in range(3)],
            [self.state[i][0] for i in range(3)],
            [self.state[i][1] for i in range(3)],
            [self.state[i][2] for i in range(3)],
            [self.state[i][i] for i in range(3)],
            [self.state[i][2-i] for i in range(3)]
        ]
        
        valid_rcd = [item for item in rcd if None not in item]

        for row in valid_rcd:
            if len(set(row)) == 1:
                return row[0]
        
        return 'tie' if valid_rcd == rcd else None
    
    def set_score(self):
        
        if self.children == None or len(self.children) == 0:
        
            if self.winner == self.player_number:
                self.score = 1
            elif self.winner == 3 - self.player_number:
                self.score = -1
            elif self.winner == 'tie':
                self.score = 0
            
        else:
            
            for child in self.children:
                child.set_score()
            
            child_scores = [child.score for child in self.children]

            if self.player_turn == self.player_number:
                self.score = max(child_scores)
            elif self.player_turn == 3 - self.player_number:
                self.score = min(child_scores)

class ReducedTicTacToeTree():
    
    def __init__(self, root_state, player_number):
        self.root = Node(root_state, 1, player_number)
        self.player_number = player_number
        self.current_nodes = [self.root]
        self.all_nodes = {str(self.root.state):self.root}
    
    def create_node_children(self, node):
        
        if node.winner != None or len(node.children) != 0:
            return
        
        children = []
        choices = [(i, j) for i in range(3) for j in range(3) if node.state[i][j] == None]
        
        for choice in choices:
        
            state_copy = copy.deepcopy(node.state)
            state_copy[choice[0]][choice[1]] = node.player_turn
        
            if str(state_copy) in list(self.all_nodes.keys()):
                children.append(self.all_nodes[str(state_copy)])
                self.all_nodes[str(state_copy)].previous.append(node)
            
            else:
        
                child = Node(state_copy, 3 - node.player_turn, self.player_number)
                child.previous = [node]
                children.append(child)
                self.all_nodes[str(state_copy)] = child
        
        node.children = children

    def build_tree(self):
        
        if len(self.current_nodes) == 0:
            self.current_nodes = [self.root]
            return
        
        all_children = []
        for node in self.current_nodes:
            self.create_node_children(node)
            if len(node.children) != 0:
                all_children += node.children
        
        self.current_nodes = all_children
        self.build_tree()