# -*- coding: utf-8 -*-
from app import app
from flask import request
import test

@app.route('/nltk', methods = ['GET', 'POST'])
def nltk():
    return nltk_ner.processSpecific(request.form['text'])
     

