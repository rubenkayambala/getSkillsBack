from django.shortcuts import render, redirect, get_object_or_404
from accounts.models import CustomUser
from home.models import Formation, Album, Certificat, Notification
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
            is_superuser=request.POST.get('superuser'),
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
    template_name = 'dashboard/certificates.html'
    users = CustomUser.objects.all()
    context = {
        'users': users,
    }
    return render(request, template_name, context)

@login_required
def ViewCertificate(request, pk):
    template_name = 'dashboard/certificat.html'
    profile = get_object_or_404(CustomUser, pk=pk)
    context = {
        'profile': profile,
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

@login_required
def AddMatricule(request, id):
    template_name = 'dashboard/addMatricule.html'
    profile = get_object_or_404(CustomUser, id=id)
    if request.method == 'POST':
        profile.matricule = request.POST.get('matricule')
        profile.save()
        return redirect('dashboard:dashboard')
    context = {
        'profile': profile,
    }
    return render(request, template_name, context)

@login_required
def receiverNotification(request):
    template_name = 'dashboard/receiverNotification.html'
    users = CustomUser.objects.all()
    context = {'users': users}
    return render(request, template_name, context)

@login_required
def sendNotification(request, id):
    template_name = 'dashboard/sendNotification.html'
    receiver_id = get_object_or_404(CustomUser, id=id)
    if request.method == "POST":
        # Créer un utilisateur avec les données du formulaire
        notif = Notification(
            sender=request.user,
            receiver=receiver_id,
            content=request.POST.get('content'),
        )
        notif.save()
        messages.success(request, "Notification envoyé avec success")
        return redirect('dashboard:see-notifications')
    return render(request, template_name)

@login_required
def seeNotifications(request):
    template_name = 'dashboard/notifications.html'
    notifs = Notification.objects.all()
    context = {
        'notifs': notifs,
    }
    return render(request, template_name, context)
