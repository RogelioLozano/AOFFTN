#!/usr/bin/env python3
import matplotlib.pyplot as plt
import pandas as pd
import os 


def get_mean_af(af):
    af=af.rename(columns={af.columns[0]:'country.value',af.columns[1]:'date'})
    mean_af=pd.DataFrame({'country':af['country.value'],'date':af.date,'mean_af':af.iloc[:,2:].mean(axis=1)})
    mean_af_piv=mean_af.pivot(index='country',columns='date',values='mean_af')
    return mean_af_piv

def load_data():
    pathto=os.path.join(os.getenv('HOME'),'food_trade_network','AOFFTN','Exploration_V2','datasetsV2')
    files=os.listdir(pathto)
    data={}
    for file in files:
        data[file[:5]]=pd.read_csv(os.path.join(pathto,file))
    return data

