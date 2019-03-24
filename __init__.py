import os

import io
from flask import Flask
from google.cloud import speech_v1
from google.cloud.speech_v1 import enums
from google.cloud.speech_v1 import types
import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        # a default secret that should be overridden by instance config
        SECRET_KEY='dev',
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.update(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # make url_for('index') == url_for('blog.index')
    # in another app, you might define a separate main index here with
    # app.route, while giving the blog blueprint a url_prefix, but for
    # the tutorial the blog will be the main index
    #app.add_url_rule('/', endpoint='index')

    return app

app = create_app()

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/api/upload', methods=['POST'])
def upload():
    return render_template('post.html')
     uri = request.files['audio'].stream.read()
     # #uri = open(stream, "rb", buffering=0)
     #
     # print("Debug")
     # print(request)
     # print(request.form)
     # print(request.files)
     # print("Debug")
     # # text = convert_speech_to_text(audio)
     #
     client = speech_v1.SpeechClient()
     #
     encoding = enums.RecognitionConfig.AudioEncoding.FLAC
     sample_rate_hertz = 48000
     language_code = 'en-US'
     #config = {'encoding': encoding, 'sample_rate_hertz': sample_rate_hertz, 'language_code': language_code}
     config = types.RecognitionConfig(encoding=encoding,
         sample_rate_hertz=sample_rate_hertz,
         language_code=language_code)
     #uri = 'gs://bucket_name/file_name.flac'
     # print(str(uri))
     audio = types.RecognitionAudio(content=uri)
     # print("AUDIO: " + str(audio))
     # print("CONFIG: " + str(config))
     response = client.recognize(config, audio)
     # print("AAAAAA"+str(response))
     # print("BBBBBBB"+str(response.results))
     # print("CCCCCCC"+str(response.results[0].alternatives))
     # print(response.results[0].alternatives[0].transcript)
     #
     # return response.results[0].alternatives[0].transcript
     sample_txt = ""
     x = io.open('sample.txt', mode='r', encoding='utf-8', errors='ignore')
     for line in x:
         sample_txt += line
     print(sample_txt)
     return sample_txt

 def clean(txt):
     return re.sub(r'[0-9]+', '', txt).replace(string.punctuation, "").replace("'", "").lower()

 @app.route('/generate')
 def extract_topics(txt):
     r = Rake(language="English", min_length=3, max_length=9)
     r.extract_keywords_from_text(clean(txt)
     y = r.get_ranked_phrases_with_scores()
     print(y)
     return y
