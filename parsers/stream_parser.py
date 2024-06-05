import json
import spotify_objs

def getFileAsDict(filename):
    #return file contents as a list of dictionaries
    with open(filename, 'r', encoding="utf8", errors="replace") as file:
        file_content = file.read()
    data = json.loads(file_content) #creates a list of dicts
    return data

def main():
    files = [] #list of json files that will be parsed
    files.append("SpotifyAccountData/StreamingHistory_music_0.json")

if __name__ == "__main__":
    main()