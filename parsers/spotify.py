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

    #Initialize lists
    Artists = ArtistList()
    Songs = SongList()

    #get streams information
    streams = stream_parser.getStreams()
    bounds = stream_parser.getStreamBounds(streams) #gives the dates that all streams occur within
    

if __name__ == "__main__":
    main()