# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 16:06:37 2020

@author: Teemu
"""
import flask
import pandas as pd
from flask import request, jsonify
from flask_cors import CORS, cross_origin

application = flask.Flask(__name__)
application.config["DEBUG"] = True
cors = CORS(application)
#application.config['CORS_HEADERS'] = 'Content-Type'

@cross_origin()
@application.route('/', methods=['GET'])
def home():
    return "<h1>S.C.H.O.O.L. API</h1><p>Routes.</p>/api/v1/sentiments<p><p>/api/v1/summat</p><p>/api/v1/raaka</p>"

# A route to return all of the available entries in our catalog.
@cross_origin()
@application.route('/api/v1/sentiments', methods=['GET'])
def api_sentiments():
    dat=pd.read_csv('sentiments.csv')
    return jsonify(dat.to_dict('records'))

@cross_origin()
@application.route('/api/v1/summat', methods=['GET'])
def api_summat():
    dat=pd.read_csv('summat.csv')
    return jsonify(dat.to_dict('records'))

@cross_origin()
@application.route('/api/v1/summat/hist', methods=['GET'])
def api_summat_hist():
    dat=pd.read_csv('summat.csv')
    cutted,bins=pd.cut(dat['summaamount'],5,labels=False,retbins=True)
    dat['bin']=cutted
    dat2=dat.groupby('bin')["summaamount"].agg(['sum','count'])
    dat3=dat.groupby('bin')["tulotamount"].sum()
    dat2['tulot']=dat3
    dat2=dat2.sort_values(by='sum')
    return jsonify(dat2.to_dict('records'))

@cross_origin()
@application.route('/api/v1/raaka', methods=['GET'])
def api_raaka():
    dat=pd.read_csv('alkuparsinta.csv')
    return jsonify(dat.to_dict('records'))
	
@cross_origin()
@application.route('/api/v1/isodonitsi', methods=['GET'])
def api_donitsi1():
    dat=pd.read_csv('master.csv')
    df=dat[['osa_alue_nimi','menotamount']]
    df2=df.groupby('osa_alue_nimi', as_index=False).sum()
    df21 = df2[(df2 != 0).all(1)]
    df3=df21.rename(columns={'osa_alue_nimi': 'name', 'menotamount': 'value'})
    return jsonify(df3.to_dict('records'))

@cross_origin()
@application.route('/api/v1/kpldonitsi', methods=['GET'])
def api_donitsi2():
    dat=pd.read_csv('master.csv')
    df=dat[['osa_alue_id']]
    df2=df.groupby(['osa_alue_id']).size().reset_index(name='count')
    df3=df2.rename(columns={'osa_alue_id': 'name', 'count': 'value'})
    df3['name'] = 'Projektityyppi ' + df3['name'].astype(str)
    return jsonify(df3.to_dict('records'))

@cross_origin()
@application.route('/api/v1/tuotosdonitsi', methods=['GET'])
def api_donitsi3():
    dat=pd.read_csv('master.csv')
    df=dat[['ei-tuotos-tyyppia','julkaisut',
            'koulutus','muu-tuotos',
            'raportti','tapahtuma','toimintamalli','tutkimus','verkkosivut']]
    df2=df.sum(axis=0).T
    df3=df2.reset_index(level=0, inplace=False)
    df4=df3.rename(columns={'index': 'name', 0: 'value'})
    return jsonify(df4.to_dict('records'))

@cross_origin()
@application.route('/api/v1/rahadonitsi', methods=['GET'])
def api_donitsi4():
    res = pd.DataFrame(columns=['name', 'value'])
    dat=pd.read_csv('master.csv')
    df=dat[['menotamount']]
    df2 = df.query('0 <= menotamount < 20000')
    df3 = df.query('20001 <= menotamount < 50000')
    df4 = df.query('50001 <= menotamount < 200000')
    df5 = df.query('200001 <= menotamount < 500000')
    df6 = df.query('500001 <= menotamount')
    dff = res.append({'name': '0 - 20 000 €', 'value':df2['menotamount'].count()}, ignore_index=True)
    dff = dff.append({'name': '20 001 - 50 000 €', 'value':df3['menotamount'].count()}, ignore_index=True)
    dff = dff.append({'name': '50 001 - 200 000 €', 'value':df4['menotamount'].count()}, ignore_index=True)
    dff = dff.append({'name': '200 001 - 500 000 €', 'value':df5['menotamount'].count()}, ignore_index=True)
    dff = dff.append({'name': '500 000- €', 'value':df6['menotamount'].count()}, ignore_index=True)
    return jsonify(dff.to_dict('records'))

@cross_origin()
@application.route('/api/v1/onnistunutdonitsi', methods=['GET'])
def api_donitsi5():
    res = pd.DataFrame(columns=['name', 'value'])
    dat=pd.read_csv('master.csv')
    df=dat[['mean']].fillna(0)
    df2 = df.query('-1 <= mean <= 0')
    df3 = df.query('0 < mean <= 0.5')
    df4 = df.query('0.5 < mean <= 1')
    total = df2['mean'].count() + df3['mean'].count() + df4['mean'].count()
    dff = res.append({'name': 'Huono onnistuminen', 'value':(df2['mean'].count() / total) * 100}, ignore_index=True)
    dff = dff.append({'name': 'Ok onnistuminen', 'value':(df3['mean'].count() / total) * 100}, ignore_index=True)
    dff = dff.append({'name': 'Hyvä onnistuminen', 'value':(df4['mean'].count() / total) * 100}, ignore_index=True)
    return jsonify(dff.to_dict('records'))


@cross_origin()
@application.route('/api/v1/alldata', methods=['GET'])
def all_data():
    data=pd.read_csv('master.csv')
    data['mean']=data['mean'].fillna(0)
    data=data.fillna("")
    return jsonify(data.to_dict('records'))

# run the app.
if __name__ == "__main__":
    application.run()