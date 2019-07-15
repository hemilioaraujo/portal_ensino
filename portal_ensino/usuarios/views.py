from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Profile
from .forms import UserForm, ProfileForm


def usuarios_list(request):
    usuarios = User.objects.all()
    return render(request, 'usuarios.html', {'usuarios': usuarios})


def usuarios_novo(request):
    if request.method == 'POST':
        form_user = UserForm(request.POST, None)
        form_profile = ProfileForm(request.POST, request.FILES, None)

        if form_user.is_valid() and form_profile.is_valid():
            user = form_user.save()

            profile = form_profile.save(commit=False)
            profile.user = user

            profile.save()

            return redirect('lista_usuarios')
    else:
        form_user = UserForm()
        form_profile = ProfileForm()

    itens_da_pagina = {'form_user': form_user, 'form_profile': form_profile}
    return render(request, 'registration/registro.html', itens_da_pagina)