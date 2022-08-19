import copy
from node import *

class TicTacToeTree():

    def __init__(self, player_number, reduced=True):
        self.root = Node([[None for _ in range(3)] for _ in range(3)], player_number)
        self.num_leaf_nodes = 0
        self.reduced = reduced
        self.node_states = []

    def other_player(self, node):
        return 3 - node.player_turn

    def build_tree(self):
        
        if self.reduced:
            self.node_states = [str(self.root.state)]

        self.make_children(self.root)
        children = self.root.children
        while len(children) != 0:
            children = self.get_grandchildren(children)
    
    def get_grandchildren(self, children):
        
        grandchildren = []
        for child in children:
            
            winner = child.check_for_winner()
            if winner is None:
                
                self.make_children(child)
                for grandchild in child.children:
                    grandchildren.append(grandchild)
            
            else:
                child.winner = winner
                self.num_leaf_nodes += 1

        return grandchildren
    
    def make_children(self, node):
        
        children = []
        for row_index in range(3):
            for col_index in range(3):
        
                if node.state[row_index][col_index] is None:
                   
                    child_board = copy.deepcopy(node.state)
                    child_board[row_index][col_index] = self.other_player(node)
                    child_node = Node(child_board, self.other_player(node))
                    
                    if not self.reduced:
                        children.append(child_node)
                    elif str(child_node.state) not in self.node_states:  
                        self.node_states.append(str(child_node.state))              
                        children.append(child_node)
        
        node.children = children

if __name__ == "__main__":

    tree = TicTacToeTree(1)
    tree.build_tree()

    print(tree.num_leaf_nodes)
    print(len(tree.nodes))