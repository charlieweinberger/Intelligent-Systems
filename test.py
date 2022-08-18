board = [['0', '1', '2'], ['2', '1', '1'], ['1', '0', '2']]

print('')
for i in range(len(board)):
    row_string = ''
    for space in board[i]:
        if space == None:
            row_string += '_|'
        else:
            row_string += space + '|'
    print(row_string[:-1])

board_2 = '000101200'

print('')
for i in range(3):
    row_string = ''
    for j in range(3):
        for piece in board_2[3*i + j]:
            row_string += ' |' if piece == '0' else f'{piece}|'
    print(row_string[:-1])