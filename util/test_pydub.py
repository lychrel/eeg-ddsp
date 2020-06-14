from scipy.io.wavfile import read
from pydub import AudioSegment
from glob import glob
from tqdm import tqdm
import numpy as np
import librosa
import sox
import warnings
warnings.filterwarnings('ignore')

#tfm = sox.Transformer()
#tfm.convert(samplerate=16000, n_channels=1)

for datadircoeff in ["a", "c"]:
    for audio_file in tqdm(glob(datadircoeff + "/*-nonorm.wav")):
        # first, fix sampling rate (DDSP wants 16k)
        #au = librosa.load("a/co2a0000424.rd.048.mp3", sr=16000)
        #librosa.output.write_wav(audio_file, au[0], au[1])
        #tfm.build(audio_file, datadircoeff + "-new/" + audio_file.split("/")[-1])
        rate, signal = read(audio_file)
        #print(signal.shape)
        channel1 = signal
        single_sec = np.copy(channel1)
        # now x10 concatenate it
        
        #channel1 = np.concatenate([channel1, np.zeros((256*9))], axis=0)

        #print(channel1.shape)
         
        for i in range(9):
            if i % 2 == 0:
                channel1 = np.concatenate([channel1, np.flip(single_sec)], axis=0)
            else:
                channel1 = np.concatenate([channel1, single_sec], axis=0)
            #print(channel1.shape)
        
        audio_segment = AudioSegment(
            channel1.tobytes(), 
            frame_rate=rate,
            sample_width=channel1.dtype.itemsize, 
            channels=1
        )

        audio_segment.export(datadircoeff + "-nonorm/" + audio_file.split("/")[-1][:-4] + ".mp3", format="mp3")
        # test that it sounds right (requires ffplay, or pyaudio):
        #from pydub.playback import play
        #play(audio_segment)
