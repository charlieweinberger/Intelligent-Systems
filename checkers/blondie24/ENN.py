import math, random, copy, numpy

class Node():
    
    def __init__(self, index, f, is_biased=False):
        self.index = index
        self.f = f
        self.is_biased = is_biased
        self.input = None
        self.output = None
        self.info_from = []
        self.info_to = []

class Blondie24ENN():

    def __init__(self):
                
        self.input_layer = []
        self.first_hidden_layer = []
        self.second_hidden_layer = []
        self.output_layer = []

        self.layers = [
            self.input_layer,
            self.first_hidden_layer,
            self.second_hidden_layer,
            self.output_layer
        ]

        self.non_input_layers = self.first_hidden_layer + self.second_hidden_layer + self.output_layer

        self.weights = {}
        self.counter = 1
        self.K = 1
    
    def linear(self, x):
        return x

    def tanh(self, x):
        return (math.exp(x) - math.exp(-x)) / (math.exp(x) + math.exp(-x))

    # Neural Network Architecture

    def create_layers(self):
        self.create_layer(self.input_layer, self.linear, 32, True)
        self.create_layer(self.first_hidden_layer, self.tanh, 40, True)
        self.create_layer(self.second_hidden_layer, self.tanh, 10, True)
        self.create_layer(self.output_layer, self.tanh, 1, False)
        # Should I add the piece difference node? (32 input nodes -> piece difference node -> output node)
    
    def create_layer(self, layer, f, n, hasABiasNode):
        for i in range(n):
            node = Node(self.counter, f, (hasABiasNode and (i == n-1)))
            layer.append(node)
            self.counter += 1

    def create_weights(self):

        for i in range(len(self.layers)):
            if i != len(self.layers) - 1:

                layer_1 = self.layers[i]
                layer_2 = self.layers[i + 1]

                for node_1 in layer_1:
                    for node_2 in layer_2:
                        if not node_2.is_biased:
                            self.weights[f'{node_1.index}{node_2.index}'] = self.get_random_weight()

    def get_random_weight(self):
        
        weight_range = 0.2 # from run.py

        num_decimals = 3
        power_of_10 = 10 ** num_decimals
        weight_range_multiple = weight_range * power_of_10
        
        return random.randint(-weight_range_multiple, weight_range_multiple) / power_of_10

    def get_nodes_from_weight_string(self, key):
        node_1_index = int(key[:int(len(key) / 2)])
        node_2_index = int(key[int(len(key) / 2):])
        return [self.get_node(node_1_index), self.get_node(node_2_index)]

    def get_node(self, index):
        for layer in self.layers:
            for node in layer:
                if node.index == index:
                    return node
    
    def reset_nodes(self):
        for layer in self.layers:
            for node in layer:
                node.info_from = []
                node.info_to = []
                node.input = None
                node.output = None

    def connect_nodes(self):
        for key in self.weights:
            node_0, node_1 = self.get_nodes_from_weight_string(key)
            node_0.info_to.append(node_1)
            node_1.info_from.append(node_0)
    
    def input_array(self, input_arr):
                
        for i, node in enumerate(self.input_layer):
            
            if node.is_biased:
                node.output = 1
                continue

            node.input = input_arr[i]
            node.output = node.f(input_arr[i])
        
        for node in self.non_input_layers:
            
            if node.is_biased:
                node.output = 1
                continue

            input_val = 0
            for input_node in node.info_from:
                input_val += input_node.output * self.weights[f'{input_node.index}{node.index}']
            
            node.input = input_val
            node.output = node.f(input_val)
        
        return [node.output for node in self.output_layer]

    def replicate(self):

        new_net = Blondie24ENN()
        
        new_net.input_layer         = copy.deepcopy(self.input_layer)
        new_net.first_hidden_layer  = copy.deepcopy(self.first_hidden_layer)
        new_net.second_hidden_layer = copy.deepcopy(self.second_hidden_layer)
        new_net.output_layer        = copy.deepcopy(self.output_layer)

        new_net.weights = {key:self.weights[key] for key in self.weights}

        new_net.reset_nodes()
        new_net.connect_nodes()

        new_net.counter = int(self.counter)

        for key in new_net.weights:
            new_net.weights[key] += N(0, 0.05) # mutation rate?
        
        new_net.K = self.K * math.exp(N(0, 1) / math.sqrt(2))

        if (new_net.K < 1): new_net.K = 1
        if (new_net.K > 3): new_net.K = 3

        return new_net
    
    def N(mean, standard_deviation):
        return numpy.random.normal(mean, standard_deviation)

    def initialize(self):
        if len(self.input_layer) != 0: return
        self.create_layers()
        self.create_weights()
        self.reset_nodes()
        self.connect_nodes()