"""
CMSC 14100
Updated Summer 2024

Test code for Homework #3
"""
import random
import os
import sys
import copy

import hw3

import pytest
import helpers
import grid_helpers as gh

# Handle the fact that the test code may not
# be in the same directory as the solution code
sys.path.insert(0, os.getcwd())

# Don't complain about the position of the import
# pylint: disable=wrong-import-position

MODULE = "hw3"

@pytest.mark.parametrize("numbers, expected",
                         [([2, 3, 4],  24),
                          ([2, -3, 4], -24),
                          ([-2, -3, -4], -24),
                          ([5], 5),
                          ([0, 2, 3], 0),
                          (list(range(1, 21)), 2432902008176640000),
                          ([2, 2, 3, 3, 4, 4], 576), 
                         ])
def test_list_product(numbers, expected):
    """
    Do a test for Exercise 1
    """
    c = copy.deepcopy(numbers)
    recreate_msg = helpers.gen_recreate_msg(
        MODULE, "list_product", numbers)
    try:
        actual = hw3.list_product(numbers)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)
    
    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)
            
    err_msg = helpers.check_list_unmodified("numbers", c, numbers)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.parametrize("a, expected", [
    (0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
    (5, [0, 5, 10, 15, 20, 25, 30, 35, 40, 45]),
    (-3, [0, -3, -6, -9, -12, -15, -18, -21, -24, -27]),
    (100, [0, 100, 200, 300, 400, 500, 600, 700, 800, 900]),
    (1, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
    (-1, [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]),
    (-100, [0, -100, -200, -300, -400, -500, -600, -700, -800, -900]),
   ])
def test_first_ten_multiples(a, expected):
    """
    Do a test for Exercise 2
    """
    recreate_msg = helpers.gen_recreate_msg(
        MODULE, "first_ten_multiples", a, expected)
    
    try:
        actual = hw3.first_ten_multiples(a)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)
    
    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)

        
@pytest.mark.parametrize("numbers, slice_start, slice_end, expected", [
    ([1, 2, 3, 4, 5], 1, 3, 24),
    ([1, 2, 3, 4, 5], 0, 3, 24),
    ([1, 2, 3, 4, 5], 2, 4, 60),
    ([1, 2, 3, 4, 5], 2, 2, 3),
    ([1, 2, 3, 4, 5], 3, 1, None),
    ([1, 2, 3, 4, 5], -1, 3, None),
    ([1, 2, 3, 4, 5], 2, 6, None),
    ([], 0, 2, None),
    ([1, 2, 3, 4, 5], 0, 4, 120), 
    ([2, 3, 4, 2, 3, 4], 1, 4, 72)
   ])
def test_slice_product(numbers, slice_start, slice_end, expected):
    """
    Do a test for Exercise 3
    """
    recreate_msg = helpers.gen_recreate_msg(
        MODULE, "slice_product", numbers, slice_start, slice_end)
    
    c = copy.deepcopy(numbers)
    try:
        actual = hw3.slice_product(numbers, slice_start, slice_end)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)
    
    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)
    
    err_msg = helpers.check_list_unmodified("numbers", c, numbers)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.parametrize("some_strings, expected", [
                        (["Hello", "World"], ["Hello!", "World!"]),
                        (["Python"], ["Python!"]), 
                        ([], None), 
                        ([""], ["!"]), 
                        ([" ", " ", " "], [" !", " !", " !"]), 
                        (["Awesome!", "Cool!", "Nice!"], ["Awesome!!", "Cool!!", "Nice!!"]), 
                        (["Hello,", "World!", "How?"], ["Hello,!", "World!!", "How?!"]),
                        (["a"] * 10000, ["a!"] * 10000), 
                        ])
def test_exclaim(some_strings, expected):
    """
    Do a test for Exercise 4
    """
    recreate_msg = helpers.gen_recreate_msg(
        MODULE, "exclaim", some_strings)
    
    c = copy.deepcopy(some_strings)
    try:
        actual = hw3.exclaim(some_strings)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)
    
    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)
    
    err_msg = helpers.check_list_unmodified("some_strings", c, some_strings)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.parametrize("original_point, other_points, expected", [
    ((0, 0), [(1, 0), (2, 2), (1, 1)], (2, 2)),
    ((-1, -1), [(-2, -2), (-1, -1), (-1, -2)], (-2, -2)),
    ((0, 0), [(1, 1)], (1, 1)),
    ((-0, 0), [], None),
    ((0, 0), [(1, 1), (-1, -1), (2, 2), (-2, -2)], (2, 2)),
    ((0, 0), [(1000, 1000), (-1000, -1001), (500, 500)], (-1000, -1001)), 
    ((0, 0), [(0.5, 0.5), (0.3, 0.3), (0.7, 0.7)], (0.7, 0.7)),
    ((0, 0), [(i, i) for i in range(10000)], (9999, 9999)),
    ])
