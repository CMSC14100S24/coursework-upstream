"""
CMSC 14100
Updated Summer 2024

Test code for Homework #6
"""

import json
import os
import sys
import traceback
import pytest
import helpers
import copy

# Handle the fact that the test code may not
# be in the same directory as the solution code
sys.path.insert(0, os.getcwd())

# Don't complain about the position of the import
# pylint: disable=wrong-import-position
import tree
import hw6

MODULE = "hw6"

# Exercise 1
def check_point(p):
    """ verify that a value is a valid point """
    return (isinstance(p, tuple) and
            len(p) == 2 and
            isinstance(p[0], int) and
            isinstance(p[1], int))

def validate_path(p1, p2, path):
    """ determine whether path is a valid path from p1 to p2 """
    err_msg = f"The actual path:\n    {path}\nis not a valid path from {p1} to {p2}."

    if not isinstance(path, list):
        return f"The actual path is not a list as required."

    if len(path) == 0:
        if p1 == p2:
            return None
        else:
            return err_msg

    for p in path:
        if not check_point(p):
            return "\n\nThe actual path does not have the right type.  The expected type is: List[Tuple[int, int]]"

    # At this point, know length path is at least one.
    # Check the end points
    if path[0] != p1 or path[-1] != p2:
        return err_msg

    current = p1
    for p in path[1:]:
        a, b = current
        c, d = p
        diff1 = c - a
        diff2 = d - b
        if not ((diff1 == 1 and diff2 == 0) or
                (diff1 == 0 and diff2 == 1)):
            return err_msg
        current = (c, d)
    return None

@pytest.mark.timeout(60)
@pytest.mark.parametrize("a, b, c, d, expected",  [
    (1, 1, 1, 1, []),
    (1, 1, 2, 1, []),
    (1, 1, 1, 2, []),    
    (1, 1, 5, 2, []),
    (1, 4, 5, 9, []),
    (4, 3, 3, 3, None),
    (20, 35, 22, 3, None),
    (1000, 1000, 0, 0, None)
])
def test_find_path(a, b, c, d, expected):
    """
    Test code for find_path
    """
    recreate_msg = helpers.gen_recreate_msg(MODULE, "find_path", (a, b), (c, d))
    try:
        actual = hw6.find_path((a, b), (c, d))
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_none(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)

    if expected is not None:
        err_msg = validate_path((a, b), (c, d), actual)
        if err_msg is not None:
            pytest.fail(err_msg + recreate_msg)

# Exercise 2
@pytest.mark.timeout(60)
@pytest.mark.parametrize("item, lst, expected",  [
    (5, [1, 2, 3, 8, 13, 21], [1, 2, 3, 5, 8, 13, 21]),
    (0, [0, 1], [0, 0, 1]),
    (30, [1, 2, 3, 8, 13, 21], [1, 2, 3, 8, 13, 21, 30]),
    (7, [], [7]),
    (3, [1, 2, 3, 3, 8, 13], [1, 2, 3, 3, 3, 8, 13]),
    (5, [2, 2, 2, 2], [2, 2, 2, 2, 5]),
    (-5, [-10, -5, 0, 5, 10], [-10, -5, -5, 0, 5, 10]),
    (1, [1], [1, 1]),
    (500, list(range(1000)), list(range(501)) + [500] + list(range(501, 1000))),
    (0, [1, 2, 3], [0, 1, 2, 3]),
])
def test_insert_item(item, lst, expected):
    """
    Test code for insert item
    """
    recreate_msg = helpers.gen_recreate_msg(MODULE, "insert_item", item, lst)
    c = copy.deepcopy(lst)
    try:
        actual = hw6.insert_item(item, lst)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_list_unmodified("lst", c, lst)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)

    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)

