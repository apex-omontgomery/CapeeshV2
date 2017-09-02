from gtts import gTTS
from streaming import single_request

# pre-request speech for common values.
class BuildSpeech:
    def grab_speech(self, text):
        return gTTS(text=text, lang='en', slow=False)


def main(_words):
    voice = BuildSpeech()
    for word in words:
        question = voice.grab_speech('How do you spell {}'.format(word))
        filename = 'temp.mp3'
        question.save(filename)



if __name__ == "__main__":
    words = ['dog', 'cat', 'dad', 'cassie', 'happy']
    main(words)