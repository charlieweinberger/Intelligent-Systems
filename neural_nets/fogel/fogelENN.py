import math, random, numpy
from fogelRNN import *

class FogelEvolvingNeuralNet():

    def __init__(self, data, mutation_rate):

        self.num_nets = 50
        self.f = lambda x: (math.exp(x) - math.exp(-x)) / (math.exp(x) + math.exp(-x))
        self.weight_range = [-0.5, 0.5]

        self.data = data
        self.mutation_rate = mutation_rate

        self.gen = 1

        for _ in range(num_nets):

            h = random.randint(1, 11)
            self.node_layers = [10, h + 1, 9]
            self.bias_node_indices = [10, 10 + h + 1]
            
            net = FogelRandomNeuralNet(node_layers, bias_node_indices, f, weight_range, mutation_rate)
            self.nets.append(net)

    def make_new_gen(self):
        self.nets = [self.replicate(parent) for parent in self.nets]
        self.gen += 1

    def replicate(self, parent):

        child = parent.make_a_copy(parent.weights)
        child.connect_nodes()

        for key in child.weights:
            child.weights[key] += numpy.random.normal(0, 0.05)
        
        return child