# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 13:16:41 2020

@author: Meri
"""
import pandas as pd
import json

#%%
alkuparsittu = pd.read_csv('alkuparsinta.csv')

#%% 
data = alkuparsittu[['unique','radioButton-good-practices', 'organization_name', 'project_name']]

data.to_csv("good_practices.csv")