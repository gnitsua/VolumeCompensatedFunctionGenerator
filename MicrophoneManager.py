import numpy as np
import pyaudio
import time


class MicrophoneManager():

    def __init__(self,chunk_size = 4096, rate = 44100):
        print("opening stream")
        self.chunk_size = chunk_size
        self.rate = rate
        self.p = pyaudio.PyAudio()  # start the PyAudio class
        self.stream_ob = self.p.open(format=pyaudio.paInt16, channels=1, rate=self.rate, input=True,
                                     frames_per_buffer=self.chunk_size)  # uses default input device

    def __iter__(self):
        return self

    def __next__(self):
        return np.fromstring(self.stream_ob.read(self.chunk_size), dtype=np.int16)

    def __del__(self):
        print("closing stream")
        # close the stream gracefully
        self.stream_ob.stop_stream()
        self.stream_ob.close()
        self.p.terminate()
