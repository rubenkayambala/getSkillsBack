from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Formation, Album, Certificat, Notification
from accounts.models import CustomUser
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def Home(request):
    certif = Certificat.objects.all()
    have_certif = None
    for c in certif:
        if c.user == request.user:
            have_certif = True
        else:
            have_certif = False
    print(have_certif)
    template_name = 'home/index.html'
    return render(request, template_name, {'have_certif': have_certif})

def About(request):
    template_name = 'home/about.html'
    return render(request, template_name)

@login_required
class addCarte(CreateView):
    model = Certificat
    fields = ['user', 'matricule', 'full_name', 'picture']
    success_url = "/certificat/"
    template_name = 'home/carte-form.html'

@login_required
def CardForm(request):
    template_name = 'home/carte-form.html'
    if request.method == "POST":
        # Créer un utilisateur avec les données du formulaire
        certif = Certificat(
            user=request.user,
            matricule=request.POST.get('matricule'),
            full_name=request.POST.get('full_name'),
            picture=request.POST.get('picture'),
        )
        certif.save()
        print(certif)
        messages.success(request, "Vous êtes enregistré avec succès")
        return HttpResponseRedirect(reverse('home:certif', kwargs={'id': id}))  # Redirige vers la page d'accueil ou une autre page
    return render(request, template_name)

@login_required
def Carte(request):
    template_name = 'home/carteApprenant.html'
    return render(request, template_name)

@login_required
def Certif(request, id):
    user = get_object_or_404(CustomUser, id=id)
    cer = get_object_or_404(Certificat, user=user)
    template_name = 'home/certificat.html'
    context = {
        'cer': cer,
        'user': user,
    }
    return render(request, template_name, context)

@login_required
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
