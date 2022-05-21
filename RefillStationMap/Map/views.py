from unicodedata import category
from django.shortcuts import render
from Map.models import Store
from Map.location_to_lati_longi import change
from Map.store_save import stores as st
from django.core import serializers
import json

# Create your views here.
def store(request):

    # store 카테고리별로 분류해서 json으로 store.html에 넘기기 => res_data 생성할 때 필터링해서 특정 데이터만 넣어
    store_del = Store.objects.all()
    print("delete ==================>",store_del)
    store_del.delete()
    print(Store.objects.all())

    store = Store()

    stores = st()

    list=[]

    for i in range(0,len(stores)):
        print([stores['상점명'][i],stores['길찾기'][i],stores['대분류'][i]])
        c_list = stores['대분류'][i].split(',')
        print(c_list)
        category = json.dumps(c_list)
        list.append([stores['상점명'][i],stores['길찾기'][i],stores['lati'][i],stores['longi'][i],category])

    for refillstation in list:
        if Store.objects.filter(latitude=refillstation[2]):
            if Store.objects.filter(longitude=refillstation[3]):
                print("이미존재")
        else:
            store.name  = refillstation[0]
            store.site =  refillstation[1]
            store.latitude = refillstation[2]
            store.longitude = refillstation[3]
            store.category = refillstation[4]
            # store.category = refillstation[5]
            store.save()

    return render(request,'store.html')

def map(request):

    if request.method == "POST":

        keyword = request.POST['keyword']
        check = request.POST['radiocheck']

        # 1. 사용자가 check한 카테고리를 필터링. => 식품 화장품 생활용품중 하나
        input = check
        res_data=[]
        stores = Store.objects.all()
        print("all:=============> ",stores)
        jsonDec = json.decoder.JSONDecoder()
        for store in stores:
            category = jsonDec.decode(store.category)
            print(category)
            if input in category:
                if store in stores:
                    print("=================store:",store)
                    res_data.append(store)
                    print(res_data)

        # 2. 사용자가 입력한 값으로 필터링 -> 세부필터링( 주 카테고리 중에서 keyword에 해당하는 것만 출력)
        # input2 = keyword #서브카테고리 키워드
        # filter_stores = Store.objects.filter(category=check)
        # jsonDec = json.decoder.JSONDecoder()
        # for store in filter_stores:
        #     sub_category = jsonDec.decode(store.sub_category)
        #     print(sub_category)
        #     if input2 in sub_category:
        #         if store in stores:
        #             res_data.append(store)
        #             print(res_data)
        #서브카테고리 데이터 추가 필요.
        
        stores_js = serializers.serialize("json", res_data)
        print(stores_js)

        return render(request,'store.html',{'res_data' : stores_js})
    else:
        stores = Store.objects.all()
        stores_js = serializers.serialize("json", stores)
        return render(request,'store.html',{'res_data' : stores_js})