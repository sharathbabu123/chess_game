from lib.pieces.piece import Piece


class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = 'N' if self.color == 'white' else 'n'
        if color == 'white':
            self.image_path = "C:/Users/shara/Desktop/Bored/August 2023/chess_game/assets/white_knight.png"
        else:
            self.image_path = "C:/Users/shara/Desktop/Bored/August 2023/chess_game/assets/black_knight.png"

    def valid_moves(self, x, y, board):
        moves = []
        
        # Define all potential "L" moves a knight can make
        potential_moves = [
            (x + 1, y + 2),
            (x + 1, y - 2),
            (x - 1, y + 2),
            (x - 1, y - 2),
            (x + 2, y + 1),
            (x + 2, y - 1),
            (x - 2, y + 1),
            (x - 2, y - 1)
        ]

        # Check each potential move
        for move in potential_moves:
            i, j = move
            if 0 <= i < 8 and 0 <= j < 8:  # Check if the move is inside the board
                if board.is_empty(i, j) or board.get_piece(i, j).color != self.color:
                    moves.append(move)

        return moves