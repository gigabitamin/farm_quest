
### 경고 메세지
# import warnings
# warnings.filterwarnings("ignore", category=UserWarning, module="tkinter")

# 기타 등등
import urllib.request
# import datetime
from datetime import datetime, timedelta
import glob
import pandas as pd
import numpy as np
import plotly.express as px

import seaborn as sns
import os
import json
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.shortcuts import get_object_or_404, render, redirect

# 데이터베이스 필터링 관련
from django.db.models import Q
from .models import DailyHotel, NaverBlog, DailyHotelMap
from .models import Youtube
from .forms import YoutubeForm
from .forms import NaverBlogForm

# 메일링
from django.dispatch import receiver
from django.core.mail import send_mail
import smtplib  # SMTP 사용을 위한 모듈
import re  # Regular Expression을 활용하기 위한 모듈
from email.mime.multipart import MIMEMultipart  # 메일의 Data 영역의 메시지를 만드는 모듈
from email.mime.text import MIMEText  # 메일의 본문 내용을 만드는 모듈
from email.mime.image import MIMEImage  # 메일의 이미지 파일을 base64 형식으로 변환하기 위한 모듈

# 이미지 업로드
from .forms import ImageForm

# 로그인 관련
from imaplib import _Authenticator
from django.views.generic.edit import DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.models import User
from users_app.models import User
from django.contrib.auth.signals import user_logged_in
from django.conf import settings

# 커스텀 유저 폼 마이페이지 관련
from .models import UsersAppUser
from .forms import UserInfoForm

# 네이버 데이터랩 트렌드 그래프
from kdy_app.templatetags.naver_datalab import *
import io
import base64

# matplotlib 관련
import matplotlib.pyplot as plt
# plt.rcParams['axes.unicode_minus'] = False
# plt.rcParams['font.family'] = 'Malgun Gothic'
# plt.rcParams['axes.grid'] = False
# pd.set_option('display.max_columns', 250)
# pd.set_option('display.max_rows', 250)
# pd.set_option('display.width', 100)
# pd.options.display.float_format = '{:.2f}'.format

# hotel_search_detail 관련
# from inneats_app.models import Visitkorea
# from inneats_app.models import Restaurant
# from inneats_app.models import Accommodation

# map_main_address 관련
from inneats_app.models import Accommodation
from .models import AccomMap

from django.http import HttpResponseBadRequest


from pathlib import Path



def upload_photo(request):
    if request.method == 'POST':
        # base64로 인코딩된 이미지 데이터 가져오기
        base64_image_data = request.POST.get('photo')

        if not base64_image_data:
            return JsonResponse({'error_message': 'base64_image_data 비어 있음'})

        try:
            # base64 데이터 디코딩
            image_data = base64.b64decode(base64_image_data.split(',')[1])
        except Exception as e:
            return JsonResponse({'error_message': 'base64 data 디코딩 에러 : {}'.format(str(e))})

        # 현재 시간을 이용해 파일명을 생성합니다.
        current_time = datetime.now().strftime('%Y%m%d%H%M%S')
        file_name = f'{current_time}_captured_photo.jpg'

        # 파일의 전체 경로를 생성합니다.
        file_path = Path(settings.MEDIA_ROOT) / file_name

        # 이미지 파일로 저장
        with open(file_path, 'wb') as destination:
            destination.write(image_data)

        # 파일의 전체 URL을 생성합니다.
        file_url = Path(settings.MEDIA_URL) / file_name

        return JsonResponse({'message': 'complete', 'file_path': str(file_path), 'file_name': file_name, 'file_url': str(file_url)})

    return render(request, 'kdy_app/upload_photo.html')









# def upload_photo(request):
#     if request.method == 'POST':
#         # base64로 인코딩된 이미지 데이터 가져오기
#         base64_image_data = request.POST.get('photo')

#         if not base64_image_data:
#             return JsonResponse({'error_message': 'base64_image_data 비어 있음'})

#         try:
#             # base64 데이터 디코딩
#             image_data = base64.b64decode(base64_image_data.split(',')[1])
#         except Exception as e:
#             return JsonResponse({'error_message': 'base64 data 디코딩 에러 : {}'.format(str(e))})

#         # 현재 시간을 이용해 파일명을 생성합니다.
#         current_time = datetime.now().strftime('%Y%m%d%H%M%S')
#         file_name = f'{current_time}_captured_photo.jpg'
#         file_path = 'media/' + file_name

#         # 이미지 파일로 저장
#         with open(file_path, 'wb') as destination:
#             destination.write(image_data)

#         # 파일의 전체 URL을 생성합니다.
#         file_url = request.build_absolute_uri(file_path)