def test_farthest(original_point, other_points, expected):
    """
    Do a test for Exercise 5
    """
    recreate_msg = helpers.gen_recreate_msg(
        MODULE, "farthest", original_point, other_points)
    
    c_points = copy.deepcopy(other_points)
    try:
        actual = hw3.farthest(original_point, other_points)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)
    
    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)
    
    err_msg = helpers.check_list_unmodified("other_points", c_points, other_points)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.parametrize("some_floats, threshold, expected", [
    # Basic Cases
    ([2.0, 3.0, 5.0], 10, (10.0, True, "right on")),
    ([3.0, 4.0, 5.0], 10, (12.0, True, "we made it")),
    ([4.0, 5.0], 10, (9.0, False, "very close")),
    
    # Edge Cases
    ([], 10, None),
    ([15.0], 20, (15.0, False, "close")),
    
    # Special Cases
    ([1.0] * 1000, 500, (1000.0, True, "we made it")),
    ([-5.0, -3.0, -1.0], -10, (-9.0, True, "we made it")),
    ([-5.0, -3.0, -1.0], -8, (-9.0, False, "very close")),
    
    # Other Cases
    ([0.1, 0.2, 0.1], 0.3, (0.4, True, "we made it")),
    ([10.0, 20.0, 30.0], 1000, (60.0, False, "not even close"))
    ])
def test_did_we_make_it(some_floats, threshold, expected):
    """
    Do a test for Exercise 6
    """
    recreate_msg = helpers.gen_recreate_msg(
        MODULE, "did_we_make_it", some_floats, threshold)
    
    c_floats = copy.deepcopy(some_floats)
    try:
        actual = hw3.did_we_make_it(some_floats, threshold)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)
    
    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)
    
    err_msg = helpers.check_list_unmodified("some_floats", c_floats, some_floats)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)
    

dupe_tests = [
    # Basic Cases
    ([1, 2, 3, 3, 4], True),
    ([1, 1, 2, 3, 4], True),
    ([1, 2, 2, 3, 4], True),
    ([1, 2, 3, 4, 4], True),
    ([1, 2, 3, 4, 5], False),
    
    # Edge Cases
    ([], False),
    ([1], False),
    ([1, 1], True),
    ([1, 1, 1], True),
    
    # Special Cases
    ([1, 2, 2, 3, 3, 3, 4], True),
    ([1, 2, 3, 3, 3, 4, 4], True),
    
    # Large list
    ([1] * 1000 + [2] * 1000, True),  # 1000 ones followed by 1000 twos
    ([1, 2] * 1000, False),  # Alternating 1 and 2, no consecutive duplicates      
    ]

@pytest.mark.parametrize("some_numbers, expected", dupe_tests)
def test_contains_duplicate_v1(some_numbers, expected):
    """
    Do a test for Exercise 7
    """
    recreate_msg = helpers.gen_recreate_msg(
        MODULE, "contains_duplicate_v1", some_numbers)
    
    c_nums = copy.deepcopy(some_numbers)
    try:
        actual = hw3.contains_duplicate_v1(some_numbers)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)
    
    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg) 
    
    err_msg = helpers.check_list_unmodified("some_numbers", c_nums, some_numbers)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.parametrize("some_numbers, expected", dupe_tests)
def test_contains_duplicate_v2(some_numbers, expected):
    """
    Do a test for Exercise 8
    """
    recreate_msg = helpers.gen_recreate_msg(
        MODULE, "contains_duplicate_v2", some_numbers)
    
    c_nums = copy.deepcopy(some_numbers)
    try:
        actual = hw3.contains_duplicate_v2(some_numbers)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)
    
    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg) 
    
    err_msg = helpers.check_list_unmodified("some_numbers", c_nums, some_numbers)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)   


RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
by_stripe = gh.load_image("tests/blue_yellow_stripe.ppm")
blue_ish_img = gh.load_image("tests/blue_ish_img.ppm")
greens_img = gh.load_image("tests/gs_example.ppm")
nqy_img = gh.load_image("tests/one_not_quite_yellow.ppm")
cbg_img = gh.load_image("tests/checkerboard_green.ppm")

