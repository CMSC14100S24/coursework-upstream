import pytest
import helpers
from hw5 import Board, Player

MODULE = "hw5"

@pytest.fixture
def setup_players():
    p1 = Player("Player1", "X")
    p2 = Player("Player2", "O")
    return p1, p2

@pytest.mark.timeout(60)
@pytest.mark.parametrize("target, height, width, expected",
                          [(2, 1, 1, (2, 1, 1, [[' ']])),
                           (3, 3, 3, (3, 3, 3, [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']])), 
                           (5, 1, 10, (5, 1, 10, [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]))
                           ])
def test_board_initialization(target, height, width, expected):
    """
    Test for exercise 1: board init (set attributes)
    """
    steps = [f"board = hw5.Board({target}, {height}, {width})"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)
    
    try:
        board = Board(target, height, width)
        actual = ((expected[0] == board.target) and 
                  (expected[1]  == board.height) and
                  (expected[2]  == board.width) and 
                  (expected[3] == board.cells))
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, True)
    if err_msg is not None:
        err_msg = "\n\nBoard attribute not set correctly."
        err_msg += f"\n  Expected: target = {expected[0] }"
        err_msg += f"\n            height = {expected[1] }"
        err_msg += f"\n            width = {expected[2] }"
        err_msg += f"\n            cells = {expected[3] }"
        err_msg += f"\n  Actual: target = {board.target}"
        err_msg += f"\n          height = {board.height}"
        err_msg += f"\n          width = {board.width}"
        err_msg += f"\n          cells = {board.cells}"

        pytest.fail(err_msg + recreate_msg)

def test_board_default_init():
    """
    Another test for exercise one
    """

    steps = [f"board = hw5.Board()"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)
    expected_cells = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ']]
    try:
        board = Board()
        actual = ((4 == board.target) and 
                  (6 == board.height) and
                  (7  == board.width) and 
                  (expected_cells == board.cells))
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, True)
    if err_msg is not None:
        err_msg = "\n\nBoard attribute not set correctly."
        err_msg += f"\n  Expected: target = {4}"
        err_msg += f"\n            height = {6}"
        err_msg += f"\n            width = {7 }"
        err_msg += f"\n            cells = {expected_cells}"
        err_msg += f"\n  Actual: target = {board.target}"
        err_msg += f"\n          height = {board.height}"
        err_msg += f"\n          width = {board.width}"
        err_msg += f"\n          cells = {board.cells}"

        pytest.fail(err_msg + recreate_msg)

@pytest.mark.timeout(60)
@pytest.mark.parametrize("board, expected",
                         [("Board(1, 1, 1)", '-----\n|   |\n-----'),
                          ("Board()", '-----------------------------\n|   |   |   |   |   |   |   |\n|   |   |   |   |   |   |   |\n|   |   |   |   |   |   |   |\n|   |   |   |   |   |   |   |\n|   |   |   |   |   |   |   |\n|   |   |   |   |   |   |   |\n-----------------------------'),
                          ("Board(3, 6, 7)", '-----------------------------\n|   |   |   |   |   |   |   |\n|   |   |   |   |   |   |   |\n|   |   |   |   |   |   |   |\n|   |   |   |   |   |   |   |\n|   |   |   |   |   |   |   |\n|   |   |   |   |   |   |   |\n-----------------------------'),
                          ("Board(3, 3, 3)", '-------------\n|   |   |   |\n|   |   |   |\n|   |   |   |\n-------------'),
                          ("Board(10, 10, 10)", '-----------------------------------------\n|   |   |   |   |   |   |   |   |   |   |\n|   |   |   |   |   |   |   |   |   |   |\n|   |   |   |   |   |   |   |   |   |   |\n|   |   |   |   |   |   |   |   |   |   |\n|   |   |   |   |   |   |   |   |   |   |\n|   |   |   |   |   |   |   |   |   |   |\n|   |   |   |   |   |   |   |   |   |   |\n|   |   |   |   |   |   |   |   |   |   |\n|   |   |   |   |   |   |   |   |   |   |\n|   |   |   |   |   |   |   |   |   |   |\n-----------------------------------------'),
                          ])
def test_board_string_no_markers(board, expected):
    """
    Test for board str
    """
    steps = [f"myboard = hw5.{board}",
             f"s = str(myboard)",
             f"print(s)"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)
    actual_board = eval(board)

    try:
        actual = str(actual_board)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)

