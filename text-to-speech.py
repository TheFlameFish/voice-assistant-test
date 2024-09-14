import torch
from TTS.api import TTS
import sounddevice as sd

# Get device
device = "cuda" if torch.cuda.is_available() else "cpu"

# List available 🐸TTS models
print("---------------------------------")
print(TTS().list_models().list_models())
print("--------------------------------")

# Init TTS with the target model name
tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC_ph", progress_bar=True).to(device)

def play(text):
    # Run TTS
    output = tts.tts(text)

    sd.play(output, 22050)  # 22050 is the sample rate used by the TTS model
    sd.wait()  # Wait for the sound to finish playing

if __name__ == "__main__":
    play("Hello, user! My name is jarvus, which stands for \"Just a very unintelligent system.\" How can I help you?")
    play("Never gonna give you up, never gonna let you down! Never gonna blah blah blah blah and blah blah!")
    play("Hello world!")