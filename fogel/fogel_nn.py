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

class FogelEvolvingNeuralNet():

    def __init__(self):
        
        self.num_H = random.randint(1, 10)
        
        self.in_layer = []
        self.h_layer = []
        self.out_layer = []
        
        self.weights = {}
        self.counter = 1
    
    def linear_f(self, x):
        return x
    
    def sigmoid_f(self, x):
        return 1 / (1 + math.exp(-x))
    
    def create_layers(self):

        for i in range(10):
            self.in_layer.append(Node(self.counter, self.linear_f, i == 9))
            self.counter += 1
            
        for i in range(self.num_H + 1):
            self.h_layer.append(Node(self.counter, self.sigmoid_f, i == self.num_H))
            self.counter += 1
        
        for _ in range(9):
            self.out_layer.append(Node(self.counter, self.sigmoid_f))
            self.counter += 1
    
    def create_weights(self):

        if len(self.in_layer) == 0 or len(self.h_layer) == 0 or len(self.out_layer) == 0: return
        
        for in_node in self.in_layer:
            for h_node in self.h_layer:
                if h_node.is_biased: continue
                self.weights[f'{in_node.index}{h_node.index}'] = random.randint(-500, 500) / 1000
        
        for h_node in self.h_layer:
            for out_node in self.out_layer:
                self.weights[f'{h_node.index}{out_node.index}'] = random.randint(-500, 500) / 1000
    
    def get_node(self, index):
        for node in self.in_layer + self.h_layer + self.out_layer:
            if node.index == index:
                return node
    
    def reset_nodes(self):
        for node in (self.in_layer + self.h_layer + self.out_layer):
            node.info_from = []
            node.info_to = []
            node.input = None
            node.output = None

    def connect_nodes(self):
        for key in self.weights:
            node_0 = self.get_node(int(key[:int(len(key) / 2)]))
            node_1 = self.get_node(int(key[int(len(key) / 2):]))
            node_0.info_to.append(node_1)
            node_1.info_from.append(node_0)
    
    def input_array(self, input_arr):
                
        for i, node in enumerate(self.in_layer):
            
            if node.is_biased:
                node.output = 1
                continue

            node.input = input_arr[i]
            node.output = node.f(input_arr[i])
        
        for node in self.h_layer + self.out_layer:
            
            if node.is_biased:
                node.output = 1
                continue

            input_val = 0
            for input_node in node.info_from:
                input_val += input_node.output * self.weights[f'{input_node.index}{node.index}']
            
            node.input = input_val
            node.output = node.f(input_val)
        
        return [node.output for node in self.out_layer]
    
    def make_a_copy(self):
        
        new_net = FogelEvolvingNeuralNet()
        
        new_net.in_layer = copy.deepcopy(self.in_layer)
        new_net.h_layer = copy.deepcopy(self.h_layer)
        new_net.out_layer = copy.deepcopy(self.out_layer)
        new_net.weights = copy.deepcopy(self.weights)

        new_net.reset_nodes()
        new_net.connect_nodes()

        new_net.counter = int(self.counter)
        
        return new_net
    
    def add_H_node(self):
        
        if len(self.h_layer) == 11: return
        
        new_node = Node(self.counter, self.sigmoid_f)
        self.h_layer.append(new_node)
        self.counter += 1

        for in_node in self.in_layer:
            self.weights[f'{in_node.index}{new_node.index}'] = 0
        for out_node in self.out_layer:
            self.weights[f'{new_node.index}{out_node.index}'] = 0
        
        self.reset_nodes()
        self.connect_nodes()
    
    def delete_H_node(self):
        
        if len(self.h_layer) == 2: return
        
        random_node = random.choice([node for node in self.h_layer if not node.is_biased])
        weights_to_delete = []
        
        for key in self.weights:
            if random_node.index in [int(k) for k in key]:
                weights_to_delete.append(key)
        
        for key in weights_to_delete:
            del self.weights[key]
        
        self.h_layer.remove(random_node)
        self.num_H -= 1
        
        for in_node in self.in_layer:
            in_node.info_to.remove(random_node)
        for out_node in self.out_layer:
            out_node.info_from.remove(random_node)
    
    def replicate(self):

        new_net = self.make_a_copy()

        for key in new_net.weights:
            new_net.weights[key] += numpy.random.normal(0, 0.05)

        if random.random() < 0.5:
            if random.random() < 0.5:
                new_net.add_H_node()
            else:
                new_net.delete_H_node()

        return new_net
    
    def initialize(self):
        if len(self.in_layer) != 0: return
        self.create_layers()
        self.create_weights()
        self.reset_nodes()
        self.connect_nodes()