def test_board_string_with_markers():
    """
    Another test for exercise two
    """
    steps = [f"myboard = hw5.Board(1, 1, 1)",
             f"myboard.drop_marker(0, 'T')"
             f"s = str(myboard)",
             f"print(s)"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual_board = Board(1, 1, 1)
        actual_board.drop_marker(0, "T")
        actual = str(actual_board)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    expected = "-----\n| T |\n-----"
    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)

moves = [(0, "X"), (1, "Y"), (1, "X"), (1, "Y")]
rets = [True, True, True, False]
state = [[[' ', ' '], ['X', ' ']], [[' ', ' '], ['X', 'Y']], [[' ', 'X'], ['X', 'Y']], [[' ', 'X'], ['X', 'Y']]]

@pytest.mark.timeout(60)
@pytest.mark.parametrize("moves, expected_ret",
                         [
                             (moves[:1], rets[0]),
                             (moves[:2], rets[1]),
                             (moves[:3], rets[2]),
                             (moves, rets[3]),
                          ])
def test_board_drop_markers_ret(moves, expected_ret):
    """
    Test for board drop_marker
    """
    steps = [f"myboard = hw5.Board(4, 2, 2)"]
    for move in moves: 
        steps.append(f"myboard.drop_marker({move[0]}, '{move[1]}')")
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    actual_board = Board(4, 2, 2)
    try:
        last_actual_ret = None
        for move in moves: 
            last_actual_ret = actual_board.drop_marker(move[0], move[1])
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(last_actual_ret, expected_ret)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)

@pytest.mark.timeout(60)
@pytest.mark.parametrize("moves, expected_cells",
                         [
                             (moves[:1], state[0]),
                             (moves[:2], state[1]),
                             (moves[:3], state[2]),
                             (moves, state[3]),
                          ])
def test_board_drop_markers_cells(moves, expected_cells):
    """
    Test for board drop_marker
    """
    steps = [f"myboard = hw5.Board(4, 2, 2)"]
    for move in moves: 
        steps.append(f"myboard.drop_marker({move[0]}, '{move[1]}')")
    steps.append(f"myboard.cells")
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    actual_board = Board(4, 2, 2)
    try:
        for move in moves: 
            actual_board.drop_marker(move[0], move[1])
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual_board.cells, expected_cells)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


victory_test_cases = [
    # 1. Horizontal Win on 3x3 Board
    ([(0, "X"), (1, "X"), (2, "X")], (3, 3, 3), True, None),

    # 2. Vertical Win on 4x4 Board
    ([(1, "O"), (1, "O"), (1, "O")], (4, 4, 3), True, None),

    # 3. Diagonal Win on 5x5 Board
    ([(0, "X"), (1, "O"), (1, "X"), (2, "O"), (2, "O"), (2, "X"), (3, "O"), (3, "O"), (3, "O"), (3, "X")], (5, 5, 4), True, None),

    # 4. Diagonal Win on 6x7 Board
    ([(5, "X"), (4, "O"), (4, "X"), (3, "O"), (3, "O"), (3, "X"), (2, "O"), (2, "O"), (2, "O"), (2, "X")], (6, 7, 4), True, None),

    # 5. No Win on 6x7 Board
    ([(0, "X"), (1, "O"), (0, "X"), (1, "O"), (2, "X")], (6, 7, 4), False, [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                                                            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                                                            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                                                            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                                                            ['X', 'O', ' ', ' ', ' ', ' ', ' '],
                                                                            ['X', 'O', 'X', ' ', ' ', ' ', ' ']]),

    # 6. Mixed Results on 4x5 Board
    ([(0, "X"), (1, "O"), (1, "X"), (2, "O"), (2, "X"), (2, "X")], (4, 5, 3), True, None),

    # 7. Vertical Win on 4x4 Board (k = 2)
    ([(1, "O"), (1, "O")], (4, 4, 2), True, None),

    # 8. Early Win on 3x5 Board
    ([(0, "X"), (1, "X")], (3, 5, 2), True, None),

    # 9. Horizontal Placing Winning Piece in Middle(5x5 Board)
    ([(0, "X"), (1, "X"), (3, "X"), (2, "X")], (5, 5, 4), True, None),

    # 10. No win with 4 in a row
    ([(0, "X"), (1, "X"), (2, "X"), (3, "X")], (1, 10, 5), False, [['X', 'X', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' ']]),

    # 11. Diagonal Placing Winning Piece in Middle (4x6 Board)
    ([(2, "X"), (0, "O"), (1, "O"), (0, "O"), (0, "X"), 
      (1, "X")], (4, 6, 3), True, None),

    # 12. Diagonal Placing Winning Piece in Middle (3x3 Board)
    ([(0, "O"), (1, "X"), (2, "O"), (2, "X"), (2, "O"), 
      (1, "O")], (3, 3, 3), True, None),

    # 13. Any Move Wins on 3x3 Board (k = 1)
    ([(0, "X")], (3, 3, 1), True, None),

    # 14. Can't win (k = 1)
    ([(0, "X")], (1, 1, 2), False, [[" "]]),

]
@pytest.mark.timeout(60)
@pytest.mark.parametrize("moves, board, expected_result, _",
                         victory_test_cases)
