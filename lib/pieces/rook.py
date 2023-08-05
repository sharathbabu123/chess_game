from lib.pieces.piece import Piece


class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = 'R' if self.color == 'white' else 'r'
        if color == 'white':
            self.image_path = "C:/Users/shara/Desktop/Bored/August 2023/chess_game/assets/white_rook.png"
        else:
            self.image_path = "C:/Users/shara/Desktop/Bored/August 2023/chess_game/assets/black_rook.png"

    def valid_moves(self, x, y, board):
        moves = []

        # Check upwards (decreasing x)
        for i in range(x-1, -1, -1):
            if not board.is_empty(i, y):
                if board.get_piece(i, y).color != self.color:
                    moves.append((i, y))
                break
            moves.append((i, y))

        # Check downwards (increasing x)
        for i in range(x+1, 8):
            if not board.is_empty(i, y):
                if board.get_piece(i, y).color != self.color:
                    moves.append((i, y))
                break
            moves.append((i, y))

        # Check left (decreasing y)
        for j in range(y-1, -1, -1):
            if not board.is_empty(x, j):
                if board.get_piece(x, j).color != self.color:
                    moves.append((x, j))
                break
            moves.append((x, j))

        # Check right (increasing y)
        for j in range(y+1, 8):
            if not board.is_empty(x, j):
                if board.get_piece(x, j).color != self.color:
                    moves.append((x, j))
                break
            moves.append((x, j))

        return moves
