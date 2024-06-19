from typing import List

class Artist():
    """
    Get artists from StreamingHistory_music_#.json files
    These json objects give artistName, trackName, and msPlayed
    """

    def __init__(self, name: str) -> None:
        self.songs: List[Song] = []
        self.name = name
        #unlike with the Song class, for Artist these start at 0
        #since Artist is initialized when their name appears for the first time
        #and isn't dependent on anything related to their first song found
        self.streams = 0 
        self.listenTime = 0

    def __str__(self):
        return self.name

class Song():
    """
    Get song names from StreamingHistory_music_#.json files
    This object holds the name, # of streams, and total milliseconds played
    """

    def __init__(self, title: str, artist: Artist, ms: int) -> None:
        self.title = title
        self.artist = artist
        self.streams = 1 #initialized to 1 since it's initialized the first time it's found
        self.listenTime = ms

    def __str__(self):
        return self.title #FIXME: rework to give name, artist, streams

    def addStream(self, ms):
        #increment streams and add to the total listen time
        self.streams += 1
        self.listenTime += ms

    def estimate_song_length(self):
        return self.listenTime / self.streams #FIXME: rework to return in time format?


class ArtistList():
    def __init__(self) -> None:
        self.artists: List[Artist] = []
    def __str__(self):
        return self.artists
    def __contains__(self, candidate: Artist):
        return candidate in self.artists
    def append(self, new: Artist):
        self.artists.append(new)

class SongList():
    def __init__(self) -> None:
        self.songs: List[Song] = []
    def __str__(self):
        return self.songs
    def __contains__(self, candidate: Song):
        return candidate in self.songs
    def append(self, new: Song):
        self.songs.append(new)
        
