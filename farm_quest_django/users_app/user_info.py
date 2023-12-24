from django.contrib.auth.decorators import login_required


# settings.py TEMPLATES OPTIONS 에 추가

def user_info(request):
    if request.user.is_authenticated:
        user_info = {
            'username': request.user.username,
            'email': request.user.email,        
            # 다른 사용자 정보 필드 추가
        }
        user_info = request.user
    else:
        return {'user_info': None}

    return {'user_info': user_info}