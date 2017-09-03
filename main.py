from gtts import gTTS
from streaming import single_request
import pdb
import pyglet
from pyglet.gl import *

pyglet.options['audio'] = ('openal', 'directsound', 'silent')

# build the speech for user if file isn't
class BuildSpeech:
    def check_if_available(self):


    def grab_speech(self, text):
        return gTTS(text=text, lang='en', slow=False)


def main(_words):
    voice = BuildSpeech()
    for word in words:
        question = voice.grab_speech('How do you spell {}'.format(word))
        filename = r'C:\Users\wimo7\Desktop\Capeesh2\env\CapeeshV2\static\music\{}.mp3'.format(word)
        question.save(filename)
'''
1. Start up webapp
2. Get list of words
3. Interact with user
4. Verify if user response correct
5. Give user response

'''



if __name__ == "__main__":
    words = ['dog', 'cat', 'dad', 'cassie', 'happy']
    main(words)