from django.urls import path
from . import views


urlpatterns = [
    
    path('review_location/<str:keyword>', views.review_location, name='review_location'),
    path('review_facility/<str:keyword>', views.review_facility, name='review_facility'),
    path('review_service/<str:keyword>', views.review_service, name='review_service'),
    path('review_clear/<str:keyword>', views.review_clear, name='review_clear'),
    # path('price_min/', views.price_min, name='price_min'),
    path('discount_rate/<str:keyword>', views.discount_rate, name='discount_rate'),
    path('search_hotels/<str:keyword>', views.search_hotels, name='search_hotels'),
    # path('search_hotels_detail/<str:daily_hotel_num>', views.search_hotels_detail, name='search_hotels_detail'),    

    path('show_map/<str:daily_hotel_name>', views.show_map, name='show_map'),
    path('accommodation_da/<str:keyword>', views.accommodation_da, name='accommodation_da'),
    path('map_main_detail_address/<str:address>', views.map_main_detail_address, name='map_main_detail_address'),
    
    path('youtube_list_user/<str:keyword>', views.youtube_list_user, name='youtube_list_user'),
    path('naver_blog_list_user/<str:keyword>', views.naver_blog_list_user, name='naver_blog_list_user'),

    path('youtube_user_preferred_tour_theme_type/<int:id>', views.youtube_user_preferred_tour_theme_type, name='youtube_user_preferred_tour_theme_type'),
    # path('youtube_user_address/<int:id>', views.youtube_user_address, name='youtube_user_address'),
    path('get_user_address/<int:id>', views.get_user_address, name='get_user_address'),
    path('get_user_preferred_region/<int:id>', views.get_user_preferred_region, name='get_user_preferred_region'),
    path('get_user_preferred_accommodation_type/<int:id>', views.get_user_preferred_accommodation_type, name='get_user_preferred_accommodation_type'),
    path('get_user_preferred_tour_theme_type/<int:id>', views.get_user_preferred_tour_theme_type, name='get_user_preferred_tour_theme_type'),

    # path('sign_up2/', views.sign_up_upload_image, name='sign_up_upload_image,'),
    # path('upload/image/', views.upload_image, name='upload_image,'),
    path('my_page/', views.my_page, name='my_page'),
    path('my_page/update/<int:id>', views.my_page_update, name='my_page_update'),
    path('my_page/delete/move<int:id>', views.my_page_delete_move, name='my_page_delete_move'),
    path('my_page/delete/', views.my_page_delete, name='my_page_delete'),
    path('my_page/delete/view/', views.MyPageDeleteView.as_view(), name='my_page_delete_view'),


    path('youtube/list/<str:keyword>', views.youtube_list, name='youtube_list'),
    path('youtube/detail/<str:youtube_id>', views.youtube_detail, name='youtube_detail'),
    path('youtube/all/lists/', views.youtube_all_lists, name='youtube_all_lists'),
    path('youtube/all/detail/<str:youtube_id>', views.youtube_all_detail, name='youtube_all_detail'),
    path('youtube/insert/', views.youtube_insert, name='youtube_insert'),
    path('youtube/update/<str:youtube_id>', views.youtube_update, name='youtube_update'),
    path('youtube/delete/<str:youtube_id>', views.youtube_delete, name='youtube_delete'),
    path('youtube/search/custom/form/', views.youtube_search_custom_form, name='youtube_search_custom_form'),
    path('youtube/search/custom/', views.youtube_search_custom, name='youtube_search_custom'),
    path('youtube/search/ajax/form', views.youtube_search_ajax_form, name='youtube_search_ajax_form'),
    path('youtube/search/ajax/', views.youtube_search_ajax, name='youtube_search_ajax'),

    path('naver_blog/list/<str:keyword>', views.naver_blog_list, name='naver_blog_list'),
    path('naver_blog/detail/<str:naver_blog_id>', views.naver_blog_detail, name='naver_blog_detail'),          

    # 카메라
    path('upload_photo/', views.upload_photo, name='upload_photo'),

]


