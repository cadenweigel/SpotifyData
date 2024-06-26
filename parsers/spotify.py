import json
import sys
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
    sys.setrecursionlimit(2000)

    #get streams loaded into Artists and Songs
    stream_parser.parseStreams(streams, Songs, Artists)
    stream_parser.sortSongs(Songs, 0, len(Songs.songs)-1)
    stream_parser.sortArtists(Artists, 0, len(Artists.artists)-1)
    
    

if __name__ == "__main__":
    main()