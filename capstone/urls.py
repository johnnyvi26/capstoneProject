from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    # path('', views.artist_list, name='artist_list'),
    # path('sounds/', views.sound_list, name='sound_list'),
    # path('artist/<int:pk>', views.artist_detail, name='artist_detail'),
    # path('sounds/<int:pk>', views.sound_detail, name='sound_detail'),
    # path('artists/new', views.artist_create, name='artist_create'),
    # path('sounds/new', views.sound_create, name='sound_create'),
    # path('artists/<int:pk>/edit', views.artist_edit, name='artist_edit'),
    # path('sounds/<int:pk>/edit', views.sound_edit, name='sound_edit'),
    # path('artists/<int:pk>/delete', views.artist_delete, name='artist_delete'),
    # path('sounds/<int:pk>/delete', views.sound_delete, name='sound_delete'),
    
    # path('', views.artist_list, name='artist_list'),
    # path('sounds/<int:pk>', views.sound_detail, name='sound_detail'),

    path('artists/', views.ArtistList.as_view(), name='artist_list'),
    path('artists/<int:pk>', views.ArtistDetail.as_view(), name='artist_detail'),
    path('sounds/', views.SoundList.as_view(), name='sound_list'),
    path('sounds/<int:pk>', views.SoundDetail.as_view(), name='sound_detail'),
]