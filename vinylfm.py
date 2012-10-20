import sys
import time
import getpass

import pylast

from vinylfm import identify
from vinylfm import audio_reader
from config import LASTFM_API_KEY, LASTFM_SECRET_KEY

def main():
    """run the main loop of the vinyl-fm scrobbler"""
    username = raw_input('Last.fm username: ')
    password_hash = pylast.md5(getpass.getpass())
    last_song = ('', '')
    
    network = pylast.LastFMNetwork(api_key = LASTFM_API_KEY, api_secret = 
        LASTFM_SECRET_KEY, username = username, password_hash = password_hash)
    
    
    print "Listening... (control-C to exit)"
    
    while True:
        audio_reader.record(60, 'tmpVFM.wav')
        current_song = identify.match_song('tmpVFM.wav')
        if current_song == (None, None):
            print "..."
            continue
        if current_song != last_song:
            network.scrobble(current_song.artist, 
                             current_song.title,
                             int(time.time()))
            print "%s - %s" % (current_song.artist, current_song.title)
            last_song = current_song


if __name__ == '__main__':
    main()