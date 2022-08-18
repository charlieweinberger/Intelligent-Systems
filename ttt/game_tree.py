import copy
from node import *

class TicTacToeTree():

    def __init__(self, player_number, reduced=True):
        self.root = Node('000000000', player_number)
        self.num_leaf_nodes = 0
        self.reduced = reduced
        self.nodes = {}

    def other_player(self, node):
        return 3 - node.player_turn

    def build_tree(self):
        
        if self.reduced:
            self.nodes[self.root.state] = self.root

        self.make_children(self.root)
        children = self.root.children
        while len(children) != 0:
            children = self.get_grandchildren(children)

    def get_grandchildren(self, children):
        
        grandchildren = []
        for child in children:
            
            winner = child.check_for_winner()
            if winner == '0':
                
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
        
                i = 3 * row_index + col_index

                if node.state[i] == '0':
                   
                    child_board = node.state[0:i] + str(self.other_player(node)) + node.state[i+1:]
                    child_node = Node(child_board, self.other_player(node))
                    
                    if not self.reduced:
                        children.append(child_node)
                    elif child_node.state not in list(self.nodes.keys()):
                        self.nodes[child_node.state] = child_node
                        children.append(child_node)
        
        node.children = children

if __name__ == "__main__":

    tree = TicTacToeTree(1)
    tree.build_tree()

    print(tree.num_leaf_nodes)
    print(len(tree.nodes))