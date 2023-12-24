from django import forms
from .models import Youtube
from .models import NaverBlog
from .models import UsersAppUser
from .models import PreferredRegion
from .models import PreferredAccommodationType
from .models import PreferredTourThemeType

class YoutubeForm(forms.ModelForm):
    class Meta:
        model = Youtube
        fields = (
            'youtube_id',
            'youtube_title',
            'youtube_link',
            'youtube_image',
            'youtube_name',
            'youtube_views',
            'youtube_date',
        )

        labels = {
            'youtube_id':'youtube_id',
            'youtube_title':'제목',
            'youtube_link':'URL',
            'youtube_image':'이미지 링크',
            'youtube_channel_name':'채널명',
            'youtube_views':'조회수',
            'youtube_date':'업로드 날짜',
        }

class NaverBlogForm(forms.ModelForm):
    class Meta:
        model = NaverBlog
        fields = (
            'naver_blog_id',
            'naver_blog_title',
            'naver_blog_link',
            'naver_blog_image',
            'naver_blog_hashtag',
            'naver_bloger_name',
            'naver_blog_content_likeit_count',
            'naver_blog_content_date',
        )

        labels = {
            'naver_blog_id' : 'naver_blog_id',
            'naver_blog_title' : 'naver_blog_title',
            'naver_blog_link' : 'naver_blog_link',
            'naver_blog_image' : 'naver_blog_image',
            'naver_bloger_name' : 'naver_blog_hashtag',
            'naver_bloger_name' : 'naver_bloger_name',
            'naver_blog_content_likeit_count' : 'naver_blog_content_likeit_count',
            'naver_blog_content_date' : 'naver_blog_content_date',
        }
        

class ImageForm(forms.Form):
    image = forms.ImageField()



class UserInfoForm(forms.ModelForm):
    # preferred_region_no = forms.ModelChoiceField(queryset=PreferredRegion.objects.all())
    # preferred_accommodation_type_no = forms.ModelChoiceField(queryset=PreferredAccommodationType.objects.all())
    # preferred_tour_theme_type_no = forms.ModelChoiceField(queryset=PreferredTourThemeType.objects.all())
    # preferred_accommodation_type = forms.CharField(max_length=45)
    # preferred_region = forms.CharField(max_length=45)
    # preferred_tour_theme_type = forms.CharField(max_length=45)

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
        #     'preferred_region',            
        #     'preferred_accommodation_type',
        #     'preferred_tour_theme_type',    
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
            # 'preferred_region':'선호 여행 지역',
            # 'preferred_accommodation_type':'선호 여행 타입',
            # 'preferred_tour_theme_type':'선호 여행 테마',       
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


# class UserInfoForm_username(forms.ModelForm):
#     preferred_region_no = forms.ModelChoiceField(queryset=PreferredRegion.objects.all())
#     preferred_accommodation_type_no = forms.ModelChoiceField(queryset=PreferredAccommodationType.objects.all())
#     preferred_tour_theme_type_no = forms.ModelChoiceField(queryset=PreferredTourThemeType.objects.all())

#     class Meta:
#         model = UsersAppUser
        
#         fields = (
#             'username',
#         )

#         labels = {

#             'username':'아이디',
#         }

# class UserInfoForm_email(forms.ModelForm):
#     preferred_region_no = forms.ModelChoiceField(queryset=PreferredRegion.objects.all())
#     preferred_accommodation_type_no = forms.ModelChoiceField(queryset=PreferredAccommodationType.objects.all())
#     preferred_tour_theme_type_no = forms.ModelChoiceField(queryset=PreferredTourThemeType.objects.all())

#     class Meta:
#         model = UsersAppUser
        
#         fields = (

#             'email',

#         )

#         labels = {

#             'email':'이메일',
           
#         }


# class UserInfoForm_password(forms.ModelForm):
#     preferred_region_no = forms.ModelChoiceField(queryset=PreferredRegion.objects.all())
#     preferred_accommodation_type_no = forms.ModelChoiceField(queryset=PreferredAccommodationType.objects.all())
#     preferred_tour_theme_type_no = forms.ModelChoiceField(queryset=PreferredTourThemeType.objects.all())

