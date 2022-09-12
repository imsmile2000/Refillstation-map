from Item.models import Item
import pandas as pd

def item_save():

    df = pd.read_csv('/Users/baeksujin/Desktop/RefillStationMap/RefillStation_Map/RefillStationMap/Item/item.csv')

    item = Item
    for i in range(0,len(df)):

        item(image = df['image'][i], price = df['price'][i], name=df['name'][i],detail = df['detail'][i]).save()

