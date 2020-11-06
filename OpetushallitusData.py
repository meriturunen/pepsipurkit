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
#%%
haku.to_excel("hakuexcel.xlsx")
loppu.to_excel("loppuexcel.xlsx")
#%%
df=pd.json_normalize(dat['loppuselvitys'],['loppuselvitys_answers','value'],meta=['haku_id','organization_name','project_name'])

df2=loppu



#%%
df2['unique']=df2[['haku_id','organization_name','project_name']].apply(lambda x: str(x['haku_id'])+str(x['organization_name'])+str(x['project_name']),axis=1)
df['unique']=df[['haku_id','organization_name','project_name']].apply(lambda x: str(x['haku_id'])+str(x['organization_name'])+str(x['project_name']),axis=1)
df2=df2.drop_duplicates('unique')
df=df.drop_duplicates(['unique','key'])
#%%
uniqueKeys=df['key'].unique()
ddf2=df2.copy()
ddf2=ddf2.set_index('unique')
ddf=df[['key','value','unique']]
ddf=ddf.set_index('unique')
for (index,key) in enumerate(df['key'].unique()):
    if((index%100)==0):
        print(index)
    ddf_=ddf[ddf['key']==key]
    ddf_=ddf_.rename(columns={'value':key})
    ddf_=ddf_[key]
    ddf3=ddf2.join(ddf_,on='unique',how="left",lsuffix="l",rsuffix="r")
    ddf2[key]=ddf3[key]

ddf2=ddf2.drop('loppuselvitys_answers',axis=1)
#%%
ddf2.to_excel('parsittu.xlsx')
ddf2.to_csv('alkuparsinta.csv')
#%%