# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 18:44:11 2020

@author: Teemu
"""
import pandas as pd
import requests

req=requests.get('https://valtionavustukset.oph.fi/api/junction-hackathon/dump')
dat=req.json()
#%%
haku=pd.DataFrame(dat['haku'])
loppu=pd.DataFrame(dat['loppuselvitys'])
