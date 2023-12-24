
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),   
    path('users/', include("users_app.urls")), 
    path('', include("farm_quest_app.urls")),
]


# 카메라 스크린샷 html 화면에 표시

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

