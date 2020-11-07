# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 13:21:46 2020

@author: Meri
"""
import pandas as pd
import json

#%%
summat = pd.read_csv('summat.csv')
summat = summat.set_index('unique')
practices = pd.read_csv('good_practices.csv')
practices = practices.drop(["Unnamed: 0"], axis=1)
practices = practices.set_index('unique')
tuotokset = pd.read_csv('project_outcome_ryhmittely.csv')
tuotokset = tuotokset.drop(["Unnamed: 0"], axis=1)
tuotokset = tuotokset.set_index('unique')

alueet = pd.read_csv("haku_ja_alueet.csv")
alueet = alueet.drop(["Unnamed: 0"], axis=1)
alueet = alueet.set_index('unique')

#%%

total = pd.concat([summat, practices, tuotokset, alueet], axis=1)

total.to_csv("master.csv")