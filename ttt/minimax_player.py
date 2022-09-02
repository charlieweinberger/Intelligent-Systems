from game_tree import *

class MinimaxPlayer():

    def __init__(self):
        self.player_number = None
    
    def set_player_number(self, player_number):
        self.player_number = player_number
        self.game = ReducedTicTacToeTree([[None for _ in range(3)] for _ in range(3)], self.player_number)
        self.game.build_tree()
        self.game.root.set_score()
    
    def update_state(self, state):
        if self.game.root.state != state:
            for child in self.game.root.children:
                if child.state == state:
                    self.game.root = child

    def choose_move(self, choices):

        for child in self.game.root.children:
            if child.score == max(node.score for node in self.game.root.children):

                for i in range(3):
                    for j in range(3):
                        if self.game.root.state[i][j] != child.state[i][j]:
                            return (i, j)

if __name__ == "__main__":

    tree = ReducedTicTacToeTree([[None for _ in range(3)] for _ in range(3)], 1)
    tree.build_tree()

    old_state = [[1, 2, 1], [2, None, 1], [2, 1, 2]]
    new_state = [[1, 2, 1], [2, 1, 1], [2, 1, 2]]
    node = tree.all_nodes[str(old_state)]
    print(tree.get_move_from_states(old_state, new_state))