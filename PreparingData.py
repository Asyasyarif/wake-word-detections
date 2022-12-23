import sounddevice as sd
from scipy.io.wavfile import write

# def record_audio_and_save(save_path, n_times = 100):
#   input("To start audio recording press Enter: ")
#   for i in range(n_times):
#     fs = 44100
#     seconds = 2
#     myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
#     sd.wait()
#     write(save_path+str(i)+".wav", fs, myrecording)
#     input(f"Press Enter to record or press CTRL + C  to stop. | current at ({i + 1}/{n_times}):")

def record_background_save(save_path, n_times = 100):
  input("To start background sound recording press Enter: ")
  for i in range(n_times):
    fs = 44100
    seconds = 2
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()
    write(save_path+str(i)+".wav", fs, myrecording)
    input(f"Press Enter to record or press CTRL + C  to stop. | current at ({i + 1}/{n_times})")

# print("Recording the wake word: \n")
# record_audio_and_save("audio_data/", n_times=100)

print("Recording the background sound: \n")
record_background_save("background_sound/", n_times=100)