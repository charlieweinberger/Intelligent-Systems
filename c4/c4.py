import random

class Connect4:
    
    def __init__(self, players, show_board=False):

        self.players = players
        self.show_board = show_board
        self.set_player_numbers()
        self.state = [[None for _ in range(7)] for _ in range(6)]
        self.player_turn = 1
        self.winner = None

    def set_player_numbers(self): 
        self.players[0].set_player_number(1)
        self.players[1].set_player_number(2)

    def complete_round(self):
        
        for player in self.players:
            
            self.update_state(player)
            self.winner = self.check_for_winner()

            if self.winner:
                if self.show_board:
                    self.print_board()
                    print(f'Winner: Player {self.winner}\n')
                break
    
        self.player_turn += 1

    def update_state(self, player):
        
        move = player.choose_move(self.state)

        for i in range(5, -1, -1):
            if self.state[i][move] == None:
                self.state[i][move] = player.player_number
                break
        
    def run_to_completion(self):
        while self.winner == None:
            self.complete_round()

    def check_for_winner(self):

        four_in_a_row = []

        for i in range(6):
            for j in range(4):
                row = [self.state[i][j + k] for k in range(4)]
                four_in_a_row.append(row)

        for i in range(3):
            for j in range(7):
                column = [self.state[i + k][j] for k in range(4)]
                four_in_a_row.append(column)
        
        for i in range(3):
            for j in range(4):
                forward_diag = [self.state[i + k][j + k] for k in range(4)]
                four_in_a_row.append(forward_diag)
        
        for i in range(3):
            for j in range(3, 7):
                backward_diag = [self.state[i + k][j - k] for k in range(4)]
                four_in_a_row.append(backward_diag)

        board_full = True
        for row in four_in_a_row:
            
            if None in row:
                board_full = False

            for player in self.players:
                if len(set(row)) == 1 and row[0] != None:
                    return row[0]
        
        return 'tie' if board_full else None
  
    def print_board(self):
        print('')
        for row in self.state:
            row_string = ''
            for space in row:
                if space == None:
                    row_string += '_ '
                else:
                    row_string += str(space) + ' '
            print(row_string[:-1])
        print('')