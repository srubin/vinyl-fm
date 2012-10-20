# identify song from audio sample

import sys
import os
from collections import namedtuple

sys.path.append('lib/')

FP_SERVICE = "echonest"

if FP_SERVICE == "echonest":
    import pyechonest.song as ensong
    from config import ECHO_NEST_API_KEY
    import pyechonest.config as enconfig
    enconfig.ECHO_NEST_API_KEY = ECHO_NEST_API_KEY
elif FP_SERVICE == "acoustid":
    from config import ACOUSTID_API_KEY 
    import acoustid

Song = namedtuple('Song', ['artist', 'title'])

def match_song(filename):
    """return artist and title of song in filename"""
    
    if FP_SERVICE == "acoustid":
        try:
            results = acoustid.match(ACOUSTID_API_KEY, filename)
        except:
            return (None, None)
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
