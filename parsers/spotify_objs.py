from typing import List

class Artist():
    """
    Get artists from StreamingHistory_music_#.json files
    These json objects give artistName, trackName, and msPlayed
    """

    def __init__(self, name: str) -> None:
        self.songs = SongList()
        self.name = name
        self.streams = 0 
        self.listenTime = 0

    def __str__(self):
        return self.name

class Song():
    """
    Get song names from StreamingHistory_music_#.json files
    This object holds the name, # of streams, and total milliseconds played
    """

    def __init__(self, title: str, artist: Artist) -> None:
        self.title = title
        self.artist = artist
        self.streams = 0 #initialized to 0 since the stream will be added later
        self.listenTime = 0

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
    
    def get_artist(self, candidate: str):
        #instead of returning true or false artist is returned
        #so that we know what artist to work with
        for a in self.artists:
            if a.name == candidate:
                return a 
        return None

    def append(self, new: Artist):
        self.artists.append(new)

class SongList():
    def __init__(self) -> None:
        self.songs: List[Song] = []

    def __str__(self):
        return self.songs
    
    def get_song(self, candidate: str):
        for s in self.songs:
            if s.title == candidate:
                return s
        return None
    
    def append(self, new: Song):
        self.songs.append(new)
        