#     class Meta:
#         model = UsersAppUser
        
#         fields = (

#             'password',            
   
#         )

#         labels = {

#             'password':'비밀번호',
           
#         }


# class UserInfoForm_user_name(forms.ModelForm):
#     preferred_region_no = forms.ModelChoiceField(queryset=PreferredRegion.objects.all())
#     preferred_accommodation_type_no = forms.ModelChoiceField(queryset=PreferredAccommodationType.objects.all())
#     preferred_tour_theme_type_no = forms.ModelChoiceField(queryset=PreferredTourThemeType.objects.all())

#     class Meta:
#         model = UsersAppUser
        
#         fields = (

#             'user_name',            

#         )

#         labels = {

#             'user_name':'성명',
       
#         }


# class UserInfoForm_user_phone(forms.ModelForm):
#     preferred_region_no = forms.ModelChoiceField(queryset=PreferredRegion.objects.all())
#     preferred_accommodation_type_no = forms.ModelChoiceField(queryset=PreferredAccommodationType.objects.all())
#     preferred_tour_theme_type_no = forms.ModelChoiceField(queryset=PreferredTourThemeType.objects.all())

#     class Meta:
#         model = UsersAppUser
        
#         fields = (

#             'user_phone',

#         )

#         labels = {

#             'user_phone':'전화번호',
#         }


# class UserInfoForm_user_address(forms.ModelForm):
#     preferred_region_no = forms.ModelChoiceField(queryset=PreferredRegion.objects.all())
#     preferred_accommodation_type_no = forms.ModelChoiceField(queryset=PreferredAccommodationType.objects.all())
#     preferred_tour_theme_type_no = forms.ModelChoiceField(queryset=PreferredTourThemeType.objects.all())

#     class Meta:
#         model = UsersAppUser
        
#         fields = (

#             'user_address',

#         )

#         labels = {

#             'preferred_region_no':'선호 여행 지역',
          
#         }



# class UserInfoForm_preferred_region_no(forms.ModelForm):
#     preferred_region_no = forms.ModelChoiceField(queryset=PreferredRegion.objects.all())
#     preferred_accommodation_type_no = forms.ModelChoiceField(queryset=PreferredAccommodationType.objects.all())
#     preferred_tour_theme_type_no = forms.ModelChoiceField(queryset=PreferredTourThemeType.objects.all())

#     class Meta:
#         model = UsersAppUser
        
#         fields = (

#             'preferred_region_no',            
 
#         )

#         labels = {

#             'preferred_region_no':'선호 여행 지역',
           
#         }

# class UserInfoForm_preferred_accommodation_type_no(forms.ModelForm):
#     preferred_region_no = forms.ModelChoiceField(queryset=PreferredRegion.objects.all())
#     preferred_accommodation_type_no = forms.ModelChoiceField(queryset=PreferredAccommodationType.objects.all())
#     preferred_tour_theme_type_no = forms.ModelChoiceField(queryset=PreferredTourThemeType.objects.all())

#     class Meta:
#         model = UsersAppUser
        
#         fields = (

#             'preferred_accommodation_type_no',

#         )

#         labels = {

#             'preferred_accommodation_type_no':'선호 여행 타입',
        
#         }


# class UserInfoForm_preferred_tour_theme_type_no(forms.ModelForm):
#     preferred_region_no = forms.ModelChoiceField(queryset=PreferredRegion.objects.all())
#     preferred_accommodation_type_no = forms.ModelChoiceField(queryset=PreferredAccommodationType.objects.all())
#     preferred_tour_theme_type_no = forms.ModelChoiceField(queryset=PreferredTourThemeType.objects.all())

#     class Meta:
#         model = UsersAppUser
        
#         fields = (
#             'preferred_tour_theme_type_no',            
#         )

#         labels = {
#             'preferred_tour_theme_type_no':'선호 여행 테마',
#         }

