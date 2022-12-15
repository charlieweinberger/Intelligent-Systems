import matplotlib.pyplot as plt
plt.style.use('bmh')
from fogelENN import *

"""

Input Layer: 9 linearly-activated nodes and 1 bias node
Hidden Layer: H sigmoidally-activated nodes and 1 bias node (H is variable, as will be described later)
Output Layer: 9 sigmoidally-activated nodes

"""

def normalize_data(data):
    x, y = [point[0] for point in data], [point[1] for point in data]
    return [((px - min(x)) / (max(x) - min(x)), (2*(py - min(y)) / (max(y) - min(y))) - 1) for px, py in data]

data = normalize_data([
    (0.0, 7), (0.2, 5.6), (0.4, 3.56), (0.6, 1.23), (0.8, -1.03),
    (1.0, -2.89), (1.2, -4.06), (1.4, -4.39), (1.6, -3.88), (1.8, -2.64),
    (2.0, -0.92), (2.2, 0.95), (2.4, 2.63),  (2.6, 3.79), (2.8, 4.22),
    (3.0, 3.8), (3.2, 2.56), (3.4, 0.68), (3.6, -1.58), (3.8, -3.84),
    (4.0, -5.76), (4.2, -7.01), (4.4, -7.38), (4.6, -6.76), (4.8, -5.22)
])

mutation_rate = 0.05
evolvingNN = FogelEvolvingNeuralNet(data, mutation_rate)

graph_x = list(range(0, 1, 0.001)) # [x/1000 for x in range(0, 1000)]

plt.figure(0)
plt.scatter([point[0] for point in data], [point[1] for point in data])
for net in evolvingNN.nets:
    plt.plot(graph_x, [net.predict(x) for x in graph_x], color='blue')

generation_nums = [1, 2, 5, 10, 25, 50, 100, 200, 500, 1000, 1500, 2000, 2500]

for num in generation_nums:
    while evolvingNN.gen != num:
        evolvingNN.make_new_gen()

for net in evolvingNN.nets:
    plt.plot(graph_x, [net.predict(x) for x in graph_x], color='red')
plt.savefig('neural_nets/fogel/initial_vs_final_regressor.png')