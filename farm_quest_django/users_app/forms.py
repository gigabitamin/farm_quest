
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model 
from django.contrib.auth.models import User

from django import forms # 상속
from .models import User, UsersAppUser, PreferredRegion, PreferredAccommodationType, PreferredTourThemeType



# 회원가입 폼 : 빌트인 폼 
# UserCreationForm 상속
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()

        fields = ('username', 'email', 'user_name', 'user_phone', 'user_address', 'preferred_region_no', 'preferred_accommodation_type_no', 'preferred_tour_theme_type_no')

        labels = {
            'username': '아이디',
            'email': '이메일',
            'user_name': '성명',
            'user_phone': '전화번호',
            'user_address': '주소',
            'preferred_region_no' : '선호 여행 지역',
            'preferred_accommodation_type_no' : '선호 숙박 형태',
            'preferred_tour_theme_type_no' :'선호 여행 테마'
        }
        


# 커스텀
class UserForm(forms.ModelForm):
    class Meta:
        model = User

        fields = (
            'username',
            'password',
            'email',
            'user_name',
            'user_phone',
            'user_address',
            'preferred_region_no',
            'preferred_accommodation_type_no',
            'preferred_tour_theme_type_no'
        )

        labels = {
            'username' : '아이디',
            'password' : '비밀번호',
            'email' : '이메일',
            'user_name' : '성명',
            'user_phone' : '전화번호',
            'user_address' : '주소',
            'preferred_region_no' : '선호 여행 지역',
            'preferred_accommodation_type_no' : '선호 숙박 형태',
            'preferred_tour_theme_type_no' :'선호 여행 테마'
        }
        
        
class UserInfoForm(forms.ModelForm):

    class Meta:
        model = UsersAppUser
        
        fields = (
            # 'profile_image'
            'username',
            'email',                     
            'user_name',
            'user_phone',
            'user_address',
            'preferred_region_no',            
            'preferred_accommodation_type_no',
            'preferred_tour_theme_type_no',  
        )

        labels = {
            # 'profile_image':'프로필 이미지'
            'username':'아이디',
            'email':'이메일',            
            'user_name':'성명',
            'user_phone':'전화번호',
            'user_address':'주소',
            'preferred_region_no':'선호 여행 지역',
            'preferred_accommodation_type_no':'선호 여행 타입',
            'preferred_tour_theme_type_no':'선호 여행 테마',    
        }



class UserInfoForm_custom(forms.ModelForm):
    preferred_region_no = forms.ModelChoiceField(queryset=PreferredRegion.objects.all())
    preferred_accommodation_type_no = forms.ModelChoiceField(queryset=PreferredAccommodationType.objects.all())
    preferred_tour_theme_type_no = forms.ModelChoiceField(queryset=PreferredTourThemeType.objects.all())

    class Meta:
        model = UsersAppUser
        
        fields = (
            'email',                     
            'user_name',
            'user_phone',
            'user_address',
            'preferred_region_no',            
            'preferred_accommodation_type_no',
            'preferred_tour_theme_type_no',
            # 'profile_image'    
        )

        labels = {            
            'email':'이메일',            
            'user_name':'성명',
            'user_phone':'전화번호',
            'user_address':'주소',
            'preferred_region_no':'선호 여행 지역',
            'preferred_accommodation_type_no':'선호 여행 타입',
            'preferred_tour_theme_type_no':'선호 여행 테마',
            # 'profile_image':'프로필 이미지'            
        }

