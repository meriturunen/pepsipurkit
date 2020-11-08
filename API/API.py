# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 16:06:37 2020

@author: Teemu
"""
import flask
import pandas as pd
from flask import request, jsonify
from flask_cors import CORS, cross_origin

app = flask.Flask(__name__)
app.config["DEBUG"] = True
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@cross_origin()
@app.route('/', methods=['GET'])
def home():
    return "<h1>S.C.H.O.O.L. API</h1><p>Routes.</p>/api/v1/sentiments<p><p>/api/v1/summat</p><p>/api/v1/raaka</p>"

# A route to return all of the available entries in our catalog.
@cross_origin()
@app.route('/api/v1/sentiments', methods=['GET'])
def api_sentiments():
    dat=pd.read_csv('../sentiments.csv')
    return jsonify(dat.to_dict('records'))

@cross_origin()
@app.route('/api/v1/summat', methods=['GET'])
def api_summat():
    dat=pd.read_csv('../summat.csv')
    return jsonify(dat.to_dict('records'))

@cross_origin()
@app.route('/api/v1/summat/hist', methods=['GET'])
def api_summat_hist():
    dat=pd.read_csv('../summat.csv')
    cutted,bins=pd.cut(dat['summaamount'],5,labels=False,retbins=True)
    dat['bin']=cutted
    dat2=dat.groupby('bin')["summaamount"].agg(['sum','count'])
    dat3=dat.groupby('bin')["tulotamount"].sum()
    dat2['tulot']=dat3
    dat2=dat2.sort_values(by='sum')
    return jsonify(dat2.to_dict('records'))

@cross_origin()
@app.route('/api/v1/raaka', methods=['GET'])
def api_raaka():
    dat=pd.read_csv('../alkuparsinta.csv')
    return jsonify(dat.to_dict('records'))
	
@cross_origin()
@app.route('/api/v1/isodonitsi', methods=['GET'])
def api_donitsi1():
    dat=pd.read_csv('../master.csv')
    df=dat[['osa_alue_nimi','menotamount']]
    df2=df.groupby('osa_alue_nimi', as_index=False).sum()
    df21 = df2[(df2 != 0).all(1)]
    df3=df21.rename(columns={'osa_alue_nimi': 'name', 'menotamount': 'value'})
    return jsonify(df3.to_dict('records'))

@cross_origin()
@app.route('/api/v1/kpldonitsi', methods=['GET'])
def api_donitsi2():
    dat=pd.read_csv('../master.csv')
    df=dat[['osa_alue_id']]
    df2=df.groupby(['osa_alue_id']).size().reset_index(name='count')
    df3=df2.rename(columns={'osa_alue_id': 'name', 'count': 'value'})
    df3['name'] = 'Projektityyppi ' + df3['name'].astype(str)
    return jsonify(df3.to_dict('records'))

@cross_origin()
@app.route('/api/v1/tuotosdonitsi', methods=['GET'])
def api_donitsi3():
    dat=pd.read_csv('../master.csv')
    df=dat[['ei-tuotos-tyyppia','henkiloestoeliikkuvuudet-lkm','julkaisut','kasikirja',
            'koulutus','muu-tuotos','ohjelma','opiskelijaliikkuvuudet-lkm',
            'raportti','selvitys','tapahtuma','toimintamalli','tutkimus','verkkosivut']]
    df2=df.sum(axis=0).T
    df3=df2.reset_index(level=0, inplace=False)
    df4=df3.rename(columns={'index': 'name', 0: 'value'})
    return jsonify(df4.to_dict('records'))

@cross_origin()
@app.route('/api/v1/alldata', methods=['GET'])
def all_data():
    data=pd.read_csv('../master.csv')
    data['mean']=data['mean'].fillna(0)
    data=data.fillna("")
    return jsonify(data.to_dict('records'))


app.run()