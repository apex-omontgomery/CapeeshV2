from google.cloud import storage
from gtts import gTTS


# pre-request speech for common values.
class BuildSpeech:
    def grab_speech(self, text):
        return gTTS(text=text, lang='en', slow=False)


class BuildText:
    def grab_text(self, sound_file):
        return


if __name__ == '__main__':
    client = storage.Client.from_service_account_json(
        r'C:\Users\wimo7\Desktop\Capeesh2\env\gsuite_speech.json')
    buckets = client.list_buckets()
    voice = BuildSpeech()
    while True:
        text = input('enter here: ')
        test = voice.grab_speech(text)
        filename = 'temp.mp3'
        test.save(filename)
