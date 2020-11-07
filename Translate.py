# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 10:59:25 2020

@author: Teemu
"""

class Kaantaja():
    def __init__(self):
        from google.cloud import translate_v2 as translate
        self.translate_client = translate.Client.from_service_account_json('SCHOOL-add80de91093.json')
        text="Olen suomenkielistä kapulatekstiä. Hervannan keittiö on paras."
        # Text can also be a sequence of strings, in which case this method
        # will return a sequence of results for each text.
        self.target='en'
        result = self.translate_client.translate(text, target_language=self.target)
        print(u"Text: {}".format(result["input"]))
        print(u"Translation: {}".format(result["translatedText"]))
        print(u"Detected source language: {}".format(result["detectedSourceLanguage"]))

    def Kaanna(self,teksti):
        result = self.translate_client.translate(teksti, target_language=self.target)
                
        print(u"Text: {}".format(result["input"]))
        print(u"Translation: {}".format(result["translatedText"]))
        print(u"Detected source language: {}".format(result["detectedSourceLanguage"]))
       
        return result["translatedText"]
    
kaant=Kaantaja()
kaant.Kaanna("Olen uusi tekstin palanen.")