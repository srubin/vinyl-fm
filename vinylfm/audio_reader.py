import pyaudio
import wave

chunk = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

def record(seconds, filename):
    p = pyaudio.PyAudio()

    stream = p.open(format = FORMAT,
                    channels = CHANNELS,
                    rate = RATE,
                    input = True,
                    frames_per_buffer = chunk)

    chunks = []
    for i in range(0, RATE / chunk * seconds):
        data = stream.read(chunk)
        chunks.append(data)

    stream.close()
    p.terminate()

    # write data to WAVE file
    data = ''.join(chunks)
    wf = wave.open(filename, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(data)
    wf.close()