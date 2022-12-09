from numpy.random import normal
from randomNN import *
import math, random

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
            self.nets.append(RandomNeuralNet(node_layers, bias_node_indices, f, weight_range, mutation_rate))

    def set_rss(self, neural_net):
        rss = sum((neural_net.predict(x) - y) ** 2 for x, y in self.data)
        neural_net.rss = rss
        return rss
    
    def rss_all(self):
        for net in self.nets:
            self.set_rss(net)
    
    def avg_rss(self):
        self.rss_all()
        return sum(net.rss for net in self.nets) / len(self.nets)
    
    def avg_predict(self, x):
        return sum(net.predict(x) for net in self.nets) / len(self.nets)

    def make_child(self, nn):

        p_mutation_rate = nn.mutation_rate
        W = len(nn.weights)
        weird_coefficient = math.exp(normal(0, 1) / (2**0.5 * W**0.25))
        c_mutation_rate = p_mutation_rate * weird_coefficient

        child = RandomNeuralNet(self.node_layers, [], self.f, self.weight_range, c_mutation_rate)
        new_weights = {key : p_weight + p_mutation_rate * normal(0, 1) for key, p_weight in nn.weights.items()}
        child.weights = new_weights
        return child
    
    def make_new_gen(self):

        self.rss_all()
        self.nets.sort(key=lambda x: x.rss)

        parents = list(self.nets[:int(self.num_nets/2)])
        children = [self.make_child(parent_nn) for parent_nn in parents]

        self.nets = parents + children
        self.gen += 1