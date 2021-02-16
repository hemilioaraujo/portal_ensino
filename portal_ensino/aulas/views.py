from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from portal_ensino.aulas.models import Aulas
from portal_ensino.base.models import User
from portal_ensino.comentarios.models import Comentarios
from portal_ensino.comentarios.views import post_comentario


@login_required
def aula(request):
    if request.method == 'POST':
        if 'enviar' in request.POST:
            post_comentario(request)
            return redirect('base:aula')
    else:
        comentarios = Comentarios.objects.filter(aula_referente=request.user.aula_atual.id).order_by('data')
        return render(request, 'aulas/aula.html', {'usuario': request.user, 'comentarios': comentarios})


@login_required
def proxima_aula(request):
    usuario = User.objects.get(id=request.user.id)
    aula_atual_id = request.user.aula_atual.id

    if aula_atual_id < Aulas.objects.last().id:
        usuario.aula_atual = Aulas.objects.get(id=aula_atual_id + 1)
        usuario.save()

    return redirect('base:aula')


@login_required
def aula_anterior(request):
    usuario = User.objects.get(id=request.user.id)
    aula_id = request.user.aula_atual.id

    if aula_id > Aulas.objects.first().id:
        usuario.aula_atual = Aulas.objects.get(id=aula_id-1)
        usuario.save()

    return redirect('base:aula')
