import os
from flask import Flask, request, render_template

music_dir = r'C:\Users\wimo7\Desktop\Capeesh2\env\CapeeshV2\static\music'
# video_dir = '/home/flask/flaskmedia/static/video'
# image_dir = '/home/flask/flaskmedia/static/image'

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
    music_files = [f for f in os.listdir(music_dir) if f.endswith('mp3')]
    music_files_number = len(music_files)
    return render_template("index2.html",

                        music_files_number = music_files_number,
                        music_files = music_files)


@app.route('/<filename>')
def song(filename):
    return render_template('play.html',

                        music_file = filename)


if __name__ == '__main__':
    app.run(host = '127.0.0.1', debug = True)