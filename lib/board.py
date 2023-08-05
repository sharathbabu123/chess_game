from lib.pieces.pawn import Pawn
from lib.pieces.rook import Rook
from lib.pieces.queen import Queen
from lib.pieces.king import King
from lib.pieces.knight import Knight
from lib.pieces.bishop import Bishop

from tkinter import PhotoImage


class Board:
    def __init__(self):
        self.board = self.initialize_board()

    def initialize_board(self):
        # 8x8 board initialized with None values
        board = [[None for _ in range(8)] for _ in range(8)]

        # Set up the initial positions for the pawns
        for i in range(8):
            board[1][i] = Pawn('black')
            board[6][i] = Pawn('white')

        # Set up the initial positions for the Rooks
        board[0][0], board[0][7] = Rook('black'), Rook('black')
        board[7][0], board[7][7] = Rook('white'), Rook('white')

        # Set up the initial positions for the Knights
        board[0][1], board[0][6] = Knight('black'), Knight('black')
        board[7][1], board[7][6] = Knight('white'), Knight('white')

        # Set up the initial positions for the Bishops
        board[0][2], board[0][5] = Bishop('black'), Bishop('black')
        board[7][2], board[7][5] = Bishop('white'), Bishop('white')

        # Set up the initial positions for the Queens
        board[0][3] = Queen('black')
        board[7][3] = Queen('white')

        # Set up the initial positions for the Kings
        board[0][4] = King('black')
        board[7][4] = King('white')

        self.white_turn = True

        return board


    def display(self):
        for row in self.board:
            for piece in row:
                print(piece if piece else '.', end=' ')
            print()

    def move_piece(self, start_x, start_y, end_x, end_y):
        piece = self.board[start_x][start_y]

        # Check if starting square has a piece of the correct color
        if not piece:
            print("There's no piece on the starting square!")
            return

        if (piece.color == 'white' and self.white_turn) or (piece.color == 'black' and not self.white_turn):

            # Validate if move is within the piece's valid moves
            valid_moves = piece.valid_moves(start_x, start_y, self)

            

            if (end_x, end_y) not in valid_moves:
                print("This move is not valid for this piece!")
                return

            # Ensure the ending square doesn't have a piece of the same color
            target = self.board[end_x][end_y]
            if target and target.color == piece.color:
                print("You can't capture your own piece!")
                return
            
            if isinstance(piece, Pawn):

                # If the move is a vertical move of 1 step but the target square is empty (i.e., en passant condition)
                if abs(start_x - end_x) == 1 and self.board[end_x][end_y] is None:

                    # Remove the opponent pawn
                    # For a white pawn, the opponent pawn will be one square below the current position
                    if piece.color == 'white':
                        self.board[start_x][end_y] = None

                    # For a black pawn, the opponent pawn will be one square above the current position
                    else:
                        self.board[start_x][end_y] = None

            # If all validations pass, make the move
            self.board[end_x][end_y] = piece
            self.board[start_x][start_y] = None

            


            if(piece.color == 'white' and isinstance(piece, Pawn) ):
                if(start_x == end_x + 2):
                    
                    piece.first_move = False
                    self.update_pawns_double_moved_status(piece.color)
                    piece.just_double_moved = True
                    # piece.just_double_moved = False

            if(piece.color == 'black' and isinstance(piece, Pawn) ):
                if(start_x == end_x - 2):
                    
                    piece.first_move = False
                    self.update_pawns_double_moved_status(piece.color)
                    piece.just_double_moved = True
                    # piece.just_double_moved = False


            if self.is_in_check(piece.color):
                self.board[end_x][end_y] = None
                self.board[start_x][start_y] = piece
                print("Invalid Move!! The king is in check")
                return

            # Flip the turn
            self.white_turn = not self.white_turn

            # if the move puts the same player in check
            

            # Check if the move puts the other player in check or checkmate
            other_color = 'white' if piece.color == 'black' else 'black'
            if self.is_in_check(other_color):
                if self.is_checkmate(other_color):
                    print(f"{other_color} is in checkmate!")
                    # TODO: End the game here
                else:
                    print(f"{other_color} is in check!")
        else:
            print("It's not your turn!")

    def update_pawns_double_moved_status(self,color):
        for x in range(8):
            for y in range(8):
                piece = self.board[x][y]
                if isinstance(piece, Pawn) and piece.just_double_moved and piece.color == color:
                    piece.just_double_moved = False

    def is_empty(self, x, y):
        return self.board[x][y] is None

    def get_piece(self, x, y):
        return self.board[x][y]

    def is_in_check(self, color):
            king_position = self.find_king(color)
            for x in range(8):
                for y in range(8):
                    piece = self.get_piece(x, y)
                    if piece and piece.color != color:
                        if king_position in piece.valid_moves(x, y, self):
                            return True
            return False

    def find_king(self, color):
            for x in range(8):
                for y in range(8):
                    piece = self.get_piece(x, y)
                    if piece and isinstance(piece, King) and piece.color == color:
                        return (x, y)
            return None  # Shouldn't happen

    def is_checkmate(self, color):
            if not self.is_in_check(color):
                return False

            for x in range(8):
                for y in range(8):
                    piece = self.get_piece(x, y)
                    if piece and piece.color == color:
                        for move in piece.valid_moves(x, y, self):
                            # Make a hypothetical move
                            old_piece = self.get_piece(*move)
                            self.board[move[0]][move[1]] = piece
                            self.board[x][y] = None

                            # Check if we're still in check after the move
                            if not self.is_in_check(color):
                                # Undo the hypothetical move
                                self.board[x][y] = piece
                                self.board[move[0]][move[1]] = old_piece
                                return False
                            
                            # Undo the hypothetical move
                            self.board[x][y] = piece
                            self.board[move[0]][move[1]] = old_piece

            return True
    
    