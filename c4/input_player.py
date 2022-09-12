class InputPlayer:
    
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
        
        answer = input(f'\nYou are player {self.player_number}.\nIn which column do you want to place a piece? ')

        if answer in '1234567':
            choice = int(answer) - 1
        else:
            print('That move is not valid! Please try again.')
            return self.choose_move(state)

        if choice not in self.get_choices(state):
            print('That move is not valid! Please try again.')
            return self.choose_move(state)
        
        return choice

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