def test_board_end_winner(moves, board, expected_result, _):
    """
    Test for board check_end for winners
    """
    steps = [f"myboard = hw5.Board({board[2]}, {board[0]}, {board[1]})"]
    for move in moves: 
        steps.append(f"myboard.drop_marker({move[0]}, '{move[1]}')")
    steps.append(f"myboard.check_end()")
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    actual_board = Board(board[2], board[0], board[1])
    try:
        for move in moves: 
            actual_board.drop_marker(move[0], move[1])
        actual_ret = actual_board.check_end()
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual_ret, expected_result)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


moves2 = [(0, "X"), (1, "Y"), (1, "X"), (1, "Y"), (0, "Y")]
# state2 = [[[' ', ' '], ['X', ' ']], [[' ', ' '], ['X', 'Y']], 
#           [[' ', 'X'], ['X', 'Y']], [[' ', 'X'], ['X', 'Y']], 
#           [['Y', 'X'], ['X', 'Y']]]
@pytest.mark.timeout(60)
@pytest.mark.parametrize("moves, expected_result",
                         [(moves2[:1], False), 
                         (moves2[:2], False), 
                         (moves2[:3], False), 
                         (moves2[:4], False), 
                         (moves2[:5], False)] 
                         )
def test_board_end_full_no_win(moves, expected_result):
    """
    Test for board check_end for catgame
    """
    steps = [f"myboard = hw5.Board(3, 2, 2)"]
    for move in moves: 
        steps.append(f"myboard.drop_marker({move[0]}, '{move[1]}')")
    steps.append(f"myboard.check_end()")
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    actual_board = Board(3, 2, 2)
    try:
        for move in moves: 
            actual_board.drop_marker(move[0], move[1])
        actual_ret = actual_board.check_end()
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual_ret, expected_result)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)

moves3 = [(2, "X"), (0, "O"), (2, "X"), (2, "O"), (1, "X"), 
          (0, "O"), (1, "X"), (1, "O"), (0, "X")]
# state3 = [
#         [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', 'X']], 
#         [[' ', ' ', ' '], [' ', ' ', ' '], ['O', ' ', 'X']], 
#         [[' ', ' ', ' '], [' ', ' ', 'X'], ['O', ' ', 'X']], 
#         [[' ', ' ', 'O'], [' ', ' ', 'X'], ['O', ' ', 'X']], 
#         [[' ', ' ', 'O'], [' ', ' ', 'X'], ['O', 'X', 'X']], 
#         [[' ', ' ', 'O'], ['O', ' ', 'X'], ['O', 'X', 'X']], 
#         [[' ', ' ', 'O'], ['O', 'X', 'X'], ['O', 'X', 'X']], 
#         [[' ', 'O', 'O'], ['O', 'X', 'X'], ['O', 'X', 'X']], 
#         [['X', 'O', 'O'], ['O', 'X', 'X'], ['O', 'X', 'X']], 
#           ]
@pytest.mark.timeout(60)
@pytest.mark.parametrize("moves, expected_result",
                         [(moves3[:1], False), 
                         (moves3[:2], False), 
                         (moves3[:5], False), 
                         (moves3[:8], False), 
                         (moves3[:9], True)] 
                         )
def test_board_end_full_with_win(moves, expected_result):
    """
    Test for board check_end last spot wins
    """
    steps = [f"myboard = hw5.Board(3, 3, 3)"]
    for move in moves: 
        steps.append(f"myboard.drop_marker({move[0]}, '{move[1]}')")
    steps.append(f"myboard.check_end()")
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    actual_board = Board(3, 3, 3)
    try:
        for move in moves: 
            actual_board.drop_marker(move[0], move[1])
        actual_ret = actual_board.check_end()
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual_ret, expected_result)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.timeout(60)
@pytest.mark.parametrize("moves, board, expected_result, nonemptystate",
                         victory_test_cases)
