class Node():
    def __init__(self, state, player_turn):
        self.state = state
        self.player_turn = player_turn
        self.winner = None
        self.children = None

    def check_for_winner(self):

        rows = self.state.copy()
        cols =  [[self.state[i][j] for i in range(3)] for j in range(3)]
        diags = [[self.state[i][i] for i in range(3)],
                 [self.state[i][2-i] for i in range(3)]]

        board_full = True
        for row in rows + cols + diags:
            
            if None in row:
                board_full = False

            for player in [1, 2]:
                if row == [player for _ in range(3)]:
                    return player
        
        return 'Tie' if board_full else None