from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.Dashboard, name='dashboard'),
    path('add-user/', views.AddUser, name='add-user'),
    
    # Cartes
    path('see-cards/', views.SeeCards, name='see-cards'),
    path('toggleViewCard/', views.ToogleViewCard, name='toogle-view-user'),

    # Certificat
    path('view-certificate/<pk>', views.ViewCertificate, name='view-certificate'),
    path('see-certificates/', views.SeeCertificates, name='see-certificates'),
    path('toggleViewCertificate/', views.ToogleViewCertificates, name='toogle-view-certificat'),
    
    # Ajouter matricule
    path('add-matricule/<id>/', views.AddMatricule, name='add-matricule'),
    
    # Notification
    path('receiver-notification/', views.receiverNotification, name='receiver-notification'),
    path('send-notification/<id>', views.sendNotification, name='send-notification'),
    path('see-notifications/', views.seeNotifications, name='see-notifications'),
]