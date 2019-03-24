import os

from flask import Flask
import rake
import re
import string

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('speech', __name__, url_prefix='/queries')

def clean(txt):
    return re.sub(r'[0-9]+', '', txt).replace(string.punctuation, "").replace("'", "").lower()

@bp.route('/generate')
def extract_topics(txt):
    r = Rake(language="English", min_length=3, max_length=9)
    r.extract_keywords_from_text(clean(txt)
    return r.get_ranked_phrases_with_scores()
