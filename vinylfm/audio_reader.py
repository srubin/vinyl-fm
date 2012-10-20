import pyaudio
import wave
import sys
import threading

import numpy as N

chunk = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

class RecordingTest(threading.Thread):
    def __init__(self, data):
        threading.Thread.__init__(self)


def record_frames(seconds):
    p = pyaudio.PyAudio()

    stream = p.open(format = FORMAT,
                    channels = CHANNELS,
                    rate = RATE,
                    input = True,
                    frames_per_buffer = chunk)

    print "* recording"
    all = []
    for i in range(0, RATE / chunk * seconds):
        data = stream.read(chunk)
        all.append(data)
    print "* done recording"

    stream.close()
    p.terminate()
    data = ''.join(all)
    return data
    #return N.frombuffer(data, N.uint16)


def record(seconds, filename):
    p = pyaudio.PyAudio()

    stream = p.open(format = FORMAT,
                    channels = CHANNELS,
                    rate = RATE,
                    input = True,
                    frames_per_buffer = chunk)

    print "* recording"
    all = []
    for i in range(0, RATE / chunk * seconds):
        data = stream.read(chunk)
        all.append(data)
    print "* done recording"

    stream.close()
    p.terminate()

    # write data to WAVE file
    data = ''.join(all)
    wf = wave.open(filename, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(data)
    wf.close()