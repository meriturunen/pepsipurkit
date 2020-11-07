# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 23:26:15 2020

@author: Meri
"""

import pandas as pd
import requests

req = requests.get('https://valtionavustukset.oph.fi/api/junction-hackathon/dump')
dat = req.json()

#%%
haku = pd.DataFrame(dat['haku'])
loppu = pd.DataFrame(dat['loppuselvitys'])

#%%

osa_alueet  = { 0: '01 Varhaiskasvatus', 1: '02 Esi- ja perusopetus', 2: '03 Toisen asteen koulutus', 3: '04 Ammatillinen koulutus', 4: '05 Korkeakoulu',
               5: '06 Järjestötoiminta', 6: '07 Vapaa sivistystyö', 7: '08 Muut'}


osa_alueet_id = ["3","0","5","1","1","3","3","3","3","0","1","1","1","2","3","6","3","3","3","1","1","1","0","1","5","3","1","3","3","0","2","2","2","1","4","3","3","3","3","1","1","1","2","1","3","2","0","4","1","1","5","1","2","2","5","2","4","1","3","2","2","2"]
#%%
uusi_df=pd.DataFrame(index=haku.index,data=osa_alueet_id)
uusi_df["id"]=haku["id"]
uusi_df["osa_alue_id"]=uusi_df.loc[:,0].astype(int)
osa_alue_df=pd.Series(osa_alueet)
osa_alue_df=osa_alue_df.rename('osa_alue_nimi')
uusi_df=uusi_df.merge(osa_alue_df,how="left",left_on="osa_alue_id",right_on=osa_alue_df.index)
uusi_df=uusi_df.drop(0,axis=1)
uusi_df["osa_alue_id"]=uusi_df["osa_alue_id"]+1
#%%
uusi_df.to_csv("haku_alue_mappays.csv")
