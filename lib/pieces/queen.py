from lib.pieces.piece import Piece


class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = 'Q' if self.color == 'white' else 'q'
        if color == 'white':
            self.image_path = "C:/Users/shara/Desktop/Bored/August 2023/chess_game/assets/white_queen.png"
        else:
            self.image_path = "C:/Users/shara/Desktop/Bored/August 2023/chess_game/assets/black_queen.png"

    def valid_moves(self, x, y, board):
        moves = []

        # Rook-like moves (horizontal and vertical)
        
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

        # Bishop-like moves (diagonals)
        
        # Check top-right diagonal (increasing x and y)
        i, j = x + 1, y + 1
        while i < 8 and j < 8:
            if not board.is_empty(i, j):
                if board.get_piece(i, j).color != self.color:
                    moves.append((i, j))
                break
            moves.append((i, j))
            i += 1
            j += 1

        # Check bottom-left diagonal (decreasing x and y)
        i, j = x - 1, y - 1
        while i >= 0 and j >= 0:
            if not board.is_empty(i, j):
                if board.get_piece(i, j).color != self.color:
                    moves.append((i, j))
                break
            moves.append((i, j))
            i -= 1
            j -= 1

        # Check top-left diagonal (increasing x, decreasing y)
        i, j = x + 1, y - 1
        while i < 8 and j >= 0:
            if not board.is_empty(i, j):
                if board.get_piece(i, j).color != self.color:
                    moves.append((i, j))
                break
            moves.append((i, j))
            i += 1
            j -= 1

        # Check bottom-right diagonal (decreasing x, increasing y)
        i, j = x - 1, y + 1
        while i >= 0 and j < 8:
            if not board.is_empty(i, j):
                if board.get_piece(i, j).color != self.color:
                    moves.append((i, j))
                break
            moves.append((i, j))
            i -= 1
            j += 1

        return moves
