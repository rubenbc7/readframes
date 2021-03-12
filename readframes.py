import wave
import numpy as np
import matplotlib.pyplot as plt

good_morning = wave.open('good-morningMan.wav', 'r')
afternoon = wave.open('good-afternoon.wav', 'r')


framesGM = good_morning.readframes(-1)
framesAN = afternoon.readframes(-1)
ondaconvertidaGM = np.frombuffer(framesGM, dtype='int16')
ondaconvertidaAN = np.frombuffer(framesAN, dtype='int16')

#print(frames[:10])

framerate_gm = good_morning.getframerate()
print (framerate_gm)
time_gm = np.linspace(start=0, stop=len(ondaconvertidaGM)/framerate_gm, num=len(ondaconvertidaGM))
print(time_gm[:10])

framerate_AN = afternoon.getframerate()
print (framerate_AN)
time_AN = np.linspace(start=0, stop=len(ondaconvertidaAN)/framerate_AN, num=len(ondaconvertidaAN))
print(time_AN[:10])

plt.title('Good morning vs Good afternoon')

plt.xlabel('Tiempo (segundos')
plt.ylabel('Amplitud')

plt.plot(time_gm, good_morning, label='Good morning')
plt.plot(time_AN, afternoon, label='Good afternoon', alpha=0.5)