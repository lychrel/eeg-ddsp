import scipy.io.wavfile
from glob import glob
from tqdm import tqdm
import numpy as np
import sys

subject_path = sys.argv[1]
data_dir = "/home/jack/Repos/bme512/data/"
target_channel = "33"

only_two_groups = True

# for every subject in the data directory,
for subject_path in tqdm(glob(data_dir + "*/")):
    #print(subject_path)
    time_series = []
    #print("num trials in {}: {}".format(subject_path, len(list(glob(subject_path + "*")))))
    #print(list(glob(subject_path + "*")))
    # for every trial in a subject's folder,
    for trial in glob(subject_path + "*"):
        channel_33 = False
        with open(trial, "r") as fp:
            file_lines = iter(fp.readlines())
            # we want channel 33
            #while not channel_33:
            for next_line in file_lines:
                #next_line = next(file_lines)
                if "chan " + target_channel in next_line:
                    channel_33 = True
                    break
                    #print(next_line)
            samples = []
            #while(len(samples) < 256):
            for trial_line in file_lines:
                #trial_line = next(file_lines)
                #print(trial_line)
                samples.append(eval(trial_line.split(" ")[-1]))
                time_series.append(eval(trial_line.split(" ")[-1]))
                if len(samples) == 256:
                    break

            # write this trial to .wav
            samples = np.array(samples)
            if samples.shape[0] == 0:
                continue
            if samples.max() == samples.min():
                continue

            samples = ((samples - samples.min()) * (1/(samples.max() - samples.min())) * 255).astype('uint8') 
            if only_two_groups:
                group = subject_path[:-1].split("/")[-1][3]
                #print(group)
                path_out = data_dir + group + "/" + trial.split("/")[-1] + ".wav"
                scipy.io.wavfile.write(path_out, 256, samples)
                # write out mega mp3 (per subject)
            else:
                scipy.io.wavfile.write(trial + ".wav", 256, samples)

    
    if len(time_series) == 0:
        continue
    time_series = np.array(time_series)
    time_series = ((time_series - time_series.min()) * (1/(time_series.max() - time_series.min())) * 255).astype('uint8') 
    
    #print(time_series.shape)
    scipy.io.wavfile.write(path_out[:-4] + "-nonorm.wav", 256, time_series)

    #print("num trials for {}: {}".format(subject_path, len(time_series) / 256))
    #time_series = np.array(time_series)
    #print(time_series.shape)
    # normalize data to [0, 255]
    #time_series -= np.mean(time_series)
    #time_series /= np.amax(time_series)
    #time_series = ((time_series - time_series.min()) * (1/(time_series.max() - time_series.min())) * 255).astype('uint8') 
    #print(time_series)
    #print(time_series)
    
    #scipy.io.wavfile.write(subject_path[:-1] + ".wav", 256, time_series)

#print(samples)
