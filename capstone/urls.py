from django.urls import path
from . import views

urlpatterns = [
    path('', views.artist_list, name='artist_list'),
    path('sounds/', views.sound_list, name='sound_list'),
    path('artist/<int:pk>', views.artist_detail, name='artist_detail'),
    path('sounds/<int:pk>', views.sound_detail, name='sound_detail'),
]