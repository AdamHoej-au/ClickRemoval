import glob as glob
import soundfile as sf
import numpy as np

## get files
files = glob.glob("*.wav")

fade_in = 100e-3  # 100 ms fade in
fade_in_time = int(44100 * fade_in)

for file in files:
    data, samplerate = sf.read(file, dtype="int16")

    # cosine fade in
    data[0:fade_in_time] = data[0:fade_in_time] * (
        (-np.cos(np.arange(fade_in_time) / fade_in_time * np.pi) + 1) / 2
    )
    sf.write(file, data, samplerate, subtype="PCM_16")
