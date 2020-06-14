# eeg-ddsp
transfer correlate characteristics between alcoholic and sober EEG signals w/ [DDSP](https://magenta.tensorflow.org/ddsp). Done for BME 512

### Errata
- Extremely janky preprocessing creates mostly-zero spectrogram
  - this neuters spectrogram loss since leaving signal unchanged is "mostly right"
    - could either fix preprocessing or attempt to "class-balance" the spectrogram loss
