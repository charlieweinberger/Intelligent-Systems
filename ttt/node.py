class Node():
    def __init__(self, state, player_turn):

        self.state = state
        self.player_turn = player_turn
        self.winner = None
        self.children = None

        self.score = ''

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