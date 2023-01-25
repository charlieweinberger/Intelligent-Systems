import matplotlib.pyplot as plt
plt.style.use('bmh')
from fogel_enn_players import *
import pickle

# version = 'simple'
version = 'full'

# don't change below

num_parent_networks = 10 if version == 'simple' else 50
num_trials          =  5 if version == 'simple' else 20
num_gens            = 50 if version == 'simple' else 100

gens = list(range(num_gens))
max_payoffs = [0]*num_gens

file = open('fogel/nn_players.pickle', 'wb')

for i in range(num_trials):
    
    print(f'trial {i + 1}')
    
    ennp = EvolvingNeuralNetPlayers(num_parent_networks)
    ennp.initialize_first_gen()
            
    for gen_num in range(num_gens):
        print(f'gen {gen_num + 1}')
        ennp.make_new_gen()
        max_payoffs[gen_num] += max(ennp.prev_gen_payoffs) / num_trials
    
    ennp.get_top_networks()
    pickle.dump(ennp.copy_players(), file)

file.close()

print('making plot')

plt.plot(gens, max_payoffs)
plt.xlabel('number of generations')
plt.ylabel('avg max payoff')
plt.savefig('fogel/fogel_evolving_nn_players.png')

print('finished plotting')