#         return JsonResponse({'message': 'complete', 'file_path': file_path, 'file_name': file_name, 'file_url': file_url})

#     return render(request, 'kdy_app/upload_photo.html')    

# def upload_photo(request):
#     if request.method == 'POST':
#         # base64로 인코딩된 이미지 데이터 가져오기
#         base64_image_data = request.POST.get('photo')

#         if not base64_image_data:
#             return HttpResponseBadRequest('base64_image_data 비어 있음')

#         try:
#             # base64 데이터 디코딩
#             image_data = base64.b64decode(base64_image_data.split(',')[1])
#         except Exception as e:
#             return HttpResponseBadRequest('base64 data 디코딩 에러 : {}'.format(str(e)))

#         # 현재 시간을 이용해 파일명을 생성합니다.
#         current_time = datetime.now().strftime('%Y%m%d%H%M%S')
#         file_name = f'{current_time}_captured_photo.jpg'
#         file_path = 'media/' + file_name

#         # 이미지 파일로 저장
#         with open(file_path, 'wb') as destination:
#             destination.write(image_data)

#         # return JsonResponse({'message': 'complete', 'file_path': file_path, 'file_name': file_name})
#         return render(request, 'kdy_app/upload_photo.html', {'file_name': file_name})

#     return render(request, 'kdy_app/upload_photo.html')








# def user_info_if(request):
#     return 'kdy_app.user_info.user_info' if request.user.is_authenticated else '',


# def user_info_if(request):
#     return {'user_info': 'kdy_app.user_info.user_info'} if request.user.is_authenticated else {'user_info': None}


def review_clear(request, keyword):
    return search_hotels(request, keyword)

def review_service(request, keyword):
    return search_hotels(request, keyword)

def review_facility(request, keyword):
    return search_hotels(request, keyword)

def review_location(request, keyword):
    return search_hotels(request, keyword)

def discount_rate(request, keyword):
    return search_hotels(request, keyword)

# 데일리 호텔 필터링 정렬 처리 결과물 -> limit 걸어서 추천 리스트 로 출력해줄 리스트도 따로 작성해서 같이 변수 처리
def search_hotels(request, keyword):

    ################################### 기본 필터링 ###############################################

    # 'daily_hotel_name' 또는 'daily_hotel_address'에서 keyword 문자열을 포함하고, 'daily_hotel_price'가 NULL이 아닌 행을 검색
    results = DailyHotel.objects.filter(
        (Q(daily_hotel_name__icontains=keyword) | Q(daily_hotel_address__icontains=keyword)) &
        Q(daily_hotel_price__isnull=False)
    ).order_by(
        '-daily_hotel_review_clear', '-daily_hotel_review_service', # 청결도 우선순위
        '-daily_hotel_review_facility', '-daily_hotel_review_location', '-daily_hotel_discount_rate'
    )

    # results 결과물 가격순으로 재정렬
    result_all = sorted(results, key=lambda x: x.daily_hotel_price)
    # 그 결과에서 상위 10개 3개만 선택
    result_top10 = result_all[:10]
    # top10에 sorted 한 번 더 넣은 뒤 top3 뽑는 것도 고려
    result_top3 = result_top10[:3]

    ##################################### column 종류별 정렬 #################################################

    # 최저가순
    price_min = DailyHotel.objects.filter(daily_hotel_discount_rate__isnull=False).order_by('daily_hotel_price')

    # 최저가순
    price_max = DailyHotel.objects.filter(daily_hotel_discount_rate__isnull=False).order_by('-daily_hotel_price')

    # 할인율순
    discount_rate = DailyHotel.objects.filter(daily_hotel_discount_rate__isnull=False).order_by('-daily_hotel_discount_rate')    

    # 리뷰 청결도순
    clear = DailyHotel.objects.filter(daily_hotel_discount_rate__isnull=False).order_by('-daily_hotel_review_clear')

    # 리뷰 서비스순
    service = DailyHotel.objects.filter(daily_hotel_discount_rate__isnull=False).order_by('-daily_hotel_review_service')

    # 리뷰 시설순
    facility = DailyHotel.objects.filter(daily_hotel_discount_rate__isnull=False).order_by('-daily_hotel_review_facility')

    # 리뷰 위치순
    location = DailyHotel.objects.filter(daily_hotel_discount_rate__isnull=False).order_by('-daily_hotel_review_location')


    # return 문
    urls_name = request.resolver_match.url_name
    query = {
                'keyword':keyword, 
                'results':results, 
                'result_all': result_all, 
                'result_top10': result_top10, 
                'result_top3': result_top3,
                'discount_rate':discount_rate,
                'price_min':price_min,
                'price_max':price_max,
                'clear':clear,
                'service':service,
                'facility':facility,
                'location':location,                        
            }              

    # urls 매핑
    if urls_name == 'search_hotels':
        return render(request, 'kdy_app/search_hotels.html', query)

    elif urls_name == 'discount_rate':
        return render(request, 'kdy_app/search_hotels_discount_rate.html', query)

    elif urls_name == 'review_clear':
        return render(request, 'kdy_app/search_hotels_review_clear.html', query)
    
    elif urls_name == 'review_service':
        return render(request, 'kdy_app/search_hotels_review_service.html', query)
    
    elif urls_name == 'review_facility':
        return render(request, 'kdy_app/search_hotels_review_facility.html', query)
    
    elif urls_name == 'review_location':
        return render(request, 'kdy_app/search_hotels_review_location.html', query)    

    else:
        pass


