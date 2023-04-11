import math
from ENN import *

class NeuralNetPlayer():

    def __init__(self, net=None):
        self.player_number = None
        self.net = Blondie24ENN() if net == None else net
        self.payoff_score = 0
        self.eval_score = 0
    
    def set_player_number(self, n):
        self.player_number = n
    
    def update_state(self, state):
        pass
    
    def choose_move(self, state, moves):

        # Converting Board to Input

        state_map = {
            0: 0,
            self.player_number: 1,
            3 - self.player_number: -1,
            -self.player_number: self.net.K,
            -(3 - self.player_number): -self.net.K,
        }

        print(f'{state = }')

        flattened_state = [state_map[elem] for row in state for elem in row]

        print(f'{flattened_state = }')

        # Converting Output to Action

        """
        
        https://www.justinmath.com/reimplementing-blondie24/
        https://www.justinmath.com/reduced-search-depth-and-heuristic-evaluation-for-connect-four/
        
        An action is chosen via the minimax algorithm using the above heuristic evaluation function. As the network learns, this heuristic evaluation function will become more accurate.

        - If a board state is a win or a loss, return 1 or -1, respectively.
        - Otherwise, pass the board state as input to the neural network and return the activity of the output node.

        The search depth is set to d = 4 to allow for reasonable execution times.
        
        """

        outputs = self.net.input_array(flattened_state)
        out_vals = list(outputs)
        max_index = outputs.index(max(outputs))
        
        while flattened_state[max_index] != 0:
            out_vals.remove(max(out_vals))
            max_index = outputs.index(max(out_vals))
        
        print(f'{max_index = }')
        print(f'move = {(math.floor(max_index / 3), max_index % 3)}')

        return (math.floor(max_index / 3), max_index % 3)

    
    def initialize_net(self):
        self.net.initialize()
    
    def replicate(self):
        new_net = self.net.replicate()
        return NeuralNetPlayer(new_net)