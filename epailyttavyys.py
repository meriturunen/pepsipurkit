# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 23:48:43 2020

@author: Meri
"""
import pandas as pd

df=pd.read_csv('master.csv')
df.fillna(0, inplace=True)
df=df.set_index('Unnamed: 0')

df['radioButton-good-practices'].loc[(df['radioButton-good-practices'] == "ei")] = 0
df['radioButton-good-practices'].fillna(0, inplace=True)
df['radioButton-good-practices'].loc[(df['radioButton-good-practices'] == "kyllae")] = 1

#%%
total = df[['summaamount', 'osa_alue_nimi', 'sum', 'mean', 'haku_id', 'radioButton-good-practices']]

total_ints = df[['summaamount', 'sum', 'mean']]

# ,'toimintamalli', 'raportti', 'muu-tuotos', 'verkkosivut',
#                                       'kasikirja', 'julkaisut', 'tutkimus', 'tapahtuma',
#                                       'koulutus', 'opiskelijaliikkuvuudet-lkm', 'henkiloestoeliikkuvuudet-lkm',

total.fillna(0, inplace=True)

#%%
total[['haku_id', 'radioButton-good-practices']] = total[['haku_id', 'radioButton-good-practices']].astype(str)

#%%
x = pd.get_dummies(total[['osa_alue_nimi', 'haku_id', 'radioButton-good-practices']])

total = pd.concat([total_ints,x],axis=1)
total.fillna(0, inplace=True)

#%%
# yhdistetty=df[df.columns[pd.Series(df.columns).str.contains('amount')]].fillna(0)

#total = pd.concat([yhdistetty, outcomedf], axis=1)

#%%
import sklearn.mixture.gaussian_mixture as gmm
import sklearn.preprocessing as prepro
scaler=prepro.MinMaxScaler()

#encode = prepro.OneHotEncoder().fit_transform(total['osa_alue_id'].values.reshape(-1,1))

X=total.values
X=scaler.fit_transform(X)
model=gmm.GaussianMixture(n_components=3)
model.fit(X)
total['poikkeavuus']=model.score_samples(X)

#%%
df['poikkeavuus'] = total['poikkeavuus']

#%%

df.to_csv("master_poikkeavuus.csv")
