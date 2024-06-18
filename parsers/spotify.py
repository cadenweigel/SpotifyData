import json
from typing import List
import stream_parser
import misc_parsers as parser
from spotify_objs import *

"""
Main file for parsing spotify data
End goal is to have this program format the data in a more accessible way
"""

def main():
    segments = parser.parse_marquee()
    streams = stream_parser.getStreams()
    artists = parser.get_segment_artists("Super Listeners")


if __name__ == "__main__":
    main()