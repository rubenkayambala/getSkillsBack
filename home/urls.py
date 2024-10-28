from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('manage/', views.Dash, name='dash'),

    path('manage/addFormation', views.addFormation.as_view(), name='addFormation'),
    path('manage/updateFormation/<int:pk>', views.updateFormation.as_view(), name='updateFormation'),

    path('manage/addAlbum', views.addAlbum.as_view(), name='addAlbum'),
    path('manage/updateAlbum/<int:pk>', views.updateAlbum.as_view(), name='updateAlbum'),
]
