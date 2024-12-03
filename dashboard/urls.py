from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.Dashboard, name='dashboard'),
    path('add-user/', views.AddUser, name='add-user'),
    
    path('see-cards/', views.SeeCards, name='see-cards'),
    path('toggleViewCard/', views.ToogleViewCard, name='toogle-view-user'),

    path('see-certificates/', views.SeeCertificates, name='see-certificates'),
    path('toggleViewCertificate/', views.ToogleViewCertificates, name='toogle-view-certificat'),
]