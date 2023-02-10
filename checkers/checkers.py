import random, time, sys
sys.path.append("./global_functions.py")
from global_functions import *

class Checkers:
    
    def __init__(self, players):

        self.players = players
        self.set_player_nums()

        self.state = [
            [0, 2, 0, 2, 0, 2, 0, 2],
            [2, 0, 2, 0, 2, 0, 2, 0],
            [0, 2, 0, 2, 0, 2, 0, 2],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0],
        ]

        self.player_turn = 1
        self.winner = None

    def set_player_nums(self):
        self.players[0].set_player_num(1)
        self.players[1].set_player_num(2)

    def run_to_completion(self):

        while self.winner == None:

            for player in self.players:

                possible_moves = self.get_all_possible_moves(player, self.state)
                first_time = True

                if possible_moves == []:
                    self.winner = 3 - player.player_num
                    break

                # check if they haven't moved yet OR they can move again

                while first_time or len(possible_moves) > 1:

                    # choose move

                    move = player.choose_move(self.state, possible_moves, first_time)
                    if move == None: move = random.choice(possible_moves)

                    # update board and winner

                    self.update_state(player, move)
                    
                    self.winner = self.check_for_winner()
                    if self.winner: break

                    # if they captured on their 1st move, allow player to move again

                    first_time = False

                    if move[2] != []:
                        new_coords = translate(move[0], move[1])
                        possible_moves = self.get_possible_moves_for_piece(player, new_coords, self.state, first_time)
                    else:
                        possible_moves = []

            self.player_turn += 1

    def get_all_possible_moves(self, player, state):
        
        possible_moves = []

        for i in range(8):
            for j in range(8):
                if abs(state[i][j]) == player.player_num:
                    possible_moves += self.get_possible_moves_for_piece(player, [i, j], state)
        
        return possible_moves
    
    def get_possible_moves_for_piece(self, player, coord, state, first_time=True):
        
        # get translations to check

        piece = state[coord[0]][coord[1]]
        d = 1 - 2*(piece % 2)

        translations_to_check = [[d, -1], [d, 1]]
        if piece < 0: translations_to_check += [[-d, -1], [-d, 1]]

        possible_moves = []

        # add option to NOT chain capture

        if not first_time:
            possible_moves.append([coord, [0, 0], []])

        # loop through translations

        for translation_to_check in translations_to_check:

            # check if the new spot is empty

            new_i, new_j = translate(coord, translation_to_check)
            if new_i < 0 or new_i > 7 or new_j < 0 or new_j > 7: continue
            new_piece = state[new_i][new_j]

            if abs(new_piece) == 0 and first_time:
                possible_moves.append([coord, translation_to_check, []])
        
            # check if the opponent is in the new spot

            elif abs(new_piece) == 3 - player.player_num:
                
                # check if the next next spot is empty

                next_translation = [2*t for t in translation_to_check]
                new_new_i, new_new_j = translate(coord, next_translation)
                if new_new_i < 0 or new_new_i > 7 or new_new_j < 0 or new_new_j > 7: continue
                new_new_piece = state[new_new_i][new_new_j]

                # add capture to possible moves

                if abs(new_new_piece) == 0:
                    possible_moves.append([coord, next_translation, [new_i, new_j]])
        
        return possible_moves

    def update_state(self, player, move):

        current_coords, translation, captured_coord = move
        new_coords = translate(current_coords, translation)

        if translation == [0, 0]: return

        self.state[new_coords[0]][new_coords[1]] = self.state[current_coords[0]][current_coords[1]] # set new coord to the old coord's piece
        self.state[current_coords[0]][current_coords[1]] = 0 # set old coord to 0

        if captured_coord != []:
            self.state[captured_coord[0]][captured_coord[1]] = 0 # set captured coords to 0
        
        # turn pieces into kings

        p1_piece_should_be_king = (player.player_num == 1 and new_coords[0] == 0 and self.state[new_coords[0]][new_coords[1]] > 0)
        p2_piece_should_be_king = (player.player_num == 2 and new_coords[0] == 7 and self.state[new_coords[0]][new_coords[1]] > 0)

        if p1_piece_should_be_king or p2_piece_should_be_king:
            self.state[new_coords[0]][new_coords[1]] *= -1

    def check_for_winner(self):
        
        flattened_state = [piece for row in self.state for piece in row]
        all_pieces = [abs(piece) for piece in flattened_state if piece != 0]

        p1_count = all_pieces.count(1)
        p2_count = all_pieces.count(2)

        if p1_count == 0: return 2
        if p2_count == 0: return 1
        if p1_count == 1 and p2_count == 1: return 'tie'

        return None

    def find_translation(self, coord1, coord2):
        return [coord1[0] - coord2[0], coord1[1] - coord2[1]]