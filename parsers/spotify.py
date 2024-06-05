import json
from typing import List
import stream_parser
import spotify_objs

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

def main():
    segments = parse_marquee()
    print(segments)

if __name__ == "__main__":
    main()