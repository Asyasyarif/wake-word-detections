import os
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


sample = "background_sound/1.wav"
data, sample_rate = librosa.load(sample)

plt.title("Wave from")
librosa.display.waveshow(data, sr=sample_rate)
plt.show()

mfccs = librosa.feature.mfcc(y=data, sr=sample_rate, n_mfcc=40)
print("Shape of mfcc:", mfccs.shape)

plt.title("MFCC")
librosa.display.specshow(mfccs, sr=sample_rate, x_axis='time')
plt.show()

all_data = []

data_patah_dict = {
  0:["background_sound/" + file_path for file_path in os.listdir("background_sound/")],
  1:["audio_data/" + file_path for file_path in os.listdir("audio_data/")]
}

for class_label, list_of_files in data_patah_dict.items():
  for single_file in list_of_files:
    data, sample_rate = librosa.load(single_file)
    mfccs = librosa.feature.mfcc(y=data, sr=sample_rate, n_mfcc=40)
    mfcc_processed = np.mean(mfccs.T, axis=0)
    all_data.append([mfcc_processed, class_label])
  print(F"INFO: Successfully Preprocessed Clas Label {class_label}")

df = pd.DataFrame(all_data, columns=["feature", "class_label"])
df.to_pickle("final_audio_data_csv/audio_data.csv")