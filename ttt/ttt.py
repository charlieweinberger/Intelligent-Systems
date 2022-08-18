# convert '000000000' back to [['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']] everywhere
# test ttt.py

class TicTacToe:
    def __init__(self, players, second_player_first, see_board=False):
        self.players = players
        self.second_player_first = second_player_first
        self.see_board = see_board
        self.set_player_symbols()
        self.set_player_numbers()
        self.determine_player_order()
        self.state = '000000000'
        self.round = 1
        self.winner = None
    
    def set_player_symbols(self): 
        self.players[0].set_player_symbol('X')
        self.players[1].set_player_symbol('O')

    def set_player_numbers(self): 
        self.players[0].set_player_number(1)
        self.players[1].set_player_number(2)
    
    def determine_player_order(self):
        if self.second_player_first:
            self.players = self.players[::-1]

    def get_possible_moves(self):
        return [i for i in range(9) if self.state[i] == '0']

    def complete_round(self):

        for player in self.players:

            choices = self.get_possible_moves()

            if choices != []:
                move = player.choose_move(choices)
                self.state = self.state[0:move] + player.symbol + self.state[move + 1:]

            if self.check_for_winner() != '0':
                self.winner = self.check_for_winner()
                break

            if self.see_board:
                self.print_board()

        self.round += 1

    def run_to_completion(self):
        while self.winner == None:
            self.complete_round()

    def check_for_winner(self):

        three_in_a_row = [
            f'{self.state[0]}{self.state[1]}{self.state[2]}',
            f'{self.state[3]}{self.state[4]}{self.state[5]}',
            f'{self.state[6]}{self.state[7]}{self.state[8]}',
            f'{self.state[0]}{self.state[3]}{self.state[6]}',
            f'{self.state[1]}{self.state[4]}{self.state[7]}',
            f'{self.state[2]}{self.state[5]}{self.state[8]}',
            f'{self.state[0]}{self.state[4]}{self.state[8]}',
            f'{self.state[2]}{self.state[4]}{self.state[6]}'
        ]

        board_full = True
        for row in three_in_a_row:
            
            if '0' in row:
                board_full = False

            for player in ['1', '2']:
                if row == 3*player:
                    return player
        
        return 'tie' if board_full else '0'

    def print_board(self):
        print('')
        for i in range(3):
            row_string = ''
            for j in range(3):
                for piece in board_2[3*i + j]:
                    row_string += ' |' if piece == '0' else f'{piece}|'
            print(row_string[:-1])