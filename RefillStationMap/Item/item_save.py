from Item.models import Item
import pandas as pd
import re

def item_save():

    df = pd.read_csv('/Users/baeksujin/Desktop/RefillStationMap/RefillStation_Map/RefillStationMap/Item/item2.csv')

    item = Item
    for i in range(0,len(df)):
        price_temp =  df['price'][i]
        price = re.sub(",","",price_temp)
        price = re.sub("원","",price)
        

        item(image = df['image'][i], price = price, name=df['name'][i],detail = df['detail'][i]).save()

