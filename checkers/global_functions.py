def print_state(state):

    print("   0 1 2 3 4 5 6 7")

    for i in range(8):

        row_to_print = f"{i} "
        for j in range(8):
            
            elem = state[i][j]

            if elem == 0:  row_to_print += "⬜" if ((i + j) % 2 == 0) else "  "
            if elem == 1:  row_to_print += "🔵"
            if elem == 2:  row_to_print += "🔴"
            if elem == -1: row_to_print += "💙"
            if elem == -2: row_to_print += "❤️ "
        
        print(row_to_print)

def print_moves(moves):
    
    print('\nPossible moves:')
    for i in range(len(moves)):
        print(f'{i}: {print_move(moves[i])}')

def print_move(move):
    
    current_coord, translation, captured_coords = move
    to_print = f'{current_coord} -> {translate(current_coord, translation)}'

    if len(captured_coords) == 1:
        to_print += f' (coords captured: {captured_coords[0]})'
    elif len(captured_coords) > 1:
        
        to_print += f' (coords captured: '
        
        for i in range(len(captured_coords) - 2):
            to_print += f'{captured_coords[i]}, '

        to_print += f'{captured_coords[-2]} and {captured_coords[-1]})'

    return to_print

def translate(coord1, coord2):
    return [coord1[0] + coord2[0], coord1[1] + coord2[1]]