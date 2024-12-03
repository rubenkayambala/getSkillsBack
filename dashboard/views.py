from django.shortcuts import render, redirect, get_object_or_404
from accounts.models import CustomUser
from home.models import Formation, Album, Certificat
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required

@login_required
def Dashboard(request):
    template_name = 'dashboard/index.html'
    users = CustomUser.objects.all()
    context = {
        'users': users,
    }
    return render(request, template_name, context)

@login_required
def AddUser(request):
    template_name = 'dashboard/index.html'
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
            picture=request.FILES.get('picture'),
        )
        
        # Utilisez set_password pour hacher le mot de passe
        user.set_password(request.POST.get('password'))  
        user.save()
        
        messages.success(request, "Utilisateur enregistré avec success")
        return redirect('dashboard:dashboard')
    
    return render(request, template_name)


@login_required
def SeeCards(request):
    template_name = 'dashboard/cards.html'
    users = CustomUser.objects.all()
    context = {
        'users': users,
    }
    return render(request, template_name, context)

@login_required
def ToogleViewCard(request):
    template_name = 'dashboard/cards.html'
    if request.method == 'POST':
        userId = request.POST.get('userId')
        user = get_object_or_404(CustomUser, id=userId)
        user.carte_apprenant = not user.carte_apprenant
        user.save()
        messages.success(request, f'Modification effectuée...')
        return redirect('dashboard:see-cards')
    return render(request, template_name)


@login_required
def SeeCertificates(request):
    template_name = 'dashboard/certificats.html'
    users = CustomUser.objects.all()
    context = {
        'users': users,
    }
    return render(request, template_name, context)

@login_required
def ToogleViewCertificates(request):
    template_name = 'dashboard/certificats.html'
    if request.method == 'POST':
        userId = request.POST.get('userId')
        user = get_object_or_404(CustomUser, id=userId)
        user.certificat_apprenant = not user.certificat_apprenant
        user.save()
        messages.success(request, f'Modification effectuée...')
        return redirect('dashboard:see-certificates')
    return render(request, template_name)