from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # 로그인
    path('sign_in', views.sign_in, name='sign_in'),
    path('sign_in2', auth_views.LoginView.as_view(template_name='users_app/sign_in2.html'), name='sign_in2'),
    path('sign_out', views.sign_out, name='sign_out'),    
    path('sign_up', views.sign_up, name='sign_up'),
    path('sign_up2', views.sign_up2, name='sign_up2'),
    
    # 마이 페이지
    path('my_page/', views.my_page, name='my_page'),
    path('my_page/update/<int:id>', views.my_page_update, name='my_page_update'),
    path('my_page/delete/move<int:id>', views.my_page_delete_move, name='my_page_delete_move'),
    path('my_page/delete/', views.my_page_delete, name='my_page_delete'),
    path('my_page/delete/view/', views.MyPageDeleteView.as_view(), name='my_page_delete_view'),


]