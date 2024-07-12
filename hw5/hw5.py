"""
CMSC 14100
Summer 2024
Homework #5

YOUR NAME HERE

People Consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URLs of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.
"""

class Board:
    """
    A class to represent a game board. 
    """
    def __init__(self, target=4, height=6, width=7):
        ### YOUR CODE HERE
        pass # delete pass

    def __str__(self):
        ### YOUR CODE HERE
        pass # delete pass

    def drop_marker(self, col, marker):
        ### YOUR CODE HERE
        pass # delete pass

    def check_end(self):
        ### YOUR CODE HERE
        pass # delete pass

    # Other methods can go here


class Player:
    """
    A class to represent a player of our game. 
    """
    def __init__(self, name, marker):
        """
        Constructor

        Inputs: 
            name [string]: The name of the player
            marker [string]: The marker that the player uses
                            in the game. (Works best with just
                            one character like "X" or "O").

        Creates an instance of Player with the
            inputs as attributes.
        """
        self.name = name
        self.marker = marker

    def make_move(self, board, column):
        """
        Simulates the player making a move with the given board. They are adding
            a piece to the given board at the given column. Only valid moves 
            will be allowed. 

        Inputs: 
            board [Board]: The board for which the player is trying to add a
                piece. 
            column [int]: The column on the board for which the player is 
                trying to add a piece. 
            
        Returns [None]: Nothing is returned. The board is modified in-place.
        """
        if column >= board.width or column < 0:
            print(f"Column must be between 0 and {board.width - 1}."
                  + " Please try again.")
        else: 
            if board.drop_marker(column, self.marker):
                if board.check_end():      
                    print(f"{self.name} wins! (Board cleared)")
            else:
                print("Column is full. Please choose another column.")           
