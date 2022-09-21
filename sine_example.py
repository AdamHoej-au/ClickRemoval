import soundfile as sf
import math

T = 1 
fs = 44100
t = [i/fs for i in range(int(fs*T))]
x = [math.sin(2*math.pi*440*t) for t in t]
T_x = 10e-3
t_x = [i/fs for i in range(int(fs*T_x))]
x_1 = [math.sin(2*math.pi*11e3*t_x) for t_x in t_x]

## append x to x_1
x_1.extend(x)
sf.write("sine.wav", x_1, fs,subtype="PCM_16")
