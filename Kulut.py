# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 23:37:32 2020

@author: Teemu
"""
import pandas as pd
data=pd.read_csv('alkuparsinta.csv')
data=data.set_index('unique')
kuludf=data.copy()
kuludf=kuludf[kuludf.columns[pd.Series(kuludf.columns).str.contains('costs')]]
kuludf[kuludf.columns[pd.Series(kuludf.columns).str.contains('amount')]]=kuludf[kuludf.columns[pd.Series(kuludf.columns).str.contains('amount')]].fillna(0)
kuludf['menotamount']=kuludf[kuludf.columns[pd.Series(kuludf.columns).str.contains('amount')]].apply(lambda x: x.sum(),axis=1)
tulot=data.copy()
tulot=tulot[tulot.columns[pd.Series(tulot.columns).str.contains('income')]]
tulot[tulot.columns[pd.Series(tulot.columns).str.contains('amount')]]=tulot[tulot.columns[pd.Series(tulot.columns).str.contains('amount')]].fillna(0)
tulot['tulotamount']=tulot[tulot.columns[pd.Series(tulot.columns).str.contains('amount')]].apply(lambda x: x.sum(),axis=1)

yhdistetty=kuludf.join(tulot)
yhdistetty['summaamount']=yhdistetty['tulotamount']-yhdistetty['menotamount']
#%%
yhdistetty_vain_summat=yhdistetty[yhdistetty.columns[pd.Series(yhdistetty.columns).str.contains('amount')]].fillna(0)
#%%
import sklearn.mixture.gaussian_mixture as gmm
import sklearn.preprocessing as prepro
scaler=prepro.MinMaxScaler()
X=yhdistetty_vain_summat.values
X=scaler.fit_transform(X)
model=gmm.GaussianMixture(n_components=3)
model.fit(X)
yhdistetty_vain_summat['SummienTodennakoisyys']=model.score_samples(X)
yhdistetty_vain_summat.to_csv("summat.csv")
