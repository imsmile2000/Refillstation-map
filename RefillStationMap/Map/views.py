from unicodedata import category
from django.shortcuts import render
from Map.models import Store
from Map.location_to_lati_longi import change
from Map.store_save import stores as st
from Map.store_save import save_stores as savestore
from django.core import serializers
import json

# Create your views here.
def store(request):

    stores = savestore()
    print(stores)

    return render(request,'store.html')

def map(request):

    if request.method == "POST":

        keyword = request.POST['keyword']
        check = request.POST['radiocheck']
        print(keyword,check)

        res_data=[]
        res_data2=[]
        stores = Store.objects.all()

        # 1. 사용자가 check한 카테고리를 필터링. => 식품 화장품 생활용품중 하나
        if not check=="null" and keyword=="":
            for store in stores:
                category = json.loads(store.category)
                if check in category:
                    if store in stores:
                        res_data.append(store)
        elif keyword and (check=="null"):
            filter_stores = Store.objects.filter(name__contains = keyword)
            for store in filter_stores:
                res_data2.append(store)
        elif keyword and (not check=="null"):
            for store in stores:
                category = json.loads(store.category)
                if check in category:
                    if store in stores:
                        res_data.append(store)
            filter_stores = Store.objects.filter(name__contains = keyword)
            for store in filter_stores:
                res_data2.append(store)
        else:
            # filter를 사용하지 않았을때 모두 나오게끔한다
            all_stores = Store.objects.all()
            stores_js = serializers.serialize("json", all_stores)
            return render(request,'store.html',{'res_data' : stores_js})

        res_data3=[]

        print(res_data)
        print(res_data2)
        if keyword and check:

            for i in res_data:
                for j in res_data2:
                    if i==j:
                        res_data3.append(i)
                        print(i)
        elif res_data:
            res_data3 = res_data
        else:
            res_data3 = res_data2

        
        stores_js = serializers.serialize("json", res_data3)
        

        return render(request,'store.html',{'res_data' : stores_js})
    else:
        stores = Store.objects.all()
        stores_js = serializers.serialize("json", stores)
        return render(request,'store.html',{'res_data' : stores_js})