# 맵관련

def show_map(request, daily_hotel_name):
    # dam_results = DailyHotelMap.objects.filter(Q(daily_hotel_name__contains=daily_hotel_name))
    # dam_result_0 = dam_results[0] 
    # , 'dam_result_0':dam_result_0
    da_results = DailyHotel.objects.filter(Q(daily_hotel_name__contains=daily_hotel_name))    
    da_result_0 = da_results[0]

    return render(request, 'kdy_app/show_map.html', {'da_result_0':da_result_0})


# 숙소 검색 후 주소 반환 받아서 해당 주소를 split한 뒤 2번째 주소를 map_main에 전달, 해당 페이지에서 2번째 주소 지도 상세페이지로 바로 이동
def accommodation_da (request, keyword):
    accom_map_list = AccomMap.objects.filter(Q(title__contains=keyword))
    accom_map_address_0 = accom_map_list[0]
    accom_map_address_0_title = accom_map_address_0.title
    accommodation_list = Accommodation.objects.filter(Q(address__contains=keyword))

    accommodation_da = Accommodation.objects.filter(
        (Q(title__icontains=keyword) | Q(address__icontains=keyword)) &
        # (Q(da_price__isnull=False) & Q(go_price__isnull=False) & Q(tr_price__isnull=False) & Q(ya_price__isnull=False))
        Q(da_price__isnull=False)
    )
    accommodation_da_sorted = sorted(accommodation_da, key=lambda x: x.da_price)

    return render(request, 'accommodation_app/accommodation.html',{'keyword':keyword, 'accommodation_list':accommodation_list, 'accommodation_da_sorted':accommodation_da_sorted, 'accom_map_address_0':accom_map_address_0, 'accom_map_address_0_title':accom_map_address_0_title})


# 기본값 제주시(매칭해줄 해당 디테일 맵페이지가 없을 경우)
def map_main_detail_address (request, address):

    map_keywords = address.split(" ")
    if len(map_keywords) >= 2:
        if map_keywords[1] in ('제주시', '서귀포시'):
            region = map_keywords[1]
            if (len(map_keywords) >= 3) and ((map_keywords[2] in ('애월읍', '한림읍', '한경면', '대정읍', '안덕면', '서귀포시', '남원읍', '성산읍', '구좌읍', '조천읍'))):
                region = map_keywords[2]
    else:
        region = "제주시"

    map_url = {
        '제주시': 'map_JejuCity.html',
        '애월읍': 'map_aewol.html',
        '한림읍': 'map_hallimeup.html',
        '한경면': 'map_hngyeongmyeon.html',
        '대정읍': 'map_daejeongeup.html',
        '안덕면': 'map_andeokmyeon.html',
        '서귀포시': 'map_seogwipoCity.html',
        '남원읍': 'map_namwoneup.html',
        '성산읍': 'map_seongsaneup.html',
        '구좌읍': 'map_gujwaeup.html',
        '조천읍': 'map_jocheoneup.html',        
        'jeju-city': 'map_JejuCity.html',
        'aewol-eup': 'map_aewol.html',
        'hallim-eup': 'map_hallimeup.html',
        'hngyeong-myeon': 'map_hngyeongmyeon.html',
        'daejeong-eup': 'map_daejeongeup.html',
        'andeok-myeon': 'map_andeokmyeon.html',
        'seogwipo-city': 'map_seogwipoCity.html',
        'namwon-eup': 'map_namwoneup.html',
        'seongsan-eup': 'map_seongsaneup.html',
        'gujwa-eup': 'map_gujwaeup.html',
        'jocheon-eup': 'map_jocheoneup.html',
        # ... 다른 지역들에 대한 매핑 ...
    }.get(region, 'default_map.html')  # 만약 지역이 매핑에 없으면 기본 맵을 반환
    region_names = {
        '제주시': '제주시',
        '애월읍': '애월읍',
        '한림읍': '한림읍',
        '한경면': '한경면',
        '대정읍': '대정읍',
        '안덕면': '안덕면',
        '서귀포시': '서귀포시',
        '남원읍': '남원읍',
        '성산읍': '성산읍',
        '구좌읍': '구좌읍',
        '조천읍': '조천읍',
        'jeju-city': '제주시',
        'aewol-eup': '애월읍',
        'hallim-eup': '한림읍',
        'hngyeong-myeon': '한경면',
        'daejeong-eup': '대정읍',
        'andeok-myeon': '안덕면',
        'seogwipo-city': '서귀포시',
        'namwon-eup': '남원읍',
        'seongsan-eup': '성산읍',
        'gujwa-eup': '구좌읍',
        'jocheon-eup': '조천읍',
        # ... 다른 지역들에 대한 매핑 ...
    }
    selected_area = region_names.get(region, '알 수 없는 지역')  # 매핑에 없는 지역은 '알 수 없는 지역'으로 반환

    return render(request, 'sjh_app/map_detail.html', {'map_file': map_url, 'selected_area': selected_area, 'map_keywords':map_keywords})



