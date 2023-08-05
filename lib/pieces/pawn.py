from lib.pieces.piece import Piece
from lib.pieces.queen import Queen



class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = 'P' if self.color == 'white' else 'p'
        if color == 'white':
            self.image_path = "C:/Users/shara/Desktop/Bored/August 2023/chess_game/assets/white_pawn.png"
        else:
            self.image_path = "C:/Users/shara/Desktop/Bored/August 2023/chess_game/assets/black_pawn.png"
        self.first_move = True
        self.just_double_moved = False # To track if the pawn just moved two squares


    def valid_moves(self, x, y, board):
        # print("Inside Valid moves")
        moves = []
        capture_offsets = []

        

        if self.color == 'white':

            # Move forward
            if x - 1 >= 0 and board.is_empty(x-1, y):
                
                moves.append((x-1, y))
                
                

            # Double move if it's the first move for the pawn
                if self.first_move and board.is_empty(x-2, y):
                        
                    moves.append((x-2, y))
                    # self.just_double_moved = True
                    # self.first_move = False                     

            # Capture diagonally
            capture_offsets = [(-1, -1), (-1, 1)]

        else:  # Black pawn 
            # Move forward
            if x + 1 < 8 and board.is_empty(x+1, y):
                moves.append((x+1, y))
                
                # Double move if it's the first move for the pawn
                if self.first_move and board.is_empty(x+2, y):
                    moves.append((x+2, y))
                    # self.just_double_moved = True
                    # self.first_move = False

            # Capture diagonally
            capture_offsets = [(1, -1), (1, 1)]

        for offset in capture_offsets:
            capture_x, capture_y = x + offset[0], y + offset[1]
            if 0 <= capture_x < 8 and 0 <= capture_y < 8 and not board.is_empty(capture_x, capture_y) and board.get_piece(capture_x, capture_y).color != self.color:
                moves.append((capture_x, capture_y))
                
        # Promotion logic
        if self.color == 'white' and x == 0:
            # Here, the pawn can be promoted to a Queen
            # You can create a new Queen instance, but the board won't reflect it yet
            # Add all possible Queen moves to the list
            # Create a temporary Queen to generate moves
            temp_queen = Queen(self.color)
            temp_queen.symbol = 'Q'
            moves.extend(temp_queen.valid_moves(x, y, board))

        elif self.color == 'black' and x == 7:
            # Same logic for the black pawn
            temp_queen = Queen(self.color)
            temp_queen.symbol = 'Q'
            moves.extend(temp_queen.valid_moves(x, y, board))
        
        # En Passant logic
        if ((self.color == 'white' and x == 3) or (self.color == 'black' and x == 4)):
            # Check the squares to the left and right of the pawn
            for adj_y in [y - 1, y + 1]:
                if 0 <= adj_y < 8:
                    adjacent_piece = board.get_piece(x, adj_y)
                    print("checking for possibility")
                    if isinstance(adjacent_piece, Pawn) and adjacent_piece.just_double_moved and adjacent_piece.color != self.color :
                        print("enpassant possible")
                        moves.append((x + int(1 if self.color == 'black' else -1), adj_y))

        # print(moves)
        return moves
    
    