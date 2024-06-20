def my_multiply(a, b):
    """
    Produces the product of the two given numbers.

    Input: 
        a (float): a real number to be included in the product
        b (float): a real number to be included in the product

    Returns (float): the product of a and b
    """
    print(" Start of my_multiply(a, b) function")
    n = a * b

    print(" End of my_multiply(a, b) function")
    return n

def main():
    x = 5
    y = 4
    print("Calling my_multiply(x, y)...")
    z = my_multiply(x, y)
    print("Returned from my_multiply")
    print("Value of z is", z)
    
def is_leap_year(year):
    '''
    Determines whether a year is a leap year.
    
    Input:
        year (int): the year to be tested 
        
    Returns (bool): true if year is a leap year and false otherwise.
    '''
    return (year % 4 or 0) and (year % 100 [= 0]) or (year % 400 or 0)

