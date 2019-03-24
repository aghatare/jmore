import io
from flask import Flask
from google.cloud import speech_v1
from google.cloud.speech_v1 import enums
import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('speech', __name__, url_prefix='/speech')

@bp.route('/index')
def index():
    return "index.html"

@bp.route('/totext')
def convert_speech_to_text(uri):
    client = speech_v1.SpeechClient()

    encoding = enums.RecognitionConfig.AudioEncoding.FLAC
    sample_rate_hertz = 44100
    language_code = 'en-US'
    config = {'encoding': encoding, 'sample_rate_hertz': sample_rate_hertz, 'language_code': language_code}
    #uri = 'gs://bucket_name/file_name.flac'
    audio = {'uri': uri}

    response = client.recognize(config, audio)
    return response
