from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from portal_ensino.base.forms import UserUpdateForm


def home(request):
    return render(request, 'base/home.html')


@login_required
def exibir_profile(request):
    return render(request, 'user/profile_usuario.html', {'user': request.user})


@login_required
def usuarios_update(request):
    if request.method == 'POST':
        update_user_form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        if 'cancel' in request.POST:
            return redirect('base:home')

        elif 'save' in request.POST:
            if update_user_form.is_valid():
                update_user_form.save()

                return redirect('base:home')

        elif 'atualizar' in request.POST:
            if update_user_form.is_valid():
                update_user_form.save()

                return redirect('base:atualizar_usuario')
    else:
        update_user_form = UserUpdateForm(instance=request.user)

    itens_da_pagina = {
        'update_user_form': update_user_form,
        'user': request.user,
    }

    return render(request, 'user/atualizar_profile.html', itens_da_pagina)


def xpto(request, *args):
    ...
