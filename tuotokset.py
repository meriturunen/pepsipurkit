# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 00:05:47 2020

@author: Meri
"""

import pandas as pd
alkuparsittu = pd.read_csv('alkuparsinta.csv')

#%%
def unique(list1): 
  
    # intilize a null list 
    unique_list = [] 
      
    # traverse for all elements 
    for x in list1: 
        # check if exists in unique_list or not 
        if x not in unique_list: 
            unique_list.append(x) 
    # print list 
    for x in unique_list: 
        print(x)


#%%
import json
import regex as re

outcome = alkuparsittu[['unique', 'project-outcomes']].dropna().reset_index()

outcome_type = []

k = 0 

for k in range(0, len(outcome)):
    
    print(k)
    load = outcome.loc[k, ['project-outcomes']].iloc[0]
    load_parsed1=re.sub(r'(?<=\'value\'\: \"[^\"]*?)(\'|\\t|\\n|\\xa0|,)(?=.*?\")',repl="",string=load)
    load_parsed=re.sub(r'(?<=\'value\'\: \'[^\']*?)(\"|\\n|\\xa0|\\t)(?=.*?\')',repl="",string=load_parsed1)
    load_parsed = load_parsed.replace("\\", "")  #\x
    load_parsed = load_parsed.replace("'", "\"")  #\xa0
    outcome_list = json.loads(load_parsed)
    
    i = 0
    koko = len(outcome_list)
    
    for i in range(0, koko):
        outc_key = outcome_list[i].get("key")
        
        value_list = outcome_list[i].get("value")
        value_koko = len(value_list)
        
        for j in range(0, value_koko):
            
            value = value_list[j].get("key")
            project_outcome = value.split(".")[-1]
            
            if project_outcome == "outcome-type":
                data = value_list[j].get("value")
                
                outcome_type.append(data)
            
            if project_outcome == "description":
                data = value_list[j].get("value")
            
         
outcome_type = unique(outcome_type)