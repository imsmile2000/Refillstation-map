import pandas as pd
from Map.location_to_lati_longi import change

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

