import matplotlib.pyplot as plt
plt.style.use('bmh')
from fogel_enn_players import *

gens = list(range(100))
max_payoffs = [0]*100

num_parent_networks = 10 # change to 50
num_trials = 5 # change to 20
num_gens = 50 # change to 800

for i in range(num_trials):
    
    ennp = EvolvingNeuralNetPlayers(num_parent_networks)
    ennp.initialize_first_gen()
    
    print(f'trial {i + 1}')
    print('initialized first gen')
    
    for gen_num in range(num_gens):
        
        ennp.make_new_gen()
        max_payoff = max(ennp.prev_gen_payoffs)
        
        print(f'trial {i + 1} gen {ennp.gen_num - 1} max payoff: {max_payoff}')
        
        max_payoffs[gen_num] += max_payoff / num_trials
    
    ennp.get_top_networks()

print('finished trials, making plot')

plt.plot(gens, max_payoffs)
plt.xlabel('gen #')
plt.ylabel('avg max payoff')
plt.savefig('fogel/fogel_evolving_nn_players.png')

print('finished plotting')