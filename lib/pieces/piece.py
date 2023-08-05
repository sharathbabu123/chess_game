# pieces.py
from tkinter import PhotoImage


class Piece:
    def __init__(self, color):
        self.color = color
        self.image = None

    def load_image(self):
        """Load the image for the piece."""
        if self.image_path:
            self.image = PhotoImage(file=self.image_path)
            # print(self.image.width(), self.image.height())


    def valid_moves(self, x, y, board):
        raise NotImplementedError

    def __str__(self):
        return self.symbol














# If needed, you can also add any utility functions or classes for specific chess variants or rules.
