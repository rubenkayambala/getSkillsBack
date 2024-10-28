from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Formation, Album

def Home(request):
    template_name = 'home/index.html'
    return render(request, template_name)


def Dash(request):
    formations = Formation.objects.all()
    albums = Album.objects.all()
    template_name = 'manage/dash.html'
    context = {
        'formations': formations,
        'albums': albums,
    }
    return render(request, template_name, context)


class addFormation(CreateView):
    model = Formation
    fields = ['name', 'image']
    success_url = "/manage/"
    template_name = 'manage/addFormation.html'

class updateFormation(UpdateView):
    model = Formation
    fields = ['name', 'image']
    success_url = "/manage/"
    template_name = 'manage/updateFormation.html'


class addAlbum(CreateView):
    model = Album
    fields = ['promotion', 'file']
    success_url = "/manage/"
    template_name = 'manage/addAlbum.html'

class updateAlbum(UpdateView):
    model = Album
    fields = ['promotion', 'file']
    success_url = "/manage/"
    template_name = 'manage/updateAlbum.html'