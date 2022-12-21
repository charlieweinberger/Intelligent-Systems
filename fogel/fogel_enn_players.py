import random, sys
sys.path.append('ttt')
from tic_tac_toe import *
from nn_player import *
from np_player import *

class EvolvingNeuralNetPlayers():

    def __init__(self, num_players, num_games=32):
        
        self.num_players = num_players
        self.num_games = num_games
        
        self.players = []
        self.prev_gen_payoffs = []
        self.gen_num = 0
    
    def initialize_first_gen(self):
        self.players = [NeuralNetPlayer() for _ in range(self.num_players)]
        for player in self.players:
            player.initialize_net()
        self.gen_num += 1
    
    def run_games(self, players=None):
        
        if players == None: players = self.players

        for player in self.players:
            for _ in range(self.num_games):
                
                game = TicTacToe([player, NearPerfectPlayer()])
                game.run_to_completion()
                
                if game.winner == 1:
                    player.payoff_score += 1
                elif game.winner == 2:
                    player.payoff_score -= 10

    def run_second_eval(self, players=None):
        
        if players == None: players = self.players

        for i, player in enumerate(self.players):
            other_player_index = [index for index in range(len(self.players)) if index != i]
            for _ in range(10):
                
                random_index = random.choice(other_player_index)
                random_player = self.players[random_index]
                
                if player.payoff_score > random_player.payoff_score:
                    player.eval_score += 1
    
    def get_top_networks(self):
        self.run_games()
        self.run_second_eval()
        self.players.sort(key=lambda p: p.eval_score, reverse=True)
        return self.players[:int(self.num_players / 2)]

    def reset_scores(self, players):
        for player in players:
            player.payoff_score = 0
            player.eval_score = 0
    
    def make_new_gen(self):
        
        if len(self.players) == 0:
            self.initialize_first_gen()

        top_players = self.get_top_networks()
        new_players = [player.replicate() for player in top_players]
        new_gen = top_players + new_players
        
        self.prev_gen_payoffs = [p.payoff_score for p in self.players]

        self.reset_scores(new_gen)
        self.players = new_gen
        self.gen_num += 1