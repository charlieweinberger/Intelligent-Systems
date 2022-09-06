class InputPlayer:
    
    def __init__(self):
        self.player_number = None
  
    def set_player_number(self, n):
        self.player_number = n

    def update_state(self, state):
        pass

    def choose_move(self, state):
        
        choices = [[i, j] for i in range(3) for j in range(3) if state[i][j] == None]
        self.print_board(state)
        
        choice = [int(elem) for elem in input(f'\nYour move: ') if elem in '012'][::-1]

        if choice not in choices:
            print('That move is not valid! Please try again.')
            return self.choose_move(state)
        
        return choice

    def print_board(self, state):
        print('')
        for row in state:
            row_string = ''
            for space in row:
                if space == None:
                    row_string += '_|'
                else:
                    row_string += str(space) + '|'
            print(row_string[:-1])