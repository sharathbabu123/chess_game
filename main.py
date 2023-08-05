import tkinter as tk
from tkinter import messagebox
from lib.board import Board
import copy

class ChessGUI(tk.Tk):
    def __init__(self, board,master=None):
        super().__init__()
        self.title('Chess Game')
        self.geometry('420x420')
        
        self.board = board
        self.buttons = [[None for _ in range(8)] for _ in range(8)]

        self.selected_piece_coords = None
        self.previous_states = []
        self.previous_states.append(copy.deepcopy(self.board))
        # self.board.get_piece(0,0).image = PhotoImage(file="path_to_white_pawn_image.png")
        # self.buttons[0][0].config(image=PhotoImage(file="path_to_white_pawn_image.png"))
        # self.load_images()
        self.initialize_ui()

    def load_images(self):
        for x in range(8):
            for y in range(8):
                piece = self.board.get_piece(x, y)
                if piece:
                    piece.load_image()  # Implement a method in the Piece class to load its image

    def initialize_ui(self):
        for x in range(8):
            for y in range(8):
                btn = tk.Button(self, width=4, height=2, command=lambda x=x, y=y: self.on_square_clicked(x, y))
                btn.grid(row=x, column=y)
                self.buttons[x][y] = btn

        self.update_buttons()
    
        # Create a new frame to place the back button, and place this frame below the chess board
        control_frame = tk.Frame(self)
        control_frame.grid(row=8, column=0, columnspan=8)
        
        back_button = tk.Button(control_frame, text="Back", command=self.undo_last_move)
        back_button.pack(side=tk.LEFT)

        for x in range(8):
            for y in range(8):
                color = "white" if (x + y) % 2 == 0 else "grey"
                self.buttons[x][y].config(bg=color)

        



    def update_buttons(self):
        
        for x in range(8):
            for y in range(8):
                piece = self.board.get_piece(x, y)
                if piece:
                    self.buttons[x][y].config(text=str(piece))
                else:
                    self.buttons[x][y].config(text='')

    def undo_last_move(self):
        if self.previous_states:
            self.previous_states.pop()
            self.board = self.previous_states.pop()
            # Flip the turn back
            

            self.previous_states.append(copy.deepcopy(self.board))
            # self.board.white_turn = not self.board.white_turn
            # Update your board's GUI
            self.update_buttons()

    def on_square_clicked(self, x, y):
        # self.reset_highlights()
        
        if self.selected_piece_coords:

            self.reset_highlights()
            # Make a move
            start_x, start_y = self.selected_piece_coords
            piece = self.board.get_piece(start_x, start_y)

            # Check if it's the correct player's turn
            if (piece.color == 'white' and self.board.white_turn) or (piece.color == 'black' and not self.board.white_turn):
                if (x, y) in piece.valid_moves(start_x, start_y, self.board):
                    self.board.move_piece(start_x, start_y, x, y)
                    self.selected_piece_coords = None
                    self.previous_states.append(copy.deepcopy(self.board))
                    self.update_buttons()
                else:
                    self.reset_highlights()
                    messagebox.showerror("Invalid Move", "That move is not valid.")
                    self.selected_piece_coords = None
                    
            else:
                self.reset_highlights()
                color_turn = "White" if self.board.white_turn else "Black"
                messagebox.showerror("Wrong Turn", f"It's {color_turn}'s turn!")
                self.selected_piece_coords = None
                # self.reset_highlights()
        else:
            piece = self.board.get_piece(x, y)
            # Ensure that a piece of the correct color is selected based on the turn
            if piece and ((piece.color == 'white' and self.board.white_turn) or (piece.color == 'black' and not self.board.white_turn)):
                self.selected_piece_coords = (x, y)
            else:
                color_turn = "White" if self.board.white_turn else "Black"
                messagebox.showwarning("Wrong Piece", f"Please select a {color_turn} piece.")
            if piece and self.selected_piece_coords:  # Only highlight if there's a piece on the square
                valid_moves = piece.valid_moves(x, y, self.board)
                self.highlight_valid_moves(valid_moves)    

    def highlight_valid_moves(self, valid_moves):
                for (x, y) in valid_moves:
                    self.buttons[x][y].config(bg="yellow")  # Change the color to yellow for highlighted squares

    def reset_highlights(self):
        for x in range(8):
            for y in range(8):
                color = "white" if (x + y) % 2 == 0 else "grey"
                self.buttons[x][y].config(bg=color)


if __name__ == "__main__":
    # root = tk.Tk()
    board = Board()
    app = ChessGUI(board)
    app.mainloop()
    # tk.PhotoImage(file="path_to_white_pawn_image.png")