# 마이페이지에 유저의 선호도 지정 키워드 -> 구글트렌드 관련검색어, 네이버 검색트렌드 에 입력 후 반환 된 결과 matplotlib 그래프로 추가
@login_required
def my_page(request):
    user_info = request.user  # 현재 로그인한 사용자
    client_id = "XZc22eND2hDwZOrJ3uAv"
    client_secret = "Ys7etJVJZ5"
    
    now = datetime.now()
    last_date_str = now.strftime("%Y-%m-%d") # 현재 시각
    first_date = now - timedelta(days=365 * 7) # 7년전, 년도 수 다르게 하려면 숫자 7변경, but 7년 이상 넘어갈 시 네이버에서 400 오류
    first_date_str = first_date.strftime("%Y-%m-%d")

    api = NaverDataLabOpenAPI(client_id, client_secret)

    group_dict = {
        'groupName': f'{user_info.preferred_accommodation_type_no.preferred_accommodation_type} {user_info.preferred_tour_theme_type_no.preferred_tour_theme_type} 통합 검색 트렌드',
        'keywords': [user_info.preferred_accommodation_type_no.preferred_accommodation_type, user_info.preferred_tour_theme_type_no.preferred_tour_theme_type]
    }
    api.add_keyword_groups(group_dict)

    startDate = first_date_str
    endDate = last_date_str
    timeUnit = "month"
    device = "pc"
    ages = ["1"]
    gender = "m"

    api.get_data(startDate, endDate, timeUnit, device, ages, gender)

    img_data = api.month_trend()

    return render(request, 'kdy_app/my_page.html', {'user_info' : user_info, 'img_data': img_data, 'last_date_str':last_date_str, 'first_date_str':first_date_str})


# 유저 로그인 시 해당 유저가 설정한 선호 지역 숙소 테마 등을 키워드로 필터링해서 출력
@login_required
def youtube_list_user(request, keyword):
    user_info = request.user  # 현재 로그인한 사용자
    preferred_region_no = get_user_preferred_region(user_info.username) # 테마 타입이 일치하는 유저 정보 

    if preferred_region_no:        
        youtube_data = Youtube.objects.filter(youtube_title__icontains=preferred_region_no)
    else:
        youtube_data = None

    youtube_list = Youtube.objects.all()
    # 추천영상 필터링에 포함
    if len(youtube_data) >= 1:
        youtube_data1 = youtube_data[0]
    else:
        youtube_data1 = youtube_list[0]
    grouped_youtube_list = [youtube_list[i:i+3] for i in range(0, len(youtube_list), 3)]
    return render(request, 'kdy_app/youtube_list.html', {'youtube_data1':youtube_data1, 'youtube_data':youtube_data, 'youtube_list':youtube_list, 'grouped_youtube_list': grouped_youtube_list, 'keyword':keyword})



