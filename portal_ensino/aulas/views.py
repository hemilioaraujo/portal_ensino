from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from portal_ensino.usuarios.models import Profile
from portal_ensino.aulas.models import Aulas


@login_required
def aula(request):
    return render(request, 'aula.html',{'usuario': request.user})


@login_required
def proxima_aula(request):
    usuario = Profile.objects.get(user_id=request.user.id)
    aula_id = request.user.profile.aula_atual.id

    if aula_id < 51:
        usuario.aula_atual = Aulas.objects.get(id=aula_id+1)
        usuario.save()

    return redirect('aula')


@login_required
def aula_anterior(request):
    usuario = Profile.objects.get(user_id=request.user.id)
    aula_id = request.user.profile.aula_atual.id

    if aula_id > 1:
        usuario.aula_atual = Aulas.objects.get(id=aula_id-1)
        usuario.save()

    return redirect('aula')