import matplotlib.pyplot as plt # Importing matplotlib
import pylab # Importing pylab
import numpy as np # Importing numpy
import random # Importing random module
class PuzzlePiece: # Creating class named PuzzlePiece
  def __init__(self, x, y): # Defining intialisation method and taking x, y as input
    self.connected_to = [] # Creating an attribute named connected_to as an empty list
    self.secret_id = (x,y) # Creating an attribute named secret_id and setting its value as a tuple (x,y)

  def __str__(self): # Defining str method
    str_repr =  "{},{}".format(self.secret_id[0], self.secret_id[1]) # String representation of tuple
    return str_repr

class Puzzle: # Creating class named Puzzle
  def __init__(self): # Defining intialisation method 
    self.u_piece = [] # Creating an attribute named u_piece as an empty list which will have all unsolved pieces
    self.s_piece = []   # Creating an attribute named s_piece as an empty list which will have all solved pieces
    for i in range(10):
      for j in range(10):
        self.u_piece.append(PuzzlePiece(i,j))

  def get_rand_piece(self): # Defining get_rand_piece method
    rand_piece = random.choice(self.u_piece) # Generatin a random piece
    return rand_piece

  def solve_one_piece(self, rand_piece):
    """1. The function takes in one argument: rand_piece, the random piece generated
    The function then checks if the length of s_piece is less than or equal to 100.
    If the length of s_piece is less than or equal to 100, then the function checks if rand_piece is in s_piece""" 
    while len(self.s_piece) <= 100: # Checking if the length of s_piece 
      # rand_piece = random.choice(self.u_piece)
      if rand_piece not in self.s_piece: # Checking if the random generated piece is in s_piece
        self.s_piece.append(rand_piece) # Appending rand_piece to s_piece
        self.u_piece.remove(rand_piece) # Removing rand_piece from u_piece
        self.s_piece = self.connected_to # Setting connected_to attribute

  def solve_all_pieces(self):
    """ The function takes in one argument: self, the object of the class.
    The function then creates a list of tuples that represents the u_pieces.
    The function then checks a lists that represents the s_pieces.
    The function then randomly selects a piece from the u_pieces list checking if it can fit s_piece.
    The function then removes"""
    for i in range(10): # For loop to iterate through the range of 10.
        for j in range(10): 
            self.u_piece.append((i, j)) # Adds the tuple (i, j) to the list u_piece.

    for i in range(10): # For loop to iterate through the range of 10.
        temp = [] # Creating empty list temp
        for j in range(10): # For loop to iterate through the range of 10.
            temp.append(()) # Appends an empty tuple to the list temp.
        self.s_piece.append(temp) # Appends the value of temp to the list s_piece.

   
    rand_piece = random.choice(self.u_piece) # Chooses a random piece from the list of unplaced pieces
    self.u_piece.remove(rand_piece) # Removes that piece from the list of unplaced pieces.
    self.s_piece[rand_piece[1]][rand_piece[0]] = rand_piece # Then places that piece in the list of placed pieces.


    def print_solved():
        """1. The function takes in no arguments.
        The function then prints out the solved puzzle.
        The function then removes the random piece from the list of unused pieces.
        The function then checks if the random piece can be placed next to the current piece.
        If the random piece can be placed next to the current piece,"""
        for i in range(10):
            for j in range(10): 
                print(f"{str(self.s_piece[i][j]):<10}", end= "") #  The function returns n multiplied by the factorial of n minus 1.
            print() # Prints a blank line to the console.

    def fun_remove(rand_piece):
        """The function takes in one argument: rand_piece, the piece to be removed from the list
        The function then tries to remove rand_piece from the list
        If rand_piece is not in the list, then the function does nothing."""
        try:
            self.u_piece.remove(rand_piece)
        except:
            pass

    while len(self.u_piece) != 0:
        """The code uses a while loop to iterate through the list "u_piece" until it is empty.
        The code then chooses a random piece from the list "u_piece" and stores it in the variable "rand_piece".
        The code then iterates through the list "s_piece" and connects the rand_piece if it can be connected"""
        rand_piece = random.choice(self.u_piece)
        for i in range(10):
            for j in range(10): 
                if len(self.s_piece[i][j]) > 0: # Checks if the length of the string at the index i, j of the list s_piece is greater than 0.
                    current_tuple = self.s_piece[i][j] # Accesses the i-th element of the j-th element of the list s_piece.
                    x = current_tuple[0] # Assigns the value of the first element in the tuple "current_tuple" to the variable "x".
                    y = current_tuple[1] # Assigns the second element of the tuple "current_tuple" to the variable "y".
                    new_x = rand_piece[0] # Assigns the value of the first element in the new rand_piece tuple to the variable "new_x".
                    new_y = rand_piece[1] # Assigns the value of the second element in the new rand_piece tuple to the variable "new_y".
                if new_x == x - 1 and new_y == y: # The code checks if new_x is equal to x minus 1 and if new_y is equal to y.
                    self.s_piece[i][j - 1] = rand_piece
                    fun_remove(rand_piece)
                if new_x == x + 1 and new_y == y: # The code checks if new_x is equal to x + 1 and new_y is equal to y.
                    self.s_piece[i][j + 1] = rand_piece
                    fun_remove(rand_piece)
                if new_y == y - 1 and new_x == x: # The code checks if new_y is equal to y minus 1 and new_x is equal to x.
                    self.s_piece[i -1][j] = rand_piece
                    fun_remove(rand_piece)
                if new_y == y + 1 and new_x == x: # The code checks if the new y value is equal to the old y value plus 1 and if the new x value is equal to the old x value.
                    self.s_piece[i + 1][j] = rand_piece
                    fun_remove(rand_piece)
    print_solved() # The function prints "s_piece" to the console.
    self.connected_to = self.s_piece # Sets the connected_to attribute of the current object to the s_piece attribute of the current object.
    return self.s_piece

  def solution_graph(self):
    """1. The function takes in one argument: self, the object
    The function then creates a list of tuples from the s_piece attribute of the object.
    The function then creates a scatterplot from the first and second elements of the s_piece attribute of the object.
    The function then displays the scatterplot."""
    list1 = list(zip(*self.s_piece)) # The code takes in a list of tuples and transposes it. The code then returns the transposed list of tuples.
    pylab.scatter(list(self.s_piece[0]),list(self.s_piece[1])) # The code plots a scatter plot of the first and second columns of the dataframe self.s_piece.
    pylab.plot()
    pylab.show()
    pylab.savefig("puzzle")


        
    
    
