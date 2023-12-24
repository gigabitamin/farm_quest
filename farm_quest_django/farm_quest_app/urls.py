from django.urls import path
from . import views

urlpatterns = [
    path( '', views.index, name='index'),
    path('customer_service_center/', views.customer_service_center, name='customer_service_center'),

]