# 유저 선호도에 따른 필터링 결과 출력
@login_required
def naver_blog_list_user(request, keyword):
    user_info = request.user  # 현재 로그인한 사용자
    preferred_region_no = get_user_preferred_region(user_info.username) # 테마 타입이 일치하는 유저 정보 

    if preferred_region_no:
        naver_blog_data = NaverBlog.objects.filter(naver_blog_title__icontains=preferred_region_no)
    else:
        naver_blog_data = None

    naver_blog_list = Youtube.objects.all()
    # 추천영상 필터링에 포함
    if len(naver_blog_data) >= 1:
        naver_blog_data1 = naver_blog_data[0]
    else:
        naver_blog_data1 = naver_blog_list[0]
    grouped_naver_blog_list = [naver_blog_list[i:i+3] for i in range(0, len(naver_blog_list), 3)]
    return render(request, 'kdy_app/naver_blog_list.html', {'naver_blog_data1':naver_blog_data1, 'naver_blog_data':naver_blog_data, 'naver_blog_list':naver_blog_list, 'grouped_naver_blog_list': grouped_naver_blog_list, 'keyword':keyword})


# 선호 지역을 받아오는 함수
def get_user_preferred_region(username):
    try:
        user_profile = UsersAppUser.objects.get(username=username)        
        return user_profile.preferred_region_no.preferred_region
    
    except UsersAppUser.DoesNotExist:
        return None

# 선호 숙소 형태를 받아오는 함수
def get_user_preferred_accommodation_type(user_id):
    try:
        user = User.objects.get(id=user_id)
        user_profile = UsersAppUser.objects.get(user=user)
        return user_profile.preferred_accommodation_type_no.preferred_accommodation_type
    except User.DoesNotExist:
        return None
    except UsersAppUser.DoesNotExist:
        return None

# 선호 테마를 받아오는 함수
def get_user_preferred_tour_theme_type(user_id):
    try:
        user = User.objects.get(id=user_id)
        user_profile = UsersAppUser.objects.get(user=user)
        return user_profile.preferred_tour_theme_type_no.preferred_tour_theme_type
    except User.DoesNotExist:
        return None
    except UsersAppUser.DoesNotExist:
        return None

# 유저 테이블에 저장된 해당 유저의 주소정보를 받아오는 함수
def get_user_address(user_id):
    try:
        user = User.objects.get(id=user_id)
        user_profile = UsersAppUser.objects.get(user=user)
        return user_profile.user_address
    except User.DoesNotExist:
        return None
    except UsersAppUser.DoesNotExist:
        return None


# 로그인한 유저가 회원가입시 지정한 테마 타입을 키워드로 반환
@login_required
def youtube_user_preferred_tour_theme_type(request):
    user_info = request.user # 로그인 유저 정보 저장
    preferred_tour_theme_type_no = get_user_preferred_region(user_info.id) # 테마 타입이 일치하는 유저 정보 

    if preferred_tour_theme_type_no:
        # 'preferred_tour_theme_type_no' 변수의 'preferred_tour_theme_type' 값이 'Youtube' 모델의 'youtube_title' 필드에 포함되는 비디오를 검색
        youtube_user_preferred_tour_theme_type = Youtube.objects.filter(youtube_title__icontains=preferred_tour_theme_type_no.preferred_tour_theme_type)
    else:
        youtube_user_preferred_tour_theme_type = None        

    return render(request, 'your_app/youtube_list.html', {'youtube_user_preferred_tour_theme_type': youtube_user_preferred_tour_theme_type})



# 회원정보 수정
@login_required
def my_page_update(request, id):  
    user_info = get_object_or_404(UsersAppUser, pk=id)
    if request.method == "POST":
        user_form = UserInfoForm(request.POST, instance=user_info)
        if user_form.is_valid():
            user_info = user_form.save(commit=False)
            user_info.save()
            return redirect('index')
    else:
        user_form = UserInfoForm(instance=user_info)
    
    return render(request, 'kdy_app/my_page_update.html', {'user_form':user_form, 'user_info_update':user_info})



# 회원정보 탈퇴 페이지로 이동 후 회원정보 삭제

class MyPageDeleteView(DeleteView):
    model = UsersAppUser
    success_url = 'index'  # 회원 탈퇴 후 리디렉션할 URL

    # 'my_page_delete_confirm.html' 템플릿을 사용하도록 설정
    template_name = 'kdy_app/my_page_delete_confirm.html'

@login_required
def my_page_delete_move(request, id):
    user_info = get_object_or_404(UsersAppUser, pk=id)        
    return render(request, 'kdy_app/my_page_delete_confirm.html', {'user_info':user_info})

@login_required
def my_page_delete(request):
    if request.method == "POST":
        user = request.user  # 현재 로그인한 사용자
        user.delete()  # 사용자 정보 삭제
        return redirect('index')  # 탈퇴 후 리디렉션할 URL
    return render(request, 'kdy_app/my_page_delete_confirm.html')


# # 이미지 업로드
# def sign_up_upload_image(request):
#     if request.method == 'POST':
#         form = ImageForm(request.POST, request.FILES)
#         if form.is_valid():
#             image = form.cleaned_data['image']
#             ImageForm.objects.create(image=image)
#             return redirect('users_app/sign_up2.html')
#     else:
#         form = ImageForm()
#     return render(request, 'users_app/sign_up2.html', {'form': form})


