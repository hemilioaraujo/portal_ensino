from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from portal_ensino.base.forms import UserUpdateForm, UserForm
from portal_ensino.base.models import User


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


def usuarios_delete(request, id):
    user = get_object_or_404(User, pk=id)

    if request.user.id == id:
        if request.method == 'POST':
            if 'cancel' in request.POST:
                return redirect('base:atualizar_usuario')
            else:
                user.delete()
                return redirect('base:home')
        return render(request, 'user/confirma_deletar_usuario.html', {'user': user})
    else:
        return redirect('base:home')


def usuarios_novo(request):
    if request.method == 'POST':
        if 'cancel' in request.POST:
            return redirect('base:home')
        else:
            form_user = UserForm(request.POST, request.FILES, None)

            if form_user.is_valid():
                form_user.save()

                return render(request, 'registration/login.html')
    else:
        form_user = UserForm()

    itens_da_pagina = {'form_user': form_user}
    return render(request, 'registration/registro.html', itens_da_pagina)


def sobre(request):
    return render(request, "base/sobre.html")


def xpto(request, *args):
    ...
