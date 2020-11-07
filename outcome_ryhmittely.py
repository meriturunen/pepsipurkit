# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 13:36:24 2020

@author: Meri
"""
import pandas as pd
import json
import numpy as np

#%%
tuotokset = pd.read_csv('project_outcome.csv').dropna().reset_index()
df = tuotokset[tuotokset.outcome_type != "0"].reset_index()

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
ryhmitelty = df[['unique', 'outcome_type']]

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

df2.to_csv('project_outcome_ryhmittely.csv')