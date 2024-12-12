from django.contrib import admin
from .models import Formation, Album, Carte, Certificat, Notification


admin.site.register(Formation)
admin.site.register(Album)
admin.site.register(Carte)
admin.site.register(Certificat)
admin.site.register(Notification)