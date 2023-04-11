import matplotlib.pyplot as plt
plt.style.use('bmh')
from run_ENN import *

num_players = 15
num_gens = 50

weight_range = 0.2 # used in ENN.py
mutation_rate = 0.05 # not being used rn
K = 2 # not being used rn

gens = list(range(num_gens))
max_payoffs = [0]*num_gens

runENN = RunENN(num_players)
runENN.initialize_first_gen()

for gen_num in range(num_gens):
    print(f'Running generation {gen_num + 1} out of {num_gens}...')
    runENN.make_new_gen()
    max_payoffs[gen_num] += max(runENN.prev_gen_payoffs) / num_trials

print('Creating plot...')

plt.plot(list(range(num_gens)), max_payoffs)
plt.xlabel('number of generations')
plt.ylabel('avg max payoff')
plt.savefig('checkers/blondie24/blondie24_ENN_performance_curve.png')

print('Finished plotting!')