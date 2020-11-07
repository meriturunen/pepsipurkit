# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 16:06:37 2020

@author: Teemu
"""
import flask
import pandas as pd
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>S.C.H.O.O.L. API</h1><p>Routes.</p>/api/v1/sentiments<p>"

# A route to return all of the available entries in our catalog.
@app.route('/api/v1/sentiments', methods=['GET'])
def api_all():
    dat=pd.read_csv('../sentiments.csv')
    return jsonify(dat.to_dict('records'))

app.run()