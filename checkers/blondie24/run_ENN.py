import random, copy
from checkers import *
from NN_player import *

# should be all done (aka updated for blondie24), but check "Converting Output to Action" section ot be sure

class RunENN():

    def __init__(self, num_players, num_games):
        
        self.num_players = num_players
        self.num_games = 5
        
        self.players = []   
        self.prev_gen_payoffs = []
        self.gen_num = 0
    
    def initialize_first_gen(self):
        self.players = [NeuralNetPlayer() for _ in range(self.num_players)]
        for player in self.players:
            player.initialize_net()
        self.gen_num += 1

    def get_top_networks(self):

        self.prev_gen_payoffs = []

        for player in self.players:
            for _ in range(self.num_games):

                game = Checkers([player, random.choice(self.players)])
                game.run_to_completion()
                
                if   game.winner == 1: player.payoff_score += 1
                elif game.winner == 2: player.payoff_score -= 2

            self.prev_gen_payoffs.append(player.payoff_score)

        self.players.sort(key=lambda player: player.eval_score, reverse=True)
        return self.players[0:self.num_players - 1]

    def reset_scores(self, players):
        for player in players:
            player.payoff_score = 0
            player.eval_score = 0
    
    def make_new_gen(self):
        
        if len(self.players) == 0: self.initialize_first_gen()

        top_players = self.get_top_networks()
        new_players = [player.replicate() for player in top_players]
        new_gen = top_players + new_players

        self.reset_scores(new_gen)
        self.players = new_gen
        self.gen_num += 1
    
    def copy_players(self):
        return [copy.deepcopy(player.net) for player in self.players]