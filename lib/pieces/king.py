from lib.pieces.piece import Piece


class King(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = 'K' if self.color == 'white' else 'k'
        if color == 'white':
            self.image_path = "C:/Users/shara/Desktop/Bored/August 2023/chess_game/assets/white_king.png"
        else:
            self.image_path = "C:/Users/shara/Desktop/Bored/August 2023/chess_game/assets/black_king.png"

    def valid_moves(self, x, y, board):
        moves = []

        # Define all potential moves the king can make
        potential_moves = [
            (x + 1, y),     # Down
            (x - 1, y),     # Up
            (x, y + 1),     # Right
            (x, y - 1),     # Left
            (x + 1, y + 1), # Down-Right
            (x + 1, y - 1), # Down-Left
            (x - 1, y + 1), # Up-Right
            (x - 1, y - 1)  # Up-Left
        ]

        # Check each potential move
        for move in potential_moves:
            i, j = move
            if 0 <= i < 8 and 0 <= j < 8:  # Check if the move is inside the board
                if board.is_empty(i, j) or board.get_piece(i, j).color != self.color:
                    moves.append(move)

        # TODO: Implement castling logic here

        return moves
