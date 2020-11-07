# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 13:36:24 2020

@author: Meri
"""
import pandas as pd
import json
import numpy as np
#%%
tuotokset = pd.read_csv('project_outcome.csv')
#%%
df_sentiment=pd.read_csv('sentiments.csv')
tuotokset=pd.concat([tuotokset,df_sentiment[['count','mean','std','min','max']].set_index(tuotokset.index)],axis=1)
#%%
tuotokset['outcome_type']=tuotokset['outcome_type'].fillna('0')
df = tuotokset.reset_index()

# toimintamalli
# raportti
# muu-tuotos
# julkaisut-www-sivu-yms             -> verkkosivut
# kasikirja
# julkaisut
# selvitys
# ohjelma
# julkaisu                           -> julkaisut
# tutkimus
# tapahtuma
# koulutus
# opiskelijaliikkuvuudet-lkm
# henkiloestoeliikkuvuudet-lkm
# julkaisut-verkkosivut-yms          -> verkkosivut
# julkaisut-verkkosivu-yms           -> verkkosivut
# materiaalit-julkaisut-www-sivu-tms -> verkkosivut

df.outcome_type.loc[(df.outcome_type == "julkaisut-www-sivu-yms")] = "verkkosivut"
df.outcome_type.loc[(df.outcome_type == "julkaisut-verkkosivut-yms")] = "verkkosivut"
df.outcome_type.loc[(df.outcome_type == "julkaisut-verkkosivu-yms")] = "verkkosivut"
df.outcome_type.loc[(df.outcome_type == "materiaalit-julkaisut-www-sivu-tms")] = "verkkosivut"
df.outcome_type.loc[(df.outcome_type == "julkaisu")] = "julkaisut"

#%%
ryhmitelty = df[['unique', 'outcome_type','count','mean','std','min','max']]

#%%
ryhmitelty['summa'] = 1
ryhma = ryhmitelty.groupby(['unique', 'outcome_type']).count()

#%%
ryhma.reset_index(drop=False, inplace=True)

#%%
types = np.sort(ryhma['outcome_type'].unique())
uniq = np.sort(ryhma['unique'].unique())
df2 = pd.DataFrame(index=uniq)
i = 0
for i in range(0,len(types)):
    df2[types[i]] = ""
  
#%%

ulostulo = []

i = 0
for i in range(0, len(ryhma)):

    projekti = ryhma.loc[i, ['unique']].iloc[0]
    outtype = ryhma.loc[i, ['outcome_type']].iloc[0]
    summa = ryhma.loc[i, ['summa']].iloc[0]
    
    arvot = {outtype: summa}
    
    df2.loc[projekti,outtype]=summa
    
    ulostulo.append(arvot)
    
    
#%%
sentg=ryhmitelty.groupby(['unique'])
sent_df=pd.DataFrame(index=sentg.first().index)

#%%
sent_df.loc[:,'min']=sentg.min()['min']
sent_df.loc[:,'max']=sentg.max()['max']
sent_df.loc[:,'std']=sentg.mean()['std']
sent_df.loc[:,'mean']=sentg.mean()['mean']
df2.loc[:,['min','max','std','mean']]=sent_df[['min','max','std','mean']]

#%%
df3 = df2.reset_index(drop=False, inplace=False)
df3 = df3.rename(columns={'index': 'unique','0':'ei-tuotos-tyyppia'})
#%% 

df3['toimintamalli'] = pd.to_numeric(df3['toimintamalli'])
df3['raportti'] = pd.to_numeric(df3['raportti'])
df3['muu-tuotos'] = pd.to_numeric(df3['muu-tuotos'])
df3['verkkosivut'] = pd.to_numeric(df3['verkkosivut'])
df3['selvitys'] = pd.to_numeric(df3['selvitys'])
df3['ohjelma'] = pd.to_numeric(df3['ohjelma'])
df3['kasikirja'] = pd.to_numeric(df3['kasikirja'])
df3['julkaisut'] = pd.to_numeric(df3['julkaisut'])
df3['tutkimus'] = pd.to_numeric(df3['tutkimus'])
df3['tapahtuma'] = pd.to_numeric(df3['tapahtuma'])
df3['koulutus'] = pd.to_numeric(df3['koulutus'])
df3['opiskelijaliikkuvuudet-lkm'] = pd.to_numeric(df3['opiskelijaliikkuvuudet-lkm'])
df3['henkiloestoeliikkuvuudet-lkm'] = pd.to_numeric(df3['henkiloestoeliikkuvuudet-lkm'])

#%%
df3['sum'] = df3[['toimintamalli', 'raportti', 'muu-tuotos', 'verkkosivut', 'selvitys', 'ohjelma', 
                                      'kasikirja', 'julkaisut', 'tutkimus', 'tapahtuma',
                                      'koulutus', 'opiskelijaliikkuvuudet-lkm', 'henkiloestoeliikkuvuudet-lkm']].sum(axis=1)
df3.to_csv('project_outcome_ryhmittely.csv')

