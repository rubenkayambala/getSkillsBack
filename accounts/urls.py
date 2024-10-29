from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.Login, name='login'),
    path('register/', views.Register, name='register'),
    path('logout/', views.Logout, name='logout'),

    path('profile/<id>/', views.Profile, name='profile'),
]