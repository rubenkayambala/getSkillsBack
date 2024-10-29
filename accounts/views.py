from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import CustomUser


def Register(request):
    template_name = 'home/index.html'
    if request.method == "POST":
        # Créer un utilisateur avec les données du formulaire
        user = CustomUser(
            username=request.POST.get('username'),
            first_name=request.POST.get('first_name'),
            post_name=request.POST.get('post_name'),
            last_name=request.POST.get('last_name'),
            email=request.POST.get('email'),
            birthday=request.POST.get('birthday'),
            adress=request.POST.get('adress'),
            phone=request.POST.get('phone'),
            picture=request.POST.get('picture'),
        )
        
        # Utilisez set_password pour hacher le mot de passe
        user.set_password(request.POST.get('password'))  
        user.save()
        
        # Authentifier et connecter l'utilisateur après l'enregistrement
        user_ = authenticate(username=user.username, password=request.POST.get('password'))

        if user_ is not None:
            login(request, user_)
            messages.success(request, "Vous êtes enregistré avec succès")
            return HttpResponseRedirect('/')  # Redirige vers la page d'accueil ou une autre page
        else:
            messages.error(request, "Erreur d'authentification. Réessayez.")
    
    return render(request, template_name)


def Login(request):
    if request.method == 'POST':
        username_email = request.POST.get('username_email')
        password = request.POST.get('password')

        if CustomUser.objects.filter(username=username_email).exists():
            user = authenticate(username=username_email, password=password)
        elif CustomUser.objects.filter(email=username_email).exists():
            user = CustomUser.objects.get(email=username_email)
            user = authenticate(username=user.username, password=password)
        else:
            messages.error(request, "Données incorrectes! Réessayez")
            return redirect('home:home')

        if user is not None:
            login(request, user)
            return redirect('home:home')
        else:
            messages.error(request, "Mot de passe incorrect! Réessayez")
            return redirect('home:home')
    
    return render(request, 'home/index.html')


@login_required
def Logout(request):
    logout(request)
    return redirect('home:home')


@login_required
def Profile(request, id):
    template_name = 'accounts/dashboardstudent.html'
    profile = get_object_or_404(CustomUser, id=id)
    return render(request, template_name, {'profile': profile})