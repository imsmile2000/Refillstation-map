import pandas as pd
from Map.location_to_lati_longi import change
from Map.models import Store
import json

def stores():

    df = pd.read_csv('/Users/baeksujin/Desktop/RefillStationMap/RefillStation_Map/RefillStationMap/Map/stores.csv')

    lati = [0]*len(df)
    longi = [0]*len(df)
    df['lati'] = lati
    df['longi'] = longi
    
    i=0

    for add in df['주소']:
        lati,longi = change(add)
        df['lati'][i] = lati
        df['longi'][i] = longi
        i = i+1

    print(df)
    
    df.to_csv("stores2.csv", index = False)
    return df



def save_stores():
    df = pd.read_csv('/Users/baeksujin/Desktop/RefillStationMap/RefillStation_Map/RefillStationMap/Map/stores2.csv')

    store = Store


    for i in range(0,len(df)):

        category_list = df['대분류'][i].split(',')
        category = json.dumps(category_list)



        store(name = df['상점명'][i], site = df['길찾기'][i], longitude=df['longi'][i],latitude = df['lati'][i], category=category).save()