from tic_tac_toe import *
from reduced_search_game_tree import *

class HeuristicMinimaxPlayer():
    
    def __init__(self, ply):
        self.player_number = None
        self.ply = ply
    
    def set_player_number(self, player_number):
        self.player_number = player_number
        self.game = ReducedSearchTree([[None for _ in range(3)] for _ in range(3)], self.player_number, self.ply)
        self.game.build_tree()
        self.game.root.set_score()

    def choose_move(self, state):

        print(f'\n{self.ply}-ply minimax player class:')

        print_board(self.game.root.state)
        print(self.game.root.children)

        for node in self.game.root.children:
            if node.score == max(node.score for node in self.game.root.children):

                print_board(node.state)
                
                for i in range(3):
                    for j in range(3):
                        if self.game.root.state[i][j] != node.state[i][j]:
                            print(f'move: {(i, j)}')
                            return (i, j)
        
        print('no matches')

    def update_state(self, state):

        print('\nUpdate state:')

        print_board(state)

        for child in self.game.root.children:
            if child.state == state:

                print(len(list(self.game.all_nodes.keys())))

                self.game.root = child
                self.game.root.depth = 0
                
                self.game.player_number = self.player_number
                self.game.current_nodes = [self.game.root]
                self.game.all_nodes = {str(state):self.game.root}
                
                print(len(list(self.game.all_nodes.keys())))

                self.game.build_tree()
                self.game.root.set_score()

                print(len(list(self.game.all_nodes.keys())))
                
                break