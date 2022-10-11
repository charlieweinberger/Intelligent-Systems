import copy, random

class LastMinutePlayer:
    
    def __init__(self):
        self.player_number = None
  
    def set_player_number(self, n):
        self.player_number = n

    def get_choices(self, state):

        choices = []

        for row in state:
            for i, space in enumerate(row):
                if space == None:
                    choices.append(i)
        
        return list(set(choices))

    def choose_move(self, state):
        
        self.print_board(state)
        moves = self.get_choices(state)

        for move in moves:

            capture_win_state = copy.deepcopy(state)
            block_loss_state = copy.deepcopy(state)

            print(f'\n{move = }')

            for i in range(5, -1, -1):
                if state[i][move] == None:
                    capture_win_state[i][move] = self.player_number
                    block_loss_state[i][move] = 3 - self.player_number
                    break
                    
            print('capture win state')
            self.print_board(capture_win_state)
            self.check_for_winner(capture_win_state, print_winner=True)

            print('block loss state')
            self.print_board(block_loss_state)
            self.check_for_winner(block_loss_state, print_winner=True)
            
            if self.check_for_winner(capture_win_state) or self.check_for_winner(block_loss_state):
                return move

        return random.choice(moves)

    def check_for_winner(self, state, print_winner=False):

        four_in_a_row = []

        for i in range(6):
            for j in range(4):
                row = [state[i][j + k] for k in range(4)]
                four_in_a_row.append(row)

        for i in range(3):
            for j in range(7):
                column = [state[i + k][j] for k in range(4)]
                four_in_a_row.append(column)
        
        for i in range(3):
            for j in range(4):
                forward_diag = [state[i + k][j + k] for k in range(4)]
                four_in_a_row.append(forward_diag)
        
        for i in range(3):
            for j in range(3, 7):
                backward_diag = [state[i + k][j - k] for k in range(4)]
                four_in_a_row.append(backward_diag)

        board_full = True
        for row in four_in_a_row:
            
            if None in row:
                board_full = False

            if len(set(row)) == 1 and row[0] != None:
                if print_winner: print(f'winner: {row[0]}')
                return row[0]
        
        return 'tie' if board_full else None

    def print_board(self, state):
        print('')
        for row in state:
            row_string = ''
            for space in row:
                if space == None:
                    row_string += '_ '
                else:
                    row_string += str(space) + ' '
            print(row_string[:-1])
        print('')