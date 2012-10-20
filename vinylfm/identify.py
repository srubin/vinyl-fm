# identify song from audio sample

import sys
import os
from collections import namedtuple

sys.path.append('lib/')

FP_SERVICE = "echonest"

if FP_SERVICE == "echonest":
    import pyechonest.song as ensong
elif FP_SERVICE == "acoustid":
    from config import ACOUSTID_API_KEY 
    import acoustid

Song = namedtuple('Song', ['artist', 'title'])

def match_song(filename):
    """return artist and title of song in filename"""
    
    if FP_SERVICE == "acoustid":
        results = acoustid.match(ACOUSTID_API_KEY, filename)
        try:
            score, recording_id, title, artist = results.next()
            return Song(artist=artist, title=title)
        except:
            return (None, None)
    elif FP_SERVICE == "echonest":
        results = ensong.identify(filename)
        try:
            song = results[0]
            return Song(artist=song.artist_name, title=song.title)
        except:
            return (None, None)
