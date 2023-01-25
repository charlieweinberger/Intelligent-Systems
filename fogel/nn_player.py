import math
from fogel_nn import *

class NeuralNetPlayer():

    def __init__(self, net=None):
        self.player_number = None
        self.net = FogelEvolvingNeuralNet() if net == None else net
        self.payoff_score = 0
        self.eval_score = 0
    
    def set_player_number(self, n):
        self.player_number = n
    
    def update_state(self, state):
        pass
    
    def choose_move(self, state):
                
        state_map = {
            None: 0,
            self.player_number: 1,
            3 - self.player_number: -1
        }

        flattened_state = []
        for row in state:
            for elem in row:
                flattened_state.append(state_map[elem])

        outputs = self.net.input_array(flattened_state)
        out_vals = list(outputs)
        max_index = outputs.index(max(outputs))
        
        while flattened_state[max_index] != 0:
            out_vals.remove(max(out_vals))
            max_index = outputs.index(max(out_vals))
        
        return (math.floor(max_index / 3), max_index % 3)

    
    def initialize_net(self):
        self.net.initialize()
    
    def replicate(self):
        new_net = self.net.replicate()
        return NeuralNetPlayer(new_net)