# @login_required
# def upload_image(request):
#     if request.method == 'POST':
#         form = ImageForm(request.POST, request.FILES)
#         if form.is_valid():
#             image = form.cleaned_data['image']
#             ImageForm.objects.create(image=image)
#             return redirect('kdy_app/my_page.html')
#     else:
#         form = ImageForm()
#     return render(request, 'kdy_app/my_page.html', {'form': form})


def youtube_list(request, keyword):
    # keyword 가 포함된 youtube_title을 db에서 검색한 뒤 해당 row가 존재하면 불러와서 youtube_data 에 저장, 
    # 리스트 일 시 첫행만 반환, 해당 조건으로 검색해서 결과값이 없을 시 all_list 에서 첫 행 반환 
    # 필터링으로 추천 리스트 테이블을 따로 만들어 둔 뒤에 그 테이블에서 첫 행을 반환시켜서 해당 keyword와 관련된 '오늘의 추천 유투브' 라는 식으로 출력할 것
    # 추천 리스트는 view나 instance 로 만들어도 되고 해당 테이블 정렬 순서는 필터링 상 가장 첫 행이 가장 추천 가치가 높도록 
    # 객관적 수치(조회수 댓글 수 좋아요 수 등) 을 비교해서 정렬 될 수 있도록 짤 것
    # 해당 절차를 다른 컨텐츠 페이지에 동일하게 적용
    youtube_data = Youtube.objects.filter(youtube_title__icontains=keyword)
    youtube_list = Youtube.objects.all()

    # 추천영상 필터링에 포함
    if len(youtube_data) > 1:
        youtube_data1 = youtube_data[0]
    else:
        youtube_data1 = youtube_list[0]
    grouped_youtube_list = [youtube_list[i:i+3] for i in range(0, len(youtube_list), 3)]
    return render(request, 'kdy_app/youtube_list.html', {'youtube_data1':youtube_data1, 'youtube_data':youtube_data, 'youtube_list':youtube_list, 'grouped_youtube_list': grouped_youtube_list, 'keyword':keyword})

    # 3개씩 묶어서 출력 -> for 문 출력시 css 문제로 1개씩 출력할경우 1개별로 행이 달라지는 문제가 발생, 3개씩 미리 구성후 한 행에 3개씩 출력
    # if len(youtube_list) % 3 == 0:
    #     print()
    # for i in grouped_youtube_list
    # grouped_youtube_list[0]
    # grouped_youtube_list[1]
    # grouped_youtube_list[2]
    



def naver_blog_list(request, keyword):
    naver_blog_data = NaverBlog.objects.filter(naver_blog_title__icontains=keyword)
    naver_blog_list = NaverBlog.objects.all()        
    if len(naver_blog_data) > 1:
        naver_blog_data1 = naver_blog_data[0]
    else:
        naver_blog_data1 = naver_blog_list[0]
    grouped_naver_blog_list = [naver_blog_list[i:i+3] for i in range(0, len(naver_blog_list), 3)]
    return render(request, 'kdy_app/naver_blog_list.html', {'naver_blog_data1':naver_blog_data1, 'naver_blog_data':naver_blog_data,'naver_blog_list':naver_blog_list, 'grouped_naver_blog_list': grouped_naver_blog_list, 'keyword':keyword})











# 로그인 시 유저에게 이메일 발송 - 프로젝트 종료로 메일링 기능 임시 정지

# @receiver(user_logged_in)
# def send_login_email(sender, request, user, **kwargs):
#     # 사용자 정보에서 이메일 주소 가져오기
#     user_email = user.email
#     inneats_user_id = user.username
#     # 이메일 보내기
#     send_mail(user_email, inneats_user_id)

