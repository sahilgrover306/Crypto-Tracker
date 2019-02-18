from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='coin_list'),
    path('bitcoin/', views.bitcoin, name='bitcoin'),
    path('ethereum/', views.ethereum, name='ethereum'),
    path('litecoin/', views.litecoin, name='litecoin'),

]