# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 13:21:46 2020

@author: Meri
"""
import pandas as pd
import json

#%%
summat = pd.read_csv('summat.csv')
practices = pd.read_csv('good_practices.csv')
tuotokset = pd.read_csv('project_outcome_ryhmittely.csv')
tuotokset = tuotokset.drop(["Unnamed: 0"], axis=1)
alueet = pd.read_csv("haku_ja_alueet.csv")
alueet = alueet.drop(["Unnamed: 0"], axis=1)


