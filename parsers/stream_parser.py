import json
from typing import List, Dict
from spotify_objs import *


def getFileAsDict(filename):
    #return file contents as a list of dictionaries
    with open(filename, 'r', encoding="utf8", errors="replace") as file:
        file_content = file.read()
    data = json.loads(file_content) #creates a list of dicts
    return data

def getStreamFiles():
    """
    gets any streaming history files and returns a list of strings
    want to automate it eventually (not type in file names manually)
    should be able to check string until it gets to a number
    SpotifyAccountData/StreamingHistory_music_ would indicate a valid file
    """
    files = []
    files.append("SpotifyAccountData/StreamingHistory_music_0.json")
    files.append("SpotifyAccountData/StreamingHistory_music_1.json")
    files.append("SpotifyAccountData/StreamingHistory_music_2.json")
    files.append("SpotifyAccountData/StreamingHistory_music_3.json")
    files.append("SpotifyAccountData/StreamingHistory_music_4.json")
    files.append("SpotifyAccountData/StreamingHistory_music_5.json")
    files.append("SpotifyAccountData/StreamingHistory_music_6.json")
    return files

def getStreams():

    files = [] #list of json files that will be parsed
    fileDicts: List[Dict] = [] #list of dictionaries that are returned from getFileAsDict

    files = getStreamFiles()
    for f in files:
        fileDicts.append(getFileAsDict(f))

    streams: List[Dict] = []
    for d in fileDicts:
        streams += d #add every dict in d to streams

    return streams

def getStreamBounds(streams: List[Dict]):
    """
    returns a tuple of the first and last endTimes in streams
    """
    start = streams[0]['endTime']
    end = streams[len(streams)-1]['endTime']
    return (start, end)


def parseStreams(streams: Dict, songs: SongList, artists: ArtistList):
    """
    Loops through streams and populates the songs and artists lists

    When a stream is parsed, it will check for that song and artist existing already
    By first checking that the artist exists, and then checking the artist's songs
    Each stream gives us artistName, trackName, and msPlayed

    Returns nothing but updates songs and artists
    """

    for stream in streams:
    
        stream_artist = artists.get_artist(stream['artistName'])

        if stream_artist == None:
            #artist hasn't been added yet
            stream_artist = Artist(stream['artistName'])
            artists.append(stream_artist)
        
        stream_song = stream_artist.songs.get_song(stream['trackName'])

        if stream_song == None:
            #song hasn't been added yet
            stream_song = Song(stream['trackName'], stream_artist)
            stream_artist.songs.append(stream_song) #add to artist's SongList
            songs.append(stream_song) #add to the global SongList

        stream_artist.streams += 1
        stream_artist.listenTime += stream['msPlayed']
        stream_song.streams += 1
        stream_song.listenTime += stream['msPlayed']
        

