from django.shortcuts import render, redirect, get_object_or_404
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
def usuarios_update(request):
    if request.method == 'POST':
        if 'cancel' in request.POST:
            return redirect('home')
        else:
            update_user_form = UserUpdateForm(request.POST, instance=request.user)
            update_profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

            if update_user_form.is_valid() and update_profile_form.is_valid():
                update_user_form.save()
                update_profile_form.save()

                return redirect('atualizar_usuario')
    else:
        update_user_form = UserUpdateForm(instance=request.user)
        update_profile_form = ProfileUpdateForm(instance=request.user.profile)

    itens_da_pagina = {
        'update_user_form': update_user_form,
        'update_profile_form': update_profile_form,
        'user': request.user,
    }

    return render(request, 'atualizar_usuario.html', itens_da_pagina)


@login_required
def usuarios_delete(request, id):
    user = get_object_or_404(User, pk=id)

    if request.user.id == id:
        if request.method == 'POST':
            if 'cancel' in request.POST:
                return redirect('atualizar_usuario')
            else:
                user.delete()
                return redirect('home')
        return render(request, 'confirma_deletar_usuario.html', {'user': user})
    else:
        return redirect('home')