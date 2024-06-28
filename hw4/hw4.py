"""
CMSC 14100
Summer 2024
Homework #4

YOUR NAME HERE

People Consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URLs of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.
"""

def song_to_string(song):
    """
    Create a string description of a song in the form:
         [Song] by [Artist] was released in [ReleasedYear]

    Input:
        song [Dict]: a song listing

    Returns [str]: A description of the song in the format above.
    """
    ### YOUR CODE HERE
    pass # delete pass in all functions as you go


def create_streams_dict(songs):
    """
    Given a list of songs, create a dictionary that maps each  
        song name to the number of streams it has on spotify.

    Inputs:
        songs [List[Dict]]: list of songs

    Returns [Dict]: Dictionary that maps songs to stream count.  
    """
    ### YOUR CODE HERE
    pass


def find_fast_songs(songs, min_tempo):
    """
    Given a list of songs, create a list of songs names for 
        that have a bpm at least as high as the given bpm. 

    Inputs:
        songs [List[Dict]]: list of songs
        min_tempo [int]: the minimum tempo of a song in bpm

    Returns [List[str]]: A list of song names that are at least
        as fast as the min_tempo
    """
    ### YOUR CODE HERE
    pass



def count_keys(songs):
    """
    Given a list of songs, create a dictionary that maps a
        key to the number of songs of that key. 

    Inputs:
        sightings [List[Dict]]: list of songs

    Returns [Dict]: Dictionary that maps keys to the number of 
        songs in that key.
    """
    ### YOUR CODE HERE
    pass


def most_common_key(songs):
    """
    Given a list of songs, determine the most commonly occurring 
        key and the number of times it occurred. 
    
    Inputs:
        songs [List[Dict]]: list of songs

    Returns [Tuple[str, int]]: The most commonly occuring key and
        the number of times it occurred. 
    """
    ### YOUR CODE HERE
    pass


def songs_by_year(songs):
    """
    Given a list of songs, create a dictionary that maps a year 
        to a list of the song dictionaries from that year.
    
    Inputs:
        songs [List[Dict]]: list of songs

    Returns [Dict]: A dictionary that maps years to a list of 
        song dictionaries.
    """
    ### YOUR CODE HERE
    pass
    
def common_artists(songs, mode):
    """
    Given a list of songs, find the songs that share 
        an artist only considering songs of the given mode. 

    Inputs:
        songs [List[Dict]]: list of songs
        mode [string]: the mode of the songs to consider

    Returns [List[Tuple[str, str]]]: A list of song name tuples where
        the songs share at least one artist. 
    """
    ### YOUR CODE HERE
    pass