"""
CMSC 14100
Updated Summer 2024

Test code for Homework #2
"""
import hw2
import os
import sys

import pytest
import helpers

# Handle the fact that the test code may not
# be in the same directory as the solution code
sys.path.insert(0, os.getcwd())

# Don't complain about the position of the import
# pylint: disable=wrong-import-position

MODULE = "hw2"

@pytest.mark.parametrize("a, x, expected",
                         [(0, 0, 0),
                          (5, 2, 12),
                          (5, 0, 0),
                          (9, 1, 10),
                          (9, -2, -20),
                          (-11, 2, -20)])
def test_add_one_and_multiply(a, x, expected):
    """
    Do a single test for Exercise 1: add_one_and_multiply
    """
    recreate_msg = helpers.gen_recreate_msg(MODULE, "add_one_and_multiply",
                                            a, x)
    try:
        actual = hw2.add_one_and_multiply(a, x)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.parametrize("a, expected",
                         [(1, False),
                          (2, True),
                          (55, False),
                          (500000, True),
                          (500001, False),
                          (-3, False),
                          (-10, True),
                          (0, True)])
def test_is_even(a, expected):
    """
    Do a single test for Exercise 2: is_even
    """
    recreate_msg = helpers.gen_recreate_msg(MODULE, "is_even", a,)
    try:
        actual = hw2.is_even(a)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.parametrize("f, expected",
                         [(32, 0.0),
                          (68, 20.0),
                          (0, -17.7777777778),
                          (100, 37.7777777778), 
                          (32.00018, 0.0001), 
                          (1e6, 555537.78), 
                          (-22, -30),
                          (-459.67, -273.15)])
def test_to_celsius(f, expected):
    """
    Do a single test for Exercise 3: to_celsius
    """
    recreate_msg = helpers.gen_recreate_msg(MODULE, "to_celsius", f,)
    try:
        actual = hw2.to_celsius(f)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)
    
    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.parametrize("a, b, c, x, expected",
                         [(2, -3, 1, 2, 3),
                          (1, 2, 5, 3, 20),
                          (0, 5, 2, 4, 22),
                          (2, 0, 3, 1, 5),
                          (1, 4, 0, 3, 21),
                          (2, -3, 1, -2, 15),
                          (1000, 500, 200, 10, 105200),
                          (1, 2, 3, 1.5, 8.25),
                          (0, 0, 5, 99, 5),
                          (1, 0, -25, 5, 0)])
def test_quadratic(a, b, c, x, expected):
    """
    Do a single test for Exercise 4: quadratic
    """
    recreate_msg = helpers.gen_recreate_msg(MODULE, "quadratic", a, b, c, x,)
    try:
        actual = hw2.quadratic(a, b, c, x)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.parametrize("y, expected",
                         [(2020, True),
                          (2021, False),
                          (1900, False),
                          (2000, True),
                          (4, True),
                          (1582, False)])
def test_is_leap_year(y, expected):
    """
    Do a single test for Exercise 5: is_leap_year
    """
    recreate_msg = helpers.gen_recreate_msg(MODULE, "is_leap_year", y,)
    try:
        actual = hw2.is_leap_year(y)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)
    
    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.parametrize("a, expected",
                         [(42, True),
                          (0,  True),
                          (3.14,  False),
                          (-5.5, False),
                          (-17, False)])
def test_is_whole_number(a, expected):
    """
    Do a single test for Exercise 6: is_whole_number
    """
    recreate_msg = helpers.gen_recreate_msg(MODULE, "is_whole_number", a,)
    try:
        actual = hw2.is_whole_number(a)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)
    
    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.parametrize("y, expected",
                         [(2020, True),
                          (2021, False),
                          (1900, False),
                          (2000, True),
                          (4, True),
                          (1582, False)])
def test_leap_year_reprise(y, expected):
    """
    Do a single test for Exercise 7: leap_year_reprise
    """
    recreate_msg = helpers.gen_recreate_msg(MODULE, "leap_year_reprise", y,)
    try:
        actual = hw2.leap_year_reprise(y)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)
    
    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.parametrize("a, expected",
                         [(1, True),
                          (2, False),
                          (55, True),
                          (500000, False),
                          (500001, True),
                          (-3, True),
                          (-10, False),
                          (0, False)])
def test_is_odd(a, expected):
    """
    Do a single test for Exercise 8: is_odd
    """
    recreate_msg = helpers.gen_recreate_msg(MODULE, "is_odd", a,)
    try:
        actual = hw2.is_odd(a)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.parametrize("w, d, expected",
                         [(8, 20, 5),
                          (6, 200, 10),
                          (9, 1000, 15),
                          (12, 100, 20),
                          (15, 30, 20),
                          (11, 300, 20),
                          (20, 1000, 20),
                          (10, 50, 5),
                          (10, 500, 10),
                          (11, 50, 20)])
def test_shipping_cost(w, d, expected):
    """
    Do a single test for Exercise 9: shipping_cost
    """
    recreate_msg = helpers.gen_recreate_msg(MODULE, "shipping_cost", w, d,)
    try:
        actual = hw2.shipping_cost(w, d)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)
    
    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.parametrize("a, b, c, expected",
                         [(5, 9, 2, 5),
                          (10, 8, 4,  8),
                          (3, 7, 10, 7),
                          (-6, -2, -9, -6),
                          (4, 4, 4, 4),
                          (8, 8, 2, 8),
                          (8, 2, 8, 8),
                          (2, 8, 8, 8),
                          (3.5, 2.1, 4.8, 3.5),
                          (10000, 50000, 20000, 20000)])
def test_median_of_three(a, b, c, expected):
    """
    Do a single test for Exercise 10: median_of_three
    """
    recreate_msg = helpers.gen_recreate_msg(MODULE, "median_of_three", a, b, c,)
    try:
        actual = hw2.median_of_three(a, b, c)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)