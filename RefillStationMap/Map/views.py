from unicodedata import category
from django.shortcuts import render
from Map.models import Store
from Map.location_to_lati_longi import change
from django.core import serializers
# Create your views here.
def store(request):

    # store 카테고리별로 분류해서 json으로 store.html에 넘기기 => res_data 생성할 때 필터링해서 특정 데이터만 넣어
    store = Store()

    list = [['알맹상점','https://almang.modoo.at/','서울특별시 마포구 월드컵로25길 47 3층','세제'],['솝리필스테이션','https://m.blog.naver.com/ati86/222414669203','경기도 성남시 수정구 위례광장로 21 가하빌딩 1층','세제']]
    for refillstation in list:
        if Store.objects.filter(name=refillstation[0]):
            print("이미존재")
        else:
            store.name  = refillstation[0]
            store.site =  refillstation[1]
            lati,longi=change(refillstation[2])
            store.longitude = float(longi)
            store.latitude = float(lati)
            store.category = refillstation[3]
            store.save()

    #들어갔는지 확인
    if(Store.objects.filter(name='알맹상점')):
        print("ok")
    

    return render(request,'store.html')

def map(request):

    # store 카테고리별로 분류해서 json으로 store.html에 넘기기 => res_data 생성할 때 필터링해서 특정 데이터만 넣어
    # 1. 사용자가 고른 값으로 필터링
    input = "세제" #카테고리가 세제인경우.
    stores = Store.objects.filter(category=input)
    print(stores)
    stores_js = serializers.serialize("json", stores)
    print(stores_js)


    return render(request,'store.html',{'res_data' : stores_js})