import json
from typing import List, Dict
import spotify_objs


def getFileAsDict(filename):
    #return file contents as a list of dictionaries
    with open(filename, 'r', encoding="utf8", errors="replace") as file:
        file_content = file.read()
    data = json.loads(file_content) #creates a list of dicts
    return data

def getStreamFiles():
    """
    gets any streaming history files and returns a list of strings
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

    streams = []
    for d in fileDicts:
        streams += d

    return streams