# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 11:36:19 2020

@author: Teemu
"""
from Translate import Kaantaja
from google.cloud import language_v1
import pandas as pd
import numpy as np
import proto
import json

#%%


class Sentiment():
    def __init__(self):
        self.kaantaja=Kaantaja()
        self.type_ = language_v1.Document.Type.PLAIN_TEXT
        self.encoding_type = language_v1.EncodingType.UTF8
        self.language = "en"
        self.client=language_v1.LanguageServiceClient.from_service_account_json('school-294823-cff2c6f17e43.json')
    
    def TunnistaSentiment(self,text,toEng=False):
        if(toEng):
            text=self.kaantaja.Kaanna(text)
        document = {"content": text, "type_": self.type_, "language": self.language}
        response = self.client.analyze_sentiment(request = {'document': document, 'encoding_type': self.encoding_type})
        resp2=proto.Message.to_json(response)
        resp=json.loads(resp2)
#        print(resp)
        sentences=resp["sentences"]
        df=pd.json_normalize(sentences)
        try:
            tulos=df[['sentiment.score']].describe()
        except:
            df=pd.DataFrame({'sentiment.score':np.nan},index=[0])
            tulos=df[['sentiment.score']].describe()
        finally:
            return tulos.T
 
#%%  
text_content=r"Olen suomenkielistä kapulatekstiä. Hervannan keittiö on paras."     
sent= Sentiment()
arvot=sent.TunnistaSentiment(text_content,True)        