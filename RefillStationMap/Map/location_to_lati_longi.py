#ssl에러 해결
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
#urllib
from urllib.request import urlopen
from urllib import parse
from urllib.request import Request
from urllib.error import HTTPError
import json
# envrion사용해서 key보호
from pathlib import Path
import environ
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Take environment variables from .env
env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# reading .env file
environ.Env.read_env(
    env_file=os.path.join(BASE_DIR, '.env')
)
#naver map api key
client_id = env('client_id')   # 본인이 할당받은 ID 입력
client_pw = env('client_pw')    # 본인이 할당받은 Secret 입력

api_url = 'https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode?query='

def change(address):
    # 네이버 지도 API 이용해서 위경도 찾기
    print(address)
    add_urlenc = parse.quote(address)  
    url = api_url + add_urlenc
    request = Request(url)
    request.add_header('X-NCP-APIGW-API-KEY-ID', client_id)
    request.add_header('X-NCP-APIGW-API-KEY', client_pw)

    try:
        response = urlopen(request)
    except HTTPError as e:
        print('HTTP Error!')
        latitude = None
        longitude = None
    else:
        rescode = response.getcode()
        if rescode == 200:
            response_body = response.read().decode('utf-8')
            response_body = json.loads(response_body)   # json
            if response_body['addresses'] == [] :
                latitude = None
                longitude = None
            else:
                latitude = response_body['addresses'][0]['y']
                longitude = response_body['addresses'][0]['x']
                #위도경도 반환
                return (latitude,longitude)
        else:
            latitude = None
            longitude = None
        
# add = ["서울특별시 중구 필동로1길 30(필동3가)","서울특별시 중구 필동로1길 30(필동3가)"]
# lati_longi=[]
# for i in add:
#     lati,longi=change(i)
#     print(lati,longi)
#     lati_longi.append((lati,longi))