def test_board_end_clear_on_win(moves, board, expected_result, nonemptystate):
    """
    Test for board cells after winner
    """
    steps = [f"myboard = hw5.Board({board[2]}, {board[0]}, {board[1]})"]
    for move in moves: 
        steps.append(f"myboard.drop_marker({move[0]}, '{move[1]}')")
    steps.append(f"myboard.check_end()")
    steps.append(f"myboard.cells")
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    actual_board = Board(board[2], board[0], board[1])
    try:
        for move in moves: 
            actual_board.drop_marker(move[0], move[1])
        _ = actual_board.check_end()
        actual_state = actual_board.cells
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)
    if expected_result: 
        expected_cells = [[" "]*board[1] for _ in range(board[0])]
    else: 
        expected_cells = nonemptystate

    err_msg = helpers.check_result(actual_state, expected_cells)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


full_board_test_cases = [
    # 1. Target 1 in 1x1 Board
    ([(0, "X")], (1, 1, 1), True, [[' ']]),

    # 2. Target 2 in 2x2 Board (All filled)
    ([(0, "X"), (0, "O"), (1, "T"), (1, "O")], (2, 2, 2), True, [[' ', ' '],
                                                                   [' ', ' ']]),

    # 3. Target 2 in 2x3 Board (Not full)
    ([(0, "X"), (1, "X"), (0, "O")], (2, 3, 3), False, [['O', ' ', ' '],
                                                         ['X', 'X', ' ']]),

    # 4. Target 3 in 3x3 Board (Not full)
    ([(0, "X"), (1, "O"), (1, "X"), (2, "X"), (1, "O")], (3, 3, 3), False, [[' ', 'O', ' '],
                                                                   [' ', 'X', ' '],
                                                                   ['X', 'O', 'X']]),

    # 5. Target 4 in 6x6 Board (Fully filled)
    ([(i, "X" if (i + j) % 2 == 0 else "O") for i in range(6) for j in range(6)], (4, 6, 20), True,
     [[' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ']]),

    # 6. Target 3 in 5x5 Board (Not full)
    ([(0, "X"), (1, "X"), (2, "X"), (3, "O"), (4, "O")], (3, 5, 5), False, 
                                                    [[' ', ' ', ' ', ' ', ' '],
                                                    [' ', ' ', ' ', ' ', ' '],
                                                    ['X', 'X', 'X', 'O', 'O'],
                                                    ]),

    # 7. Target 2 in 4x4 Board (Fully filled)
    ([(i, "X" if (i + j) % 2 == 0 else "O") for i in range(4) for j in range(4)], (2, 4, 5), True,
     [[' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ']]),

    # 8. Target 5 in 5x5 Board (One column empty)
    ([(i, "X") for i in range(5) for j in range(5) if i != 4], (5, 5, 6), False, [['X', 'X', 'X', 'X', ' '],
                                                                                   ['X', 'X', 'X', 'X', ' '],
                                                                                   ['X', 'X', 'X', 'X', ' '],
                                                                                   ['X', 'X', 'X', 'X', ' '],
                                                                                   ['X', 'X', 'X', 'X', ' ']]),

    # 9. Target 6 in 6x7 Board (All positions filled)
    ([(i, "X" if (i + j) % 2 == 0 else "O") for i in range(6) for j in range(7)], (6, 6, 7), True,
     [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', ' ']]),
]


@pytest.mark.timeout(60)
@pytest.mark.parametrize("moves, board, expected_result, nonemptystate",
                         full_board_test_cases)
def test_board_end_clear_on_full(moves, board, expected_result, nonemptystate):
    """
    Test for board cells after filled up, winner or not. 
    """
    steps = [f"myboard = hw5.Board({board[2]}, {board[0]}, {board[1]})"]
    for move in moves: 
        steps.append(f"myboard.drop_marker({move[0]}, '{move[1]}')")
    steps.append(f"myboard.check_end()")
    steps.append(f"myboard.cells")
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    actual_board = Board(board[2], board[0], board[1])
    try:
        for move in moves: 
            actual_board.drop_marker(move[0], move[1])
        _ = actual_board.check_end()
        actual_state = actual_board.cells
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)
    
    if expected_result: 
        expected_cells = [[" "]*board[1] for _ in range(board[0])]
    else: 
        expected_cells = nonemptystate

    err_msg = helpers.check_result(actual_state, expected_cells)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)

