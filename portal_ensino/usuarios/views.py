from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import UserForm, ProfileForm, UserUpdateForm, ProfileUpdateForm

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required
def usuarios_list(request):
    usuarios = User.objects.all()
    return render(request, 'usuarios.html', {'usuarios': usuarios})


def usuarios_novo(request):
    if request.method == 'POST':
        if 'cancel' in request.POST:
            return redirect('home')
        else:
            form_user = UserForm(request.POST, None)
            form_profile = ProfileForm(request.POST, request.FILES, None)

            if form_user.is_valid() and form_profile.is_valid():
                user = form_user.save()

                profile = form_profile.save(commit=False)
                profile.user = user

                profile.save()

                return render(request, 'index.html')
    else:
        form_user = UserForm()
        form_profile = ProfileForm()

    itens_da_pagina = {'form_user': form_user, 'form_profile': form_profile}
    return render(request, 'registration/registro.html', itens_da_pagina)


def do_login(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request,'Nome de usuário ou senha incorretos :(')
            return redirect('login')
    
    return render(request, 'registration/login.html')


def do_logout(request):
    logout(request)
    return redirect('home')


@login_required
def usuario_update(request):
    update_user_form = UserUpdateForm()
    update_profile_form = ProfileUpdateForm()

    itens_da_pagina = {
        'update_user_form': update_user_form,
        'update_profile_form': update_profile_form,
    }

    return render(request, 'atualizar-profile', itens_da_pagina)