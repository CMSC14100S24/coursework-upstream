"""
CMSC 14100
Summer 2024
Homework #3

YOUR NAME HERE
Ibrahim
People Consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URL of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.
"""

# Exercise 1
def list_product(numbers):
    """
    Calculate the product for a given list of numbers.

    Inputs:
        numbers [List[int]]: the number of matches

    Returns [int]: the product of all the elements in the list
    """
    product = 1
    for number in numbers:
        product *= number
    return product


# Exercise 2
def first_ten_multiples(a):
    """
    Generate the first ten multiples of the given number 'a'.

    Arguments:
    a (int): The number whose multiples are to be generated.

    Returns:
    list: A list containing the first ten multiples of 'a'.
    """
    multiples = []
    i = 0
    while i < 10:
        multiples.append(i * a)
        i += 1
    return multiples



# Exercise 3
def slice_product(numbers, slice_start, slice_end):
    """
    Calculating the product of elements in the specified slice of a list of numbers.

    Arguments:
    numbers (list of int or float): The list of numbers from which to slice and calculate the product.
    slice_start (int): The starting index (inclusive) of the slice.
    slice_end (int): The ending index (exclusive) of the slice.

    Returns float or int: The product of the elements in the specified slice of 'numbers'.
    """
    if slice_start < 0 or slice_end < 0 or slice_start >= len(numbers) or slice_end >= len(numbers) or slice_start > slice_end:
        return None 
    product = 1
    i = slice_start
    while i <= slice_end:
        product *= numbers[i]
        i += 1
    
    return product


# Exercise 4
def exclaim(some_strings):
    """
    Add an exclamation point ('!') to each string in the list 'some_strings'.

    Arguments:
    some_strings (list of str): A list containing strings to which an exclamation point will be added.

    Returns list of strings: A list where each string from 'some_strings' has an exclamation point added.
    """
    if not some_strings:
        return None
    
    exclaimed_strings = []
    for string in some_strings:
        exclaimed_strings.append(string + '!')
    
    return exclaimed_strings



# Exercise 5
def farthest(original_point, other_points):
    """
    Find the point in 'other_points' that is farthest from 'original_point'.

    Arguments:
    original_point (tuple of float): Coordinates of the original point (x, y).
    other_points (list of tuples of float): List of tuples representing other points [(x1, y1), (x2, y2), ...].

    Returns tuple of float: Coordinates of the point in 'other_points' that is farthest from 'original_point'.
    """
    if not other_points:
        return None
    
    farthest_point = None
    max_distance_sq = -1  

    for point in other_points:
        distance_sq = (point[0] - original_point[0]) ** 2 + (point[1] - original_point[1]) ** 2
        
        if distance_sq > max_distance_sq:
            max_distance_sq = distance_sq
            farthest_point = point

    return farthest_point


# Exercise 6
def did_we_make_it(some_floats, threshold):
    """
    Calculate the sum of numbers in the list, check if the sum meets or exceeds
    the threshold, and determine how far away the sum is from the threshold.
    """
    sum_numbers = sum(some_floats)
    is_above_threshold = sum_numbers >= threshold

    if is_above_threshold:
        if sum_numbers > threshold:
            distance_str = "we made it"
        else:
            distance_str = "right on"
    else:
        difference = threshold - sum_numbers
        if difference <= 0:
            distance_str = "right on"
        elif difference == 1:
            distance_str = "very close"
        elif difference <= 5:
            distance_str = "close"
        else:
            distance_str = "not even close"

    return (sum_numbers, is_above_threshold, distance_str)



# Exercise 7
def contains_duplicate_v1(some_numbers):
    """
    Check if a list of integers contains the same number more than once in a row.

    Arguments:
    some_numbers (list of int): List of integers to check.
    """
    previous_number = None
    
    for num in some_numbers:
        if num == previous_number:
            return True
        previous_number = num
    
    return False



# Exercise 8
def contains_duplicate_v2(some_numbers):
    """
    Check if a list of integers contains the same number more than once in a row.

    Arguments:
    some_numbers (list of int): List of integers to check.
    """
    previous_number = None
    
    for num in some_numbers:
        if previous_number is not None and num == previous_number:
            return True
        previous_number = num
        
    return False


# Exercise 9

from typing import List, Tuple

COLOR_SIMILARITY_THRESHOLD = 10000 

def count_close_colors(img: List[List[Tuple[int, int, int]]], rgb_color: Tuple[int, int, int]) -> int:
    """
    Counts the number of pixels in an image that are close to the target color.
    
    Parameters:
    img (List[List[Tuple[int, int, int]]]): The image represented as a list of lists of RGB colors.
    rgb_color (Tuple[int, int, int]): The target RGB color.
    
    Returns:
    int: The number of pixels in the image that are close to the target color.
    
    Helper Functions:
    color_distance: Computes the squared Euclidean distance between two RGB colors.
    is_close_color: Determines if two RGB colors are close based on a threshold (default is 10000).
    """
    
    def color_distance(color1: Tuple[int, int, int], color2: Tuple[int, int, int]) -> float:
        """
        Computes the squared Euclidean distance between two RGB colors.
        
        Parameters:
        color1 (Tuple[int, int, int]): The first color.
        color2 (Tuple[int, int, int]): The second color.
        
        Returns:
        float: The squared Euclidean distance between the two colors.
        """
        r1, g1, b1 = color1
        r2, g2, b2 = color2
        return (r1 - r2) ** 2 + (g1 - g2) ** 2 + (b1 - b2) ** 2
    
    def is_close_color(color1: Tuple[int, int, int], color2: Tuple[int, int, int], threshold: int = COLOR_SIMILARITY_THRESHOLD) -> bool:
        """
        Determines if two RGB colors are close based on a threshold.
        
        Parameters:
        color1 (Tuple[int, int, int]): The first color.
        color2 (Tuple[int, int, int]): The second color.
        threshold (int): The threshold for closeness based on squared distance.
        
        Returns:
        bool: True if the colors are close (distance <= threshold), False otherwise.
        """
        return color_distance(color1, color2) <= threshold
    
    count = 0
    target_r, target_g, target_b = rgb_color
    
    for row in img:
        for pixel in row:
            pixel_r, pixel_g, pixel_b = pixel
            if is_close_color((pixel_r, pixel_g, pixel_b), (target_r, target_g, target_b)):
                count += 1
    
    return count

# Exercise 10
def loc_radius_to_corners(grid_dim, center_coord, rad):
    """
    Computes the coordinates of the corners of a square region centered at a given location
    with a specified radius within a grid.

    Parameters:
    grid_dim: Dimensions of the grid (height, width).
    center_coord: Center coordinates of the region (row, column).
    rad: Radius of the square region.

    """
    height, width = grid_dim
    row, col = center_coord
    
    tl_row = max(row - rad, 0)
    tl_col = max(col - rad, 0)
    
    tr_row = max(row - rad, 0)
    tr_col = min(col + rad, width - 1)
    
    bl_row = min(row + rad, height - 1)
    bl_col = max(col - rad, 0)
    
    br_row = min(row + rad, height - 1)
    br_col = min(col + rad, width - 1)
    
    return (tl_row, tl_col), (tr_row, tr_col), (bl_row, bl_col), (br_row, br_col)
