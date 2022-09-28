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

    def update_state(self, state):
        if self.game.root.state != state:
            for child in self.game.root.children:
                if child.state == state:
                    self.game.root = child
    
    def choose_move(self, state):

        # print(self.game.root.state)
        # print(self.game.root.children)

        for node in self.game.root.children:
            if node.score == max(node.score for node in self.game.root.children):

                # print(node.state)
                
                for i in range(3):
                    for j in range(3):
                        if self.game.root.state[i][j] != node.state[i][j]:
                            # print(f'{self.ply}-ply minimax player class: {(i, j)}')
                            return (i, j)
        
        # print('no matches')