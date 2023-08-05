from lib.pieces.piece import Piece

class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = 'B' if self.color == 'white' else 'b'
        if color == 'white':
            self.image_path = "C:/Users/shara/Desktop/Bored/August 2023/chess_game/assets/white_bishop.png"
        else:
            self.image_path = "C:/Users/shara/Desktop/Bored/August 2023/chess_game/assets/black_bishop.png"

    def valid_moves(self, x, y, board):
        moves = []

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
