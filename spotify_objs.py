from typing import List

class ArtistList():
    def __init__(self) -> None:
        self.artists: List[Artist] = []

class SongList():
    def __init__(self) -> None:
        self.songs: List[Song] = []

class Artist():
    """
    Get artists from StreamingHistory_music_#.json files
    These json objects give artistName, trackName, and msPlayed
    """

    def __init__(self, name: str) -> None:
        self.songs: List[Song] = []
        self.name = name

class Song():
    """
    Get song names from StreamingHistory_music_#.json files
    This object holds the name, # of streams, and total milliseconds played
    """

    def __init__(self, name: str, artist: str, ms: int) -> None:
        self.name = name
        self.artist = artist
        self.streams = 1 #initialized to 1 since it's initialized the first time it's found
        self.listenTime = ms

    def addStream(self, ms):
        self.streams += 1
        self.listenTime += ms
