from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.Home, name='home'),
    path('about/', views.About, name='about'),
    path('manage/', views.Dash, name='dash'),

    path('carte-form/', views.CardForm, name='carte_form'),
    path('carte/', views.Carte, name='carte'),
    path('my-certificat/<int:id>', views.Certif, name='certif'),

    path('manage/addFormation', views.addFormation.as_view(), name='addFormation'),
    path('manage/updateFormation/<int:pk>', views.updateFormation.as_view(), name='updateFormation'),

    path('manage/addAlbum', views.addAlbum.as_view(), name='addAlbum'),
    path('manage/updateAlbum/<int:pk>', views.updateAlbum.as_view(), name='updateAlbum'),
]