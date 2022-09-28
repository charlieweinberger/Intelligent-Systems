class TicTacToe:
    
    def __init__(self, players, show_board=False):

        self.players = players
        self.show_board = show_board
        self.set_player_numbers()
        self.state = [[None for _ in range(3)] for _ in range(3)]
        self.player_turn =  1
        self.winner = None

    def set_player_numbers(self): 
        self.players[0].set_player_number(1)
        self.players[1].set_player_number(2)

    def complete_round(self):
        
        for player in self.players:
            
            print(self.state)

            player_move = player.choose_move(self.state)
            self.state[player_move[0]][player_move[1]] = player.player_number
            self.update_player_states()
            
            self.winner = self.check_for_winner()

            if self.winner:
                if self.show_board:
                    self.print_board()
                    print(f'Winner: {self.winner}\n')
                break
    
        self.player_turn += 1

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

        board_full = True
        for row in rcd:
            
            if None in row:
                board_full = False

            for player in self.players:
                if row == [player.player_number for _ in range(3)]:
                    return player.player_number
        
        return 'tie' if board_full else None
  
    def print_board(self):

        print('')
        for row in self.state:
            row_string = ''
            for space in row:
                if space == None:
                    row_string += '_|'
                else:
                    row_string += str(space) + '|'
            print(row_string[:-1])
        print('')

    def update_player_states(self):
        for player in self.players:
            player.update_state(self.state)