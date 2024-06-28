"""
CMSC 14100
Updated Summer 2024

Test code for HW #4
"""
import hw4
import json
import copy
import os
import sys
import pytest
import helpers

# Handle the fact that the test code may not
# be in the same directory as the solution code
sys.path.insert(0, os.getcwd())

# Don't complain about the position of the import
# pylint: disable=wrong-import-position

MODULE = "hw4"

# Exercise 1
song_to_string = json.load(open("tests/song_to_string.json", "r", encoding="utf-8"))
@pytest.mark.timeout(60)
@pytest.mark.parametrize("song, expected", song_to_string)
def test_song_to_string(song, expected):
    """
    Test for exercise 1
    """
    steps = [f"song = {song}",
             f"{MODULE}.song_to_string(song)"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw4.song_to_string(song)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)



# Exercise 2
create_streams_dict = json.load(open("tests/create_streams_dict.json", "r", encoding="utf-8"))
@pytest.mark.timeout(60)
@pytest.mark.parametrize("filename, songs, expected", create_streams_dict)
def test_create_streams_dict(filename, songs, expected):
    """
    Test for exercise 2
    """
    steps = [f"import data_helpers",
             f"songs = data_helpers.load_csv_data('data/{filename}.csv')",
             f"{MODULE}.create_streams_dict(songs)"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)
    
    c = copy.deepcopy(songs)
    try:
        actual = hw4.create_streams_dict(songs)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)


    err_msg = helpers.check_list_unmodified("songs", c, songs)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)

    err_msg = helpers.check_dict(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


# Exercise 3
find_fast_songs = json.load(open("tests/find_fast_songs.json", "r", encoding="utf-8"))
@pytest.mark.timeout(60)
@pytest.mark.parametrize("filename, songs, min_tempo, expected", find_fast_songs)
def test_find_fast_songs(filename, songs, min_tempo, expected):
    """
    Test for exercise 3
    """
    steps = [f"import data_helpers",
             f"songs = data_helpers.load_csv_data('data/{filename}.csv')",
             f"{MODULE}.find_fast_songs(songs, {min_tempo})"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)
    
    c = copy.deepcopy(songs)
    try:
        actual = hw4.find_fast_songs(songs, min_tempo)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    # actual.sort()
    err_msg = helpers.check_list_unmodified("songs", c, songs)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)

    err_msg = helpers.check_1d_iterable(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


# Exercise 4
count_keys = json.load(open("tests/count_keys.json", "r", encoding="utf-8"))
@pytest.mark.timeout(60)
@pytest.mark.parametrize("filename, songs, expected", count_keys)
def test_count_keys(filename, songs, expected):
    """
    Test for exercise 4
    """
    steps = [f"import data_helpers",
             f"songs = data_helpers.load_csv_data('data/{filename}.csv')",
             f"{MODULE}.count_keys(songs)"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)
    c = copy.deepcopy(songs)

    try:
        actual = hw4.count_keys(songs)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_list_unmodified("songs", c, songs)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)
    
    err_msg = helpers.check_dict(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)



# Exercise 5
most_common_key = json.load(open("tests/most_common_key.json", "r", encoding="utf-8"))
@pytest.mark.timeout(60)
@pytest.mark.parametrize("filename, songs, expected", most_common_key)
def test_most_common_key(filename, songs, expected):
    """
    Test for exercise 5
    """
    steps = [f"import data_helpers",
             f"songs = data_helpers.load_csv_data('data/{filename}.csv')",
             f"{MODULE}.most_common_key(songs)"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)
    expected = tuple(expected)

    c = copy.deepcopy(songs)
    try:
        actual = hw4.most_common_key(songs)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_list_unmodified("songs", c, songs)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)

    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


# Exercise 6
songs_by_year = json.load(open("tests/songs_by_year.json", "r", encoding="utf-8"))
songs_fixed = []
for test in songs_by_year: 
    test_res = test[2] 
    fixed_type_dict = dict([(int(k), v) for k, v in test_res.items()])
    # json stores the year keys with quotes and reads in as string
    # this fixes them to ints
    songs_fixed.append([test[0], test[1], fixed_type_dict])
songs_by_year = songs_fixed
@pytest.mark.timeout(60)
@pytest.mark.parametrize("filename, songs, expected", songs_by_year)
def test_songs_by_year(filename, songs, expected):
    """
    Test for exercise 6
    """

    steps = [f"import data_helpers",
             f"songs = data_helpers.load_csv_data('data/{filename}.csv')",
             f"{MODULE}.songs_by_year(songs)"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)
    
    c = copy.deepcopy(songs)
    try:
        actual = hw4.songs_by_year(songs)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_list_unmodified("songs", c, songs)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)

    err_msg = helpers.check_dict(actual, expected)
    if err_msg is not None:
        print(actual)
        pytest.fail(err_msg + recreate_msg)

# Exercise 7
common_artists = json.load(open("tests/common_artists.json", "r", encoding="utf-8"))
@pytest.mark.timeout(60)
@pytest.mark.parametrize("filename, songs, mode, expected", common_artists)
def test_common_artists(filename, songs, mode, expected):
    """
    Test for exercise 7
    """
    steps = [f"import data_helpers",
             f"songs = data_helpers.load_csv_data('data/{filename}.csv')",
             f"{MODULE}.common_artists(songs, {mode})"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)
    c = copy.deepcopy(songs)
    for i, pair in enumerate(expected):
        expected[i] = tuple(pair)

    try:
        actual = hw4.common_artists(songs, mode)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    actual = [tuple(sorted(t)) for t in actual]
    actual.sort()
    err_msg = helpers.check_list_unmodified("songs", c, songs)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)

    expected = [tuple(sorted(t)) for t in expected]
    expected.sort()
    err_msg = helpers.check_1d_iterable(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)

