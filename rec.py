import sounddevice as sd
import wave
import numpy as np

duration = 5 
sample_rate = 44100 
channels = 1 

print("start recording")
audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=channels, dtype=np.int16)
sd.wait() 
print("recoreded")

file_name = "recorded_audio.wav"
with wave.open(file_name, 'wb') as wf:
    wf.setnchannels(channels)
    wf.setsampwidth(2)  
    wf.setframerate(sample_rate)
    wf.writeframes(audio_data.tobytes())

print(f"saved as '{file_name}'")
