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
#%%
for key in df['key']:
    df2[key]=df.loc[df['key']==key,'value']
    
#%%
ddf=df[df['key']=='language']
ddf.loc[:,'haku_id']=ddf['haku_id'].astype('int64')
print(ddf.dtypes)
print(df2.dtypes)
df2types=df2.dtypes
ddf2=df2.join(ddf,on=['unique'],how="left",lsuffix="df2_",rsuffix="ddf_")