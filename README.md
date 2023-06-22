# Puzzle-using-OOP


This is a Python project using Object Oriented Programming to solve all the puzzle pieces.


## Functions in this code
def __init__(self, x, y): # Defining intialisation method and taking x, y as input

__str__(self): # Defining str method

get_rand_piece(self): # Defining get_rand_piece method

solve_one_piece(self, rand_piece): The function takes in one argument: rand_piece, the random piece generated. The function then checks if the length of s_piece is less than or equal to 100. If the length of s_piece is less than or equal to 100, then the function checks if rand_piece is in s_piece

solve_all_pieces(self):
    The function takes in one argument: self, the object of the class.
    The function then creates a list of tuples that represents the u_pieces.
    The function then checks a lists that represents the s_pieces.
    The function then randomly selects a piece from the u_pieces list checking if it can fit s_piece.
    The function then removes

print_solved():
        The function takes in no arguments.
        The function then prints out the solved puzzle.
        The function then removes the random piece from the list of unused pieces.
        The function then checks if the random piece can be placed next to the current piece.
        If the random piece can be placed next to the current piece

fun_remove(rand_piece):
        The function takes in one argument: rand_piece, the piece to be removed from the list
        The function then tries to remove rand_piece from the list
        If rand_piece is not in the list, then the function does nothing.
        
solution_graph(self):
    1. The function takes in one argument: self, the object
    The function then creates a list of tuples from the s_piece attribute of the object.
    The function then creates a scatterplot from the first and second elements of the s_piece attribute of the object.
    The function then displays the scatterplot.

## Modules used
matplotlib.pyplot

pylab

numpy

random


