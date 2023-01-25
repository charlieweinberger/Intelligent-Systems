import random, time

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

                possible_moves = self.get_possible_moves(player)

                if possible_moves == []:
                    self.winner = 3 - player.player_num
                    break

                move = player.choose_move(self.state, possible_moves)
                if move == None: move = random.choice(possible_moves)

                self.update_state(player, move)
                
                self.winner = self.check_for_winner()
                if self.winner: break
        
            self.player_turn += 1

    def get_possible_moves(self, player, state=None):
        
        if state == None: state = self.state

        possible_moves = []

        # loop through all coordinates

        for i in range(8):
            for j in range(8):

                current_coords = [i, j]
                current_piece = state[i][j]

                # check if there is a piece on the current coord

                if abs(current_piece) == player.player_num:

                    # get moves that the piece might be able to do

                    moves_to_check = self.add_moves_to_check(current_piece, current_coords, [], [])

                    while len(moves_to_check) > 0:

                        # check first move in moves_to_check

                        move_to_check = moves_to_check.pop(0) # moves_to_check is a queue
                        coord, translation_to_check, captured_coords = move_to_check

                        new_i, new_j = self.translate(coord, translation_to_check)
                        if new_i < 0 or new_i > 7 or new_j < 0 or new_j > 7: continue
                        new_piece = state[new_i][new_j]

                        # check if the new spot is empty

                        if abs(new_piece) == 0 and captured_coords == []:
                            possible_moves.append(move_to_check)
                    
                        # check if the opponent is in the new spot

                        elif abs(new_piece) == 3 - player.player_num:
                            
                            # if so, and if the next next spot is empty, add that spot to moves_to_check

                            next_translation = [2*t for t in translation_to_check]
                            new_new_i, new_new_j = self.translate(coord, next_translation)
                            if new_new_i < 0 or new_new_i > 7 or new_new_j < 0 or new_new_j > 7: continue
                            new_new_piece = state[new_new_i][new_new_j]

                            if abs(new_new_piece) == 0 and not self.nested_list_in_list(captured_coords, [new_i, new_j]):

                                # add capture to possible moves

                                previous_translation = self.find_translation(coord, current_coords)
                                new_translation = self.translate(previous_translation, next_translation)
                                new_captured_coords = captured_coords + [[new_i, new_j]]
                                possible_moves.append([current_coords, new_translation, new_captured_coords])

                                # add potential to combo captures

                                next_next_coords = self.translate(current_coords, new_translation)
                                moves_to_check = self.add_moves_to_check(current_piece, next_next_coords, new_captured_coords, moves_to_check)

                                # then, it'll loop back to the start of moves_to_check
        
        return possible_moves

    def add_moves_to_check(self, current_piece, current_coords, captured_coords, moves_to_check):
        
        direction = 1 - 2*(current_piece % 2)

        moves_to_check.append([current_coords, [direction, -1], captured_coords])
        moves_to_check.append([current_coords, [direction, 1], captured_coords])

        if current_piece < 0:
            moves_to_check.append([current_coords, [-direction, -1], captured_coords])
            moves_to_check.append([current_coords, [-direction, 1], captured_coords])
        
        return moves_to_check

    def update_state(self, player, move):

        current_coords, translation, captured_coords = move
        new_coords = self.translate(current_coords, translation)

        self.state[new_coords[0]][new_coords[1]] = self.state[current_coords[0]][current_coords[1]] # set new coord to the old coord's piece
        self.state[current_coords[0]][current_coords[1]] = 0 # set old coord to 0

        for coords in captured_coords:
            self.state[coords[0]][coords[1]] = 0 # set captured coords to 0
        
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

    def translate(self, coord1, coord2):
        return [coord1[0] + coord2[0], coord1[1] + coord2[1]]

    def find_translation(self, coord1, coord2):
        return [coord1[0] - coord2[0], coord1[1] - coord2[1]]

    def lists_are_equal(self, list1, list2):
        if len(list1) != len(list2): return False
        for i in range(len(list1)):
            if list1[i] != list2[i]: return False
        return True

    def nested_list_in_list(self, parent_list, nested_list):
        for l in parent_list:
            if all(x == y for x, y in zip(l, nested_list)):
                return True
        return False

    def print_state(self):
        print("self.state:")
        for row in self.state:
            print(row)