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
        self.added_coord = None
    
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
        
        return "tie" if valid_rcd == rcd else None
    
    def get_possible_moves(self):
        return [(i, j) for i in range(3) for j in range(3) if self.state[i][j] == None]

    def set_score(self):
        
        if self.children:

            children_scores = [child.set_score() for child in self.children]

            scoreMap = {
                self.player_number: max(children_scores),
                3 - self.player_number: min(children_scores)
            }
        
        else:

            scoreMap = {
                self.player_number: 1,
                3 - self.player_number: -1,
                'tie': 0
            }

        self.score = scoreMap[self.player_turn]
        return self.score

class ReducedTicTacToeTree():

    def __init__(self, root_state, player_number):
        self.root = Node(root_state, 1, player_number)
        self.player_number = player_number
        self.num_leaf_nodes = 0
        self.current_nodes = [self.root]
        self.all_nodes = {str(self.root.state):self.root}

    def build_tree(self):

        while len(self.current_nodes) != 0:

            all_children = []
            
            for node in self.current_nodes:
            
                self.create_children(node)
                all_children += node.children
            
                if len(node.children) == 0:
                    self.num_leaf_nodes += 1
            
            self.current_nodes = all_children

        self.current_nodes = [self.root]

    def create_children(self, node):

        if node.winner and node.children:
            return

        children = []
        for option in node.get_possible_moves():

            child_state = copy.deepcopy(node.state) 
            child_state[option[0]][option[1]] = node.player_turn
            
            if str(child_state) in list(self.all_nodes.keys()):
                
                children.append(self.all_nodes[str(child_state)])
                self.all_nodes[str(child_state)].previous.append(node)
            
            else:
            
                child_node = Node(child_state, 3 - node.player_turn, self.player_number)
                children.append(child_node)
                child_node.previous = [node]
                self.all_nodes[str(child_state)] = child_node
            
        node.children = children

if __name__ == "__main__":

    tree = ReducedTicTacToeTree([[None for _ in range(3)] for _ in range(3)], 1)
    tree.build_tree()

    print(len(list(tree.all_nodes.keys()))) # 5,478 or something similar 
    print(tree.num_leaf_nodes) # 255,168