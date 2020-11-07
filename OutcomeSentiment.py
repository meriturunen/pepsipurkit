# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 13:36:24 2020

@author: Teemu
"""
import pandas as pd
from GCP.NLP import Sentiment

data= pd.read_csv('project_outcome.csv')
data=data.fillna("")
#%%
sent = Sentiment()
#datajoku=data.apply(lambda x: sent.TunnistaSentiment(x["description_en"]),axis=1)
lista=pd.DataFrame()
#%%
i=585
while(i<len(data)):
    arvo=sent.TunnistaSentiment(data.loc[i,"description_en"])
    lista=lista.append(arvo)
    i=i+1
    print(i)

#%%
df_concat=pd.concat([data,lista.set_index(data.index)],axis=1)
df_concat.to_csv('sentiments.csv')