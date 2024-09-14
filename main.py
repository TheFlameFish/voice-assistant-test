## TODO: Implement stt

import texttospeech as tts
import random

class UserFinished(Exception): pass

tts.play("Initialized")

def random_number():
    return "Here's a random number. " + str(random.randint(0,100))

def goodbye():
    raise UserFinished
    

responses = {
    "Hi user! How can I help you?": ["hi","hello","greetings","salutations"],
    goodbye: ["bye","goodbye","see you"],
    random_number: ["random", "number"]
}

def get_response(text):
    text = text.lower()
    words = text.split() 
    
    for key, values in responses.items():
        for value in values:
            if value in words:
                if callable(key):
                    return key()
                return key
    return "Sorry, I don't understand."


if __name__ == "__main__":
    while True:
        try:
            tts.play(get_response(input("> ")))
        except UserFinished:
            tts.play("Goodbye!")
            break