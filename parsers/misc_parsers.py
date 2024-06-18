import json
from typing import List, Dict
import spotify_objs

"""
Python file to hold various parsers
For files that aren't really that interesting
But we want them parsed anyways just in case
"""

#Marquee Parsers

def parse_marquee():
    """
    Returns a dictionary where the keys are segments
    and the values are the number of artists in that segment
    """

    f = 'SpotifyAccountData/Marquee.json'
    with open(f, 'r', encoding="utf8", errors="replace") as file:
        file_content = file.read()
 
    data = json.loads(file_content) #creates a list of dicts

    segments = {} #track the possible segment options
    for i in data:
        seg = i['segment']
        if seg not in segments:
            segments[seg] = 1
        else:
            segments[seg] += 1

    return segments

def get_segment_artists(segment: str) -> List[str]:
    """
    gets artists in a given segment
    Options: Previously Active Listeners, Light Listeners, Moderate Listeners, Super Listeners
    """
    f = 'SpotifyAccountData/Marquee.json'
    with open(f, 'r', encoding="utf8", errors="replace") as file:
        file_content = file.read()
 
    data = json.loads(file_content) #creates a list of dicts
    artists = []

    for i in data:
        if (i['segment'] == segment):
            artists.append(i['artistName'])

    return artists
