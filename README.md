# vinyl-fm

*automatically* scrobble vinyl to last.fm

## Usage

`python vinylfm.py`

You will be asked to enter your username and password. The password is immediately hashed and authorized by last.fm (it's not being saved in plaintext anywhere- don't worry!).

At the moment, you must be using a record player that has USB output connected to your computer, or a split output that you can plug in to your computer's microphone port. Make sure that you switch your sound input settings to use the record player (however it's attached).

A future update will save the password hash for automated login. Ideally, `vinyl-fm` would use over-the-air recognition (a la Sound Hound and Shazam) but I can't yet find a music fingerprinting library that can robustly identify music this way. If you find anything that would work in the over-the-air setting, please let me know!

Also coming soon: more intelligent recording segments. At the moment, vinyl-fm arbitrarily records 90 seconds segments. Instead, it should note long periods of silence and start recording after those pauses.

## Requirements
portaudio, pyaudio, Cython, pyechonest, pylast

So, first:

http://portaudio.com/download.html (I built this from source; I think there was a problem with the homebrew version)

and then:

`pip install pyaudio Cython pyechonest pylast`

## Obligatory work-in-progress note

This is a work in progress. Chill. It'll get better.