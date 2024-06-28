
"""
CMSC 14100, Summer 2024
Homework #2

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

def add_one_and_multiply(a, x):
    """
    Add 1 to a, and multiply by x.

    Inputs:
        a (int): an integer value
        x (int): another integer value

    Returns (int): The result of adding 1 to a and then multiplying by x.
    """

    return (a + 1) * x


def is_even(a):
    """
    Determine whether or not an integer is even.
    An integer is even if it is divisible by 2 with a remainder 0. 

    Inputs:
        a (int): an integer value

    Returns (boolean): True if a is even, False otherwise.
    """

    result = (a % 2 == 0)

    return result


def to_celsius(f):
    """
    Convert a temperature in Fahrenheit to Celsius.

    Inputs:
        f (number): the temperature in Fahrenheit

    Returns (float): The temperature in Celsius
    """

    result = (f - 32) * 5/9

    return result

def quadratic(a, b, c, x):
    """
    Calculates ax^2 + bx + c

    Inputs:
        a (float): quadratic coefficient
        b (float): linear coefficient
        c (float): constant value
        x (float): x value

    Returns (float): The result of the quadratic expression
    """

    result = a * x**2 +b * x + c

    return result


def is_leap_year(y):
    """
    Determine whether or not year y is a leap year. 

    Inputs:
      y (int): the year

    Returns (boolean): True if year y is a leap year, False otherwise.
    """
    if y % 4 == 0:
        if y % 100 == 0:
            if y % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
   return result 

def is_whole_number(a):
    """
    Determines whether or not a number is a whole number. 
    Whole numbers are non-negative integers. 

    Inputs:
        a (number): 

    Returns (boolean): True if a is a whole number, False otherwise. 
    """

    result = a >= 0 and int(a) == a

    return result


def is_leap_year_reprise(y):
    """
    Determine whether or not year y is a leap year, using conditionals. 

    Inputs:
      y (int): the year

    Returns (boolean): True if year y is a leap year, False otherwise.
    """

    if y % 4 == 0:
        if y % 100 == 0:
            if y % 400 == 0:
                result = True
            else:
                result = False
        else:
            result = True
    else: 
        result = False

    return result

def is_odd(a):
    """
    Determine whether or not an integer is odd.
    An integer is odd if it is not even. 

    Inputs:
        a (integer): a number 

    Returns (boolean): True if the number is odd, False otherwise.
    """

    if a % 2 == int:
        result = False
    else:
        result = True

    return result

def shipping_cost(w, d):
    """
    Calculate the shipping cost for shipping a package with weight w
    and distance d. 

    Inputs:
        w (number): weight of package in kg
        d (number): shipping distance in miles

    Returns (int): The dollar value of the shipping cost
    """

    base_cost = 5
    cost_per_kg = 2
    cost_per_mile = 0.5
    result = base_cost + w *cost_per_kg + d * cost_per_mile

    return result

def median_of_three(a, b, c):
    """
    Calculate the median of the three numbers without using logical operators.

    Inputs:
        a (number): first number
        b (number): second number
        c (number): third number

    Returns (number): The middle value of the three numbers. 
    """
 
    if (a <= b <= c) or (c <= b <= a):
        result = b
    elif (b <= a <= c) or (c <= a <=b):
        result = a
    else:
        result = c
    
    return result
