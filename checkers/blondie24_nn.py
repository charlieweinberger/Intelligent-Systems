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
        
        self.weights = {}
        self.counter = 1
    
    def linear(self, x):
        return x

    def tanh(self, x):
        return (math.exp(x) - math.exp(-x)) / (math.exp(x) + math.exp(-x))

    def create_layers(self):
        self.create_layer(self.input_layer, self.linear, 32, True)
        self.create_layer(self.first_hidden_layer, self.tanh, 40, True)
        self.create_layer(self.second_hidden_layer, self.tanh, 10, True)
        self.create_layer(self.output_layer, self.tanh, 1, False)
    
    def create_layer(self, layer, f, n, hasABiasNode):
        for i in range(n):
            node = Node(self.counter, f, (hasABiasNode and (i == n-1)))
            layer.append(node)
            self.counter += 1
    
    def create_weights(self):

        if len(self.input_layer) == 0 or len(self.hidden_layer) == 0 or len(self.output_layer) == 0: return
        
        for in_node in self.input_layer:
            for h_node in self.hidden_layer:
                if h_node.is_biased: continue
                self.weights[f'{in_node.index}{h_node.index}'] = random.randint(-500, 500) / 1000
        
        for h_node in self.hidden_layer:
            for out_node in self.output_layer:
                self.weights[f'{h_node.index}{out_node.index}'] = random.randint(-500, 500) / 1000
    
    def get_nodes_from_weight_string(self, key):
        node_1_index = int(key[:int(len(key) / 2)])
        node_2_index = int(key[int(len(key) / 2):])
        return [self.get_node(node_1_index), self.get_node(node_2_index)]

    def get_node(self, index):
        for node in self.input_layer + self.hidden_layer + self.output_layer:
            if node.index == index:
                return node
    
    def reset_nodes(self):
        for node in (self.input_layer + self.hidden_layer + self.output_layer):
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
        
        for node in self.hidden_layer + self.output_layer:
            
            if node.is_biased:
                node.output = 1
                continue

            input_val = 0
            for input_node in node.info_from:
                input_val += input_node.output * self.weights[f'{input_node.index}{node.index}']
            
            node.input = input_val
            node.output = node.f(input_val)
        
        return [node.output for node in self.output_layer]
    
    def add_H_node(self):
        
        if len(self.hidden_layer) == 11: return
        
        new_node = Node(self.counter, self.sigmoid_f)
        self.hidden_layer.append(new_node)
        self.counter += 1

        for in_node in self.input_layer:
            self.weights[f'{in_node.index}{new_node.index}'] = 0
        for out_node in self.output_layer:
            self.weights[f'{new_node.index}{out_node.index}'] = 0
        
        self.reset_nodes()
        self.connect_nodes()
    
    def delete_H_node(self):
        
        if len(self.hidden_layer) == 2: return
        
        random_node = random.choice([node for node in self.hidden_layer if not node.is_biased])
        weights_to_delete = []

        for key in self.weights:
            if random_node in self.get_nodes_from_weight_string(key):
                weights_to_delete.append(key)

        for key in weights_to_delete:
            del self.weights[key]

        self.num_H -= 1
        self.hidden_layer.remove(random_node)
        
        for in_node in self.input_layer:
            in_node.info_to.remove(random_node)
        for out_node in self.output_layer:
            out_node.info_from.remove(random_node)

    def replicate(self):

        new_net = FogelEvolvingNeuralNet()
        
        new_net.input_layer = copy.deepcopy(self.input_layer)
        new_net.hidden_layer = copy.deepcopy(self.hidden_layer)
        new_net.output_layer = copy.deepcopy(self.output_layer)

        new_net.weights = {key:self.weights[key] for key in self.weights}

        new_net.reset_nodes()
        new_net.connect_nodes()

        new_net.counter = int(self.counter)

        for key in new_net.weights:
            new_net.weights[key] += numpy.random.normal(0, 0.05)

        if random.random() < 0.5:
            if random.random() < 0.5:
                new_net.add_H_node()
            else:
                new_net.delete_H_node()

        return new_net
    
    def initialize(self):
        if len(self.input_layer) != 0: return
        self.create_layers()
        self.create_weights()
        self.reset_nodes()
        self.connect_nodes()