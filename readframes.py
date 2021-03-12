import wave
import numpy as np

GM = wave.open('good-morningMan.wav', 'r')


frames = GM.readframes(-1)
ondaconvertida = np.frombuffer(frames, dtype='int16')

print(frames[:10])