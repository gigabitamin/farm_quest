# 회원가입 로그인

from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from .models import User, UsersAppUser
from .forms import CustomUserCreationForm, UserForm, UserInfoForm

# 마이페이지
# 로그인 관련
from imaplib import _Authenticator
from django.views.generic.edit import DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in
from django.conf import settings

# 네이버 데이터랩 트렌드 그래프
from .templatetags.naver_datalab import *
import io
import base64

# 로그인 메일링
from django.dispatch import receiver
from django.core.mail import send_mail
import smtplib  # SMTP 사용을 위한 모듈
import re  # Regular Expression을 활용하기 위한 모듈
from email.mime.multipart import MIMEMultipart  # 메일의 Data 영역의 메시지를 만드는 모듈
from email.mime.text import MIMEText  # 메일의 본문 내용을 만드는 모듈
from email.mime.image import MIMEImage  # 메일의 이미지 파일을 base64 형식으로 변환하기 위한 모듈

# 기타
from datetime import datetime, timedelta
import os
from django.shortcuts import get_object_or_404, render, redirect



def sign_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)

        if form.is_valid():
            login(request, form.get_user())
            return redirect('index')
        
    else:
        form = AuthenticationForm()

    return render(request, 'users_app/sign_in.html', {'form':form})

def sign_out(request):
    logout(request)
    return redirect('index')

def sign_up(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect('sign_in')
    else:
        form = CustomUserCreationForm()

    return render(request, 'users_app/sign_up.html', {'form':form})

def sign_up2(request):   
    if request.method == 'POST':
        
        username = request.POST['username']        
        email = request.POST['email']
        password = request.POST['password']
        user_name = request.POST['user_name']
        user_phone = request.POST['user_phone']
        user_address = request.POST['user_address']
        preferred_region_no = request.POST['preferred_region_no']
        preferred_accommodation_type_no = request.POST['preferred_accommodation_type_no']
        preferred_tour_theme_type_no = request.POST['preferred_tour_theme_type_no']

        user = UserForm(request.POST)
        # 매개변수는 3개만 전달 가능
        # 순서 주의 : username, email, password

        user = User.objects.create_user(username, email, password)
        # 3개 외 나머지는 별도로 추가
        user.user_name = user_name
        user.user_phone = user_phone
        user.user_address = user_address
        user.preferred_region_no = preferred_region_no
        user.preferred_accommodation_type_no = preferred_accommodation_type_no
        user.preferred_tour_theme_type_no = preferred_tour_theme_type_no
            
        user.save()        

        return redirect('sign_in')
    
    else:
        form = UserForm()

    return render(request, 'users_app/sign_up2.html', {'form':form})







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

    return render(request, 'users_app/my_page.html', {'user_info' : user_info, 'img_data': img_data, 'last_date_str':last_date_str, 'first_date_str':first_date_str})



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
    
    return render(request, 'users_app/my_page_update.html', {'user_form':user_form, 'user_info_update':user_info})



# 회원정보 탈퇴 페이지로 이동 후 회원정보 삭제

class MyPageDeleteView(DeleteView):
    model = UsersAppUser
    success_url = 'index'  # 회원 탈퇴 후 리디렉션할 URL

    # 'my_page_delete_confirm.html' 템플릿을 사용하도록 설정
    template_name = 'users_app/my_page_delete_confirm.html'

@login_required
def my_page_delete_move(request, id):
    user_info = get_object_or_404(UsersAppUser, pk=id)        
    return render(request, 'users_app/my_page_delete_confirm.html', {'user_info':user_info})

@login_required
def my_page_delete(request):
    if request.method == "POST":
        user = request.user  # 현재 로그인한 사용자
        user.delete()  # 사용자 정보 삭제
        return redirect('index')  # 탈퇴 후 리디렉션할 URL
    return render(request, 'users_app/my_page_delete_confirm.html')