# 로그인시 해당 유저 이메일로 자동 메일 발송
def send_mail(to_email, inneats_user_id):
    # py 파일명이 email 일 경우 에러나니 변경할 것
    # 해당 기능 전체를 함수화해서 사용할 것, Class modeul로 빼는 것도 고려
    # def sendEmail (from_email, to_email, from_email_password, inneats_user_id): 

    # Gmail 계정에서 IMAP 설정
    # https://mail.google.com/mail/u/0/#settings/fwdandpop
    # 해당 설정에서 IMAP 을 사용상태로 open 해줘야 타클라이언트에서 gmail 전송 사용가능
    # https://myaccount.google.com/security
    # app_password = '본인 app password' # 2차 로그인을 하는 계정일 시 구글 보안설정에서 app 패스워드 설정 후 입력 필요

    # 발송자 정보
    from_email = 'gigabitamin@gmail.com' # 보낼 계정
    from_email_password = 'kywqqehhchzcqszu'

    # 수신자 정보
    to_email = 'myanyhoney@gmail.com' # 수신할 계정 # 여러명에게 보낼 땐 [] 로 리스트 처리
    inneats_user_id = inneats_user_id

    # 보낼 내용
    now = datetime.now()
    send_subject = f'{inneats_user_id}님께서 {now}에 InnEats에 로그인 하셨습니다' # 제목
    text = f"\
        안녕하세요 {inneats_user_id}님\n\
        InnEats에 오신 것을 환영합니다"
    html = f"<html><body><h1>{now}</h1><p>{text}</p></body></html>"

    # 서버와 연결
    smtp_server = 'smtp.gmail.com' # gmail smtp 주소
    smtp_port = 465  # gmail smtp 포트번호
    server = smtplib.SMTP_SSL(smtp_server, smtp_port) # SMTP 객체
    
    # 로그인
    server.login(from_email, from_email_password)
    
    # 메일 기본 정보 설정
    msg = MIMEMultipart("alternative")
    msg["Subject"] = send_subject
    msg["From"] = from_email
    msg["To"] = to_email

    # 메일 본문 _email내용
    text_part = MIMEText(text, "plain")
    html_part = MIMEText(html, "html")
    msg.attach(text_part)
    msg.attach(html_part)
    
    # 이미지 파일 추가
    # image_path = "{% static 'img/logo/inneats/InnEats_logo_temp.png' %}" --> load static 실행 안됨, 절대 결로 or 상대 경로 처리
    # image_path = "C:\djangoWorkspace/InnEats_logo_temp.png"
    # image_path = "../../../static/img/logo/inneats/InnEats_logo_temp.png"
    
    image_path = os.path.join(settings.STATIC_ROOT, 'img/kdy/logo/inneats/InnEats_logo_temp.png')
    
    # 'rb' read binary, 2진 데이터로 처리 -> 이미지 로딩 가능
    with open(image_path, 'rb') as file: 
        img = MIMEImage(file.read())
        img.add_header('Content-Disposition', 'attachment', filename=image_path)
        msg.attach(img)
    
    # 받는 메일 유효성 검사 거친 후 메일 전송
    # 올바른 형식으로 보내는지 정규식 검사
    reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"
    try:
        if re.match(reg, to_email):
            server.sendmail(from_email, to_email, msg.as_string())
            print("정상적으로 메일이 발송되었습니다")
        else:
            print("받으실 메일 주소를 정확히 입력하십시오")
    except Exception as e:
        print("error", e)
    
    # smtp 서버 연결 해제
    server.quit()




# # 개별 정보 수정 -- 전체수정에서 개별 수정이 가능해서 필요 없어지고 임시 기능 정지
# @login_required
# def my_page_update_email(request, id):  
#     user_info = get_object_or_404(UsersAppUser, pk=id)    
#     if request.method == "POST":
#         user_form = UserInfoForm_email(request.POST, instance=user_info)
#         if user_form.is_valid():
#             user_info = user_form.save(commit=False)
#             user_info.save()
#             return redirect('index')
#     else:
#         user_form = UserInfoForm_email(instance=user_info)
    
#     return render(request, 'kdy_app/my_page_update.html', {'user_form':user_form, 'user_info':user_info})


# # 페이지별 세션 처리 문제 -> kdy_app/user_info.py 컨텍스트 로 해결

# @login_required
# def my_page(request):
#     user_info = request.user  # 현재 로그인한 사용자
#     if user_info.is_authenticated and user_info.id == id:
#         return render(request, 'kdy_app/my_page.html', {'user_info': user_info})
#     else:
#         # 로그인하지 않은 사용자나 다른 사용자의 마이페이지에 접근하려는 경우 리디렉션
#         return redirect('sign_in')  


# @receiver(user_logged_in, dispatch_uid="set_session")
# def set_session(sender, request, user, **kwargs):
#     user_info = user
#     request.session['id'] = user_info.id
#     return HttpResponse("Session data set.")

# @receiver(user_logged_in, dispatch_uid="get_session")
# def get_session(sender, request, user, **kwargs):
#     user_id = request.session.get('id')  # 세션에서 데이터 읽기
#     return HttpResponse(f"User ID: {user_id}")

