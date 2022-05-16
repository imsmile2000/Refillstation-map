from unicodedata import category
from django.shortcuts import render
from Map.models import Store
from Map.location_to_lati_longi import change
from django.core import serializers
import json
# Create your views here.
def store(request):

    # store 카테고리별로 분류해서 json으로 store.html에 넘기기 => res_data 생성할 때 필터링해서 특정 데이터만 넣어
    store = Store()
    
    list = [['알맹상점','https://almang.modoo.at/','서울특별시 마포구 월드컵로25길 47 3층','생활용품',json.dumps(['샴푸','비누','칫솔'])],['솝리필스테이션','https://m.blog.naver.com/ati86/222414669203','경기도 성남시 수정구 위례광장로 21 가하빌딩 1층','생활용품',json.dumps(['바디워시','샴푸','린스','섬유유연제','토너'])]]
    print(list)

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
            store.sub_category = refillstation[4]
            # store.save()

    #들어갔는지 확인
    if(Store.objects.filter(name='알맹상점')):
        print("ok")
    

    return render(request,'store.html')

def map(request):

    if request.method == "POST":

        keyword = request.POST['keyword']
        check = request.POST['radiocheck']

        # 1. 사용자가 check한 카테고리를 필터링. => 식품 화장품 생활용품중 하나
        input = check
        stores = Store.objects.filter(category=input)
        print(stores)

        res_data = []

        # 2. 사용자가 입력한 값으로 필터링 -> 세부필터링( 주 카테고리 중에서 keyword에 해당하는 것만 출력)
        input2 = keyword #서브카테고리 키워드
        filter_stores = Store.objects.filter(category=check)
        jsonDec = json.decoder.JSONDecoder()
        for store in filter_stores:
            sub_category = jsonDec.decode(store.sub_category)
            print(sub_category)
            if input2 in sub_category:
                if store in stores:
                    res_data.append(store)
                    print(res_data)
        
        stores_js = serializers.serialize("json", res_data)
        print(stores_js)

        return render(request,'store.html',{'res_data' : stores_js})
    else:
        stores = Store.objects.all()
        stores_js = serializers.serialize("json", stores)
        return render(request,'store.html',{'res_data' : stores_js})