# Exercise 3
@pytest.mark.timeout(60)
@pytest.mark.parametrize("lst, expected",  [
    ([23, 5, 1, 67, 4, 34, 9, 8, 5], [1, 4, 5, 5, 8, 9, 23, 34, 67]),
    ([], []),
    ([5, 5, 5, 5, 5], [5, 5, 5, 5, 5]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
    ([-5, -10, 0, 5, -2], [-10, -5, -2, 0, 5]),
    ([100, 50, 25, 75, 200, 150], [25, 50, 75, 100, 150, 200]),
]
)
def test_insertion_sort(lst, expected):
    """
    Test code for insertion sort
    """
    recreate_msg = helpers.gen_recreate_msg(MODULE, "insertion_sort", lst)
    c = copy.deepcopy(lst)
    try:
        actual = hw6.insertion_sort(lst)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_list_unmodified("lst", c, lst)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)

    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)

# Exercise 4
@pytest.mark.timeout(60)
@pytest.mark.parametrize("s, expected", [
    ("dogGod!!", True),
    ("doGood", False),
    ("A man, a plan, a canal, Panama!", True),
    ("Was it a car or a cat I saw?", True),
    ("No 'x' in Nixon", True),
    ("Racecar", True),
    ("apple", False),
    ("noon", True),
    ("abccba", True),
    ("", True),
]
)
def test_is_palindrome(s, expected):
    """
    Test code for is_palindrome
    """
    recreate_msg = helpers.gen_recreate_msg(MODULE, "is_palindrome", s)

    try:
        actual = hw6.is_palindrome(s)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


# Exercise 5
@pytest.mark.timeout(60)
@pytest.mark.parametrize("input_filename, expected", [
    ("sample_trees/t2.in", 0),        
    ("sample_trees/t3.in", 20),
    ("sample_trees/t1.in", 15),
    ("sample_trees/t4.in", 30),
    ("sample_trees/t5.in", 0),
    ("sample_trees/t6.in", 27)    
])
def test_sum_pos_leaves(input_filename, expected):
    """
    Test code for sum_pos_leaves
    """
    t = tree.load_tree(input_filename)
    if t is None:
        pytest.fail(f"Cannot open file: '{input_filename}'")

    steps = [
        f"import tree",
        f"t = tree.load_tree('{input_filename}')",
        f"actual = hw6.sum_pos_leaves(t)"
        ]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw6.sum_pos_leaves(t)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)
           

# Exercise 6
@pytest.mark.timeout(60)
@pytest.mark.parametrize("input_filename, target, expected", [
    ('sample_trees/t3.in', 21, 1),
    ('sample_trees/t3.in', 20, 0),
    ('sample_trees/t12.in', 50, 5),
    ('sample_trees/t12.in', 15, 3),
    ('sample_trees/t12.in', 9, 0),        
    ('sample_trees/t11.in', 8, 1),
    ('sample_trees/t7.in', 40, 4),
    ('sample_trees/t7.in', 35, 3),
    ('sample_trees/t7.in', 20, 2),
])
def test_count_less_than_paths(input_filename, target, expected):
    """
    Test code for count_less_than_paths
    """
    t = tree.load_tree(input_filename)
    if t is None:
        pytest.fail(f"Cannot open file: '{input_filename}'")

    steps = [
        f"import tree",
        f"t = tree.load_tree('{input_filename}')",
        f"actual = hw6.count_less_than_paths(t, {target})"
        ]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw6.count_less_than_paths(t, target)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)
             
        
# Exercise 7
@pytest.mark.timeout(60)
@pytest.mark.parametrize("input_filename, expected", [
    ('sample_trees/t8.in', [200]),
    ('sample_trees/t9.in', [1, 2, 3, 4]),
    ('sample_trees/t12.in', [10, 4, 8, 11]),
    ('sample_trees/t13.in', [1, 3, 6, 12]),
    ('sample_trees/t2.in', [100]),
    ('sample_trees/t14.in', [1, 2, 4, 8]),
    ('sample_trees/t6.in', [1, 3, 7, 15])
])
def test_find_max_weight_path(input_filename, expected):
    t = tree.load_tree(input_filename)
    if t is None:
        pytest.fail(f"Cannot open file: '{input_filename}'")

    steps = [
        f"import tree",
        f"t = tree.load_tree('{input_filename}')",
        f"hw6.find_max_weight_path(t)"
        ]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw6.find_max_weight_path(t)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)