# @receiver(user_logged_in, dispatch_uid="get_session")
# def login_view(sender, request, user, **kwargs):
#     if request.method == 'POST':
#         username = request.POST['username']
#         user = _Authenticator(request, username=username, password='password')
#         if user:
#             login(request, user)
#             # 클라이언트 측 로컬 스토리지에 로그인 정보 저장
#             response = JsonResponse({'message': '로그인 성공'})
#             response.set_cookie('user', username, max_age=settings.SESSION_COOKIE_AGE) # 3일
#             return response
#         else:
#             return JsonResponse({'message': '로그인 실패'})


























































# CRUD 연습용으로 넣었다가 삭제한 기능들
# insert 게시글 등록 기능은 살려서 유저가 직접 컨텐츠를 등록할 수 있는 폼으로 활용할 것
# 게시판 용도로 재활용 가능하도록 만들 것

def naver_blog_detail(request, naver_blog_id):
    NaverBlog = get_object_or_404(NaverBlog, pk=naver_blog_id)
    return render(request, 'kdy_app/naver_blog_detail.html', {'NaverBlog':NaverBlog})

def youtube_detail(request, youtube_id):
    youtube = get_object_or_404(Youtube, pk=youtube_id)
    return render(request, 'kdy_app/youtube_detail.html', {'youtube':youtube})

def youtube_list_kdy(request,keyword):
    return render(request, 'kdy_app/youtube_list_kdy.html',{'keyword':keyword})

def youtube_all_lists(request):
    youtube_all_lists = Youtube.objects.all()
    return render(request, 'kdy_app/youtube_all_lists.html', {'youtube_all_lists':youtube_all_lists})

def youtube_all_detail(request, youtube_id):
    youtube = get_object_or_404(Youtube, pk=youtube_id)
    return render(request, 'kdy_app/youtube_all_detail.html', {'youtube':youtube})

# 등록
def youtube_insert(request):    
    if request.method == "POST":        
        form = YoutubeForm(request.POST)
        # 데이터 유효성 확인
        if form.is_valid():
            youtube = form.save(commit=False)            
            youtube.save()
            return redirect('youtube_all_lists')
    else:
        form = YoutubeForm()
    
    return render(request, 'kdy_app/youtube_all_insert.html', {'form':form})
        
# 수정
def youtube_update(request, youtube_id):  
    youtube = get_object_or_404(Youtube, pk=youtube_id)    
    if request.method == "POST":        
        form = YoutubeForm(request.POST, instance=youtube)        
        if form.is_valid(): # 저장 지연
            youtube = form.save(commit=False)
            youtube.save() # 저장
            return redirect('youtube_all_lists')
    else:
        form = YoutubeForm(instance=youtube)
        # 폼에 youtube_id 에 해당되는 상품 데이터 출력
    
    return render(request, 'kdy_app/youtube_all_update.html', {'form':form})

# 삭제
def youtube_delete(youtube_id):
    youtube = get_object_or_404(Youtube, pk=youtube_id)    
    youtube.delete()
    return redirect('youtube_list')

# 검색창 열기
def youtube_search_custom_form(request):
    return render(request, 'kdy_app/youtube_search_custom.html')

# 검색 쿼리 수행
def youtube_search_custom(request):
    if request.method == "POST":
        type = request.POST['type']
        keyword = request.POST['keyword']

        print(type, keyword)

        if type == "youtube_title":
            youtube_list = Youtube.objects.filter(Q(youtube_title__contains=keyword)) 
        elif type == "youtube_channel_name":
            youtube_list = Youtube.objects.filter(Q(youtube_channel_name__contains=keyword))
        elif type == "youtube_hashtag":
            youtube_list = Youtube.objects.filter(Q(youtube_hashtag__contains=keyword))
        else: 
            pass

        return render(request, 'kdy_app/youtube_search_custom.html', {'youtube_list':youtube_list})

def youtube_search_ajax_form(request):
    return render(request, 'kdy_app/youtube_search_ajax.html')

def youtube_search_ajax(request):
    if request.method == "POST":
        type = request.POST['type']
        keyword = request.POST['keyword']

        print(type, keyword)

        if type == "youtube_title":
            youtube_list = Youtube.objects.filter(Q(youtube_title__contains=keyword)) 
        elif type == "youtube_channel_name":
            youtube_list = Youtube.objects.filter(Q(youtube_channel_name__contains=keyword))
        elif type == "youtube_hashtag":
            youtube_list = Youtube.objects.filter(Q(youtube_hashtag__contains=keyword))
        else: 
            pass
        
        # youtube_list 쿼리 데이터 셋을 JSON 타입으로 변환
        youtube_list_json = json.loads(serializers.serialize('json', youtube_list, ensure_ascii=False))

        return JsonResponse({'reload_all':False, 'youtube_list_json':youtube_list_json})
    

