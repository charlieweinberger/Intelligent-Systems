import random, copy

class NearPerfectPlayer():

    def __init__(self):
        self.player_number = None
    
    def set_player_number(self, n):
        self.player_number = n
    
    def update_state(self, state):
        pass
    
    def get_rcd(self, state):
        return [
            [state[0][i] for i in range(3)],
            [state[1][i] for i in range(3)],
            [state[2][i] for i in range(3)],
            [state[i][0] for i in range(3)],
            [state[i][1] for i in range(3)],
            [state[i][2] for i in range(3)],
            [state[i][i] for i in range(3)],
            [state[i][2-i] for i in range(3)]
        ]

    def check_for_winner(self, state):

        board_full = True
        for row in self.get_rcd(state):
            
            if None in row:
                board_full = False
            
            if row.count(row[0]) == 3:
                return row[0]
        
        return 'tie' if board_full else None
    
    def choose_move(self, state):

        moves = [(i, j) for i in range(3) for j in range(3) if state[i][j] == None]
        
        if random.randint(1, 10) == 1:
            return random.choice(moves)
        
        for move in moves:
            
            new_state = copy.deepcopy(state)
            new_state[move[0]][move[1]] = self.player_number

            new_opponent_state = copy.deepcopy(state)
            new_opponent_state[move[0]][move[1]] = 3 - self.player_number

            if self.check_for_winner(new_state) or self.check_for_winner(new_opponent_state):
                return move

        forward_diag = [(0, 0), (1, 1), (2, 2)]
        backward_diag = [(0, 2), (1, 1), (2, 0)]

        for i, row in enumerate(self.get_rcd(state)):
            if row.count(None) == 2 and row.count(3 - self.player_number) == 1:
                
                move = random.choice([n for n, item in enumerate(row) if item == None])
                
                if (i in [0, 1, 2]): return (i % 3, move)
                if (i in [3, 4, 5]): return (move, i % 3)
                if (i == 6): return forward_diag[move]
                if (i == 7): return backward_diag[move]
        
        return random.choice(moves)