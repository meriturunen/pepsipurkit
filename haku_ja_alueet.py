# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 18:11:08 2020

@author: Meri
"""
import pandas as pd
import json

#%%
mappays = pd.read_csv('haku_alue_mappays.csv')
alkuparsittu = pd.read_csv('alkuparsinta.csv')

#%% 
mappays = mappays.drop("Unnamed: 0",axis=1)
mappays = mappays.set_index('id')

data = alkuparsittu[['unique', 'haku_id']]
#%%
data=data.merge(mappays,how="left",left_on="haku_id",right_on=mappays.index)

#%%

# i = 0

# for i in range(0, len(data)):
#     haku_id = data.loc[i, ['haku_id']][0]
#     osa_alue = mappays.at[haku_id, 'osa_alueet']
    
#     data.osa_alue.iloc[[i]] = osa_alue

#%% 

data.to_csv("haku_ja_alueet.csv")
