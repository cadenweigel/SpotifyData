import json
import os
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
    files = os.listdir("SpotifyAccountData")
    stream_files = []
    for f in files:
        if f.startswith("StreamingHistory_music_"):
            #since the directory isn't included when doing os.listdir
            #it needs to be added back in the string here
            stream_files.append("SpotifyAccountData/" + f)

    return stream_files

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

    A stream will be added if its msPlayed is greater than 25000ms (25 seconds)
    It's okay to add a new song or artist on a 0ms stream since their listening data 
    is only updated if the stream is valid

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

        if stream['msPlayed'] > 25000:
            #stream is only valid if it isn't 25000ms / 25s (subject to change)

            stream_artist.streams += 1
            stream_artist.listenTime += stream['msPlayed']
            stream_artist.lastStream = stream['endTime']

            stream_song.streams += 1
            stream_song.listenTime += stream['msPlayed']
            stream_song.lastStream = stream['endTime']

            if stream_artist.streams == 0:
                #firstStream is updated here to account for 0ms streams
                stream_artist.firstStream = stream['endTime']
                stream_song.firstStream = stream['endTime']
        

def sortSongs(songs: SongList, low: int, high: int):

    if low < high:

        # Find pivot element such that
        # elements smaller than pivot are on the left
        # elements greater than pivot are on the right
        pi = partitionSongs(songs, low, high) #pivot index

        sortSongs(songs, low, pi - 1) #Recursive call on the left of pivot
        sortSongs(songs, pi + 1, high) #Recursive call on the right of pivot


def partitionSongs(songs: SongList, low: int, high: int):
    
    pivot = songs.songs[high].streams #choose the rightmost element as pivot
    i = low - 1 #pointer for greater element

    for j in range(low, high):
        if songs.songs[j].streams >= pivot:
            i = i + 1 #swap it with the greater element pointed by i
            (songs.songs[i], songs.songs[j]) = (songs.songs[j], songs.songs[i])

    #Swap the pivot element with the greater element specified by i
    (songs.songs[i+1], songs.songs[high]) = (songs.songs[high], songs.songs[i+1])

    return i + 1 #Return the position from where partition is done

def sortArtists(artists: ArtistList, low: int, high: int):

    if low < high:

        # Find pivot element such that
        # elements smaller than pivot are on the left
        # elements greater than pivot are on the right
        pi = partitionArtists(artists, low, high) #pivot index

        sortArtists(artists, low, pi - 1) #Recursive call on the left of pivot
        sortArtists(artists, pi + 1, high) #Recursive call on the right of pivot


def partitionArtists(artists: ArtistList, low: int, high: int):
    
    pivot = artists.artists[high].streams #choose the rightmost element as pivot
    i = low - 1 #pointer for greater element

    for j in range(low, high):
        if artists.artists[j].streams >= pivot:
            i = i + 1 #swap it with the greater element pointed by i
            (artists.artists[i], artists.artists[j]) = (artists.artists[j], artists.artists[i])

    #Swap the pivot element with the greater element specified by i
    (artists.artists[i+1], artists.artists[high]) = (artists.artists[high], artists.artists[i+1])

    return i + 1 #Return the position from where partition is done 