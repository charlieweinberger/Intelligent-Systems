class TicTacToe:
    
    def __init__(self, players, second_player_first, see_board=False):
        self.players = players
        self.second_player_first = second_player_first
        self.see_board = see_board
        self.set_player_numbers()
        self.determine_player_order()
        self.state = [[None for _ in range(3)] for _ in range(3)]
        self.winner = None
        self.turn = 1

    def set_player_numbers(self):
        self.players[0].set_player_number(1)
        self.players[1].set_player_number(2)
    
    def determine_player_order(self):
        if self.second_player_first:
            self.players = self.players[::-1]

    def get_possible_moves(self):
        return [(i, j) for i in range(3) for j in range(3) if self.state[i][j] == None]

    def complete_round(self):

        for player in self.players:

            choices = self.get_possible_moves()

            player_move = player.choose_move(choices)
            self.state[player_move[0]][player_move[1]] = player.player_number

            if self.see_board:
                self.print_board()
                            
            for player in self.players:
                player.update_state(self.state)
            
            if self.check_for_winner() != None:
                self.winner = self.check_for_winner()
                break
                
            self.turn += 1

    def run_to_completion(self):
        while self.winner == None:
            self.complete_round()

    def check_for_winner(self):
        
        rcd = [
            [self.state[0][i] for i in range(3)],
            [self.state[1][i] for i in range(3)],
            [self.state[2][i] for i in range(3)],
            [self.state[i][0] for i in range(3)],
            [self.state[i][1] for i in range(3)],
            [self.state[i][2] for i in range(3)],
            [self.state[i][i] for i in range(3)],
            [self.state[i][2-i] for i in range(3)]
        ]

        valid_rcd = [item for item in rcd if None not in item]
        
        for row in valid_rcd:
            if len(set(row)) == 1:
                return row[0]
        
        if valid_rcd == rcd:
            return "tie"
        
        return None

    def print_board(self):
        print('')
        for i in range(len(self.state)):
            row = self.state[i]
            row_string = ''
            for space in row:
                if space == None:
                    row_string += '_|'
                else:
                    row_string += str(space) + '|'
            print(row_string[:-1])