@pytest.mark.parametrize("img, rgb_color, expected", [
    # Basic Cases
    (  # Case 1: Single pixel match
        [
            [(255, 0, 0), (0, 255, 0)],
            [(0, 0, 255), (255, 255, 0)]
        ],
        (255, 0, 0),
        1
    ),
    (  # Case 2: Multiple pixels match
        [
            [(255, 0, 0), (0, 255, 0)],
            [(0, 0, 255), (0, 255, 0)]
        ],
        (0, 255, 0),
        2
    ),
    (  # Case 3: No pixels match
        [
            [(255, 0, 0), (0, 255, 0)],
            [(0, 0, 255), (255, 255, 0)]
        ],
        (0, 0, 0),
        0
    ),
    
    # Edge Cases
    (  # Case 4: Empty image
        [],
        (255, 0, 0),
        0
    ),
    (  # Case 5: Image with single pixel
        [[(255, 255, 255)]],
        (255, 255, 255),
        1
    ),
    
    # Special Cases
    (  # Case 6: Close colors with varying distances
        [
            [(255, 0, 0), (0, 255, 0), (0, 0, 255)],
            [(255, 255, 255), (100, 100, 100), (200, 200, 200)]
        ],
        (200, 200, 200),
        2
    ),
    (  # Case 7: Close colors with very large image
        [
            [(255, 0, 0)] * 1000,
            [(0, 255, 0)] * 1000,
            [(0, 0, 255)] * 1000
        ] * 1000,
        (0, 0, 0),
        0
    ),
    (greens_img, RED, 0),
    (greens_img, GREEN, 86),
    (greens_img, BLUE, 0),
    (nqy_img, YELLOW, 0),
    (cbg_img, YELLOW, 0),
    (cbg_img, GREEN, 18),
    (cbg_img, BLACK, 6),
    (cbg_img, WHITE, 6),
])
def test_count_close_colors(img, rgb_color, expected):
    """
    Do a test for Exercise 9
    """
    recreate_msg = helpers.gen_recreate_msg(
        MODULE, "count_close_colors", img, rgb_color)
    
    c_img = copy.deepcopy(img)
    try:
        actual = hw3.count_close_colors(img, rgb_color)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)
    
    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg) 
    
    err_msg = helpers.check_list_unmodified("img", c_img, img)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.parametrize("grid_dim, center_coord, rad, expected", [
    # Basic Cases
    ((10, 10), (5, 5), 3, ((2, 2), (2, 8), (8, 2), (8, 8))),
    ((3, 3), (1, 1), 2, ((0, 0), (0, 2), (2, 0), (2, 2))),
    
    # Edge Cases
    ((5, 5), (0, 0), 2, ((0, 0), (0, 2), (2, 0), (2, 2))),
    ((10, 10), (5, 5), 0, ((5, 5), (5, 5), (5, 5), (5, 5))),
    
    # Special Cases
    ((6, 6), (3, 3), 3, ((0, 0), (0, 5), (5, 0), (5, 5))),
    ((1000, 1000), (500, 500), 500, ((0, 0), (0, 999), (999, 0), (999, 999))),
    
    # Additional Cases from the question
    ((6, 5), (3, 2), 0, ((3, 2), (3, 2), (3, 2), (3, 2))),
    ((6, 5), (3, 2), 1, ((2, 1), (2, 3), (4, 1), (4, 3))),
    ((6, 5), (3, 2), 2, ((1, 0), (1, 4), (5, 0), (5, 4))),
    ((6, 5), (3, 2), 3, ((0, 0), (0, 4), (5, 0), (5, 4))),
    ((6, 5), (0, 0), 0, ((0, 0), (0, 0), (0, 0), (0, 0))),
    ((6, 5), (0, 0), 1, ((0, 0), (0, 1), (1, 0), (1, 1))),
    ((6, 5), (0, 0), 2, ((0, 0), (0, 2), (2, 0), (2, 2))),     
])
def test_loc_radius_to_corners(grid_dim, center_coord, rad, expected):
    """
    Do a test for Exercise 10
    """
    recreate_msg = helpers.gen_recreate_msg(
        MODULE, "loc_radius_to_corners", grid_dim, center_coord, rad)
    
    try:
        actual = hw3.loc_radius_to_corners(grid_dim, center_coord, rad)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)
    
    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg) 
