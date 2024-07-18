"""
CMSC 14100
Summer 2024
Homework #6

We will be using anonymous grading, so please do NOT include your name
in this file.

People Consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URLs of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.
"""


# Exercise 1
def find_path(p1, p2):
    """
    Determine whether it is possible traverse from p1 to p2 by
    repeatedly taking positive steps in the x direction and/or 
    positive steps in the y direction.  (One step at a time.)

    Inputs:
        p1 [Tuple[int, int]]: the starting point in cartesian coordinates
        p2 [Tuple[int, int]]: the target point in cartesian coordinates.

    Returns [List[Tuple[int, int]]]: a path from p1 to p2 if one exists;
      None otherwise.
    """
    pass # delete pass as you go


# Exercise 2
def insert_item(item, lst):
    """
    Inserts a given item into a sorted list at the proper location

    Input:
        item [int]: the item to be inserted
        lst [list[int]]: a sorted list
    
    Returns [list[int]]: sorted list containing item and items from lst 
    """
    pass # delete pass as you go


# Exercise 3
def insertion_sort(lst):
    """
    Given a list of integers, produces a list of the same integers in sorted order.

    Input:
        lst [list[int]]: list of integers

    Returns [list[int]]: sorted list of integers 
    """
    pass # delete pass as you go


# Exercise 4
def is_palindrome(s):
    """
    Checks if the input string is a palindrome. That is, whether it reads the same
    forward and backwards. Non-characters are ignored. Capitalization is ignored.

    Inputs: 
        s [str]: a string to check

    Returns [boolean]: True if the letters in s form a palindrome; False otherwise
    """
    assert isinstance(s, str)
    pass # delete pass as you go


# Exercise 5
def sum_pos_leaves(t):
    """
    Calculate the total sum of all the values ignoring leaves with negative values

    Inputs:
        t [Tree]: a non-emty tree

    Returns [int]: the sum value of leaves with positive values.
    """
    pass # delete pass as you go
    

# Exercise 6
def count_less_than_paths(t, target):
    """
    Count the number of root-to-leaf paths where weight of a
    path is strictly less than the specified target weight.

    Inputs:
        t [Tree]: a tree with non-negative values
        target [int]: a non-negative target weight

    Returns [int]: the number of root-to-leaf paths with weights
      strictly less than the target weight.

    """
    assert target >= 0
    pass # delete pass as you go
  

# Exercise 7
def find_max_weight_path(t):
    """
    Find the root-to-leaf path with greates total weight among
    all root-to-leaf paths.

    Inputs:
        t [Tree]: a tree
    
    Returns [List[List[int]]]: a list of paths with weights strictly
      less than the target, where a path is represented by a list of
      node identifiers.
    """
    pass # delete pass as you go



