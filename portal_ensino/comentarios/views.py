from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from portal_ensino.aulas.models import Aulas
from portal_ensino.base.models import User
from portal_ensino.comentarios.models import Comentarios


def post_comentario(request):
    resposta = request.POST
    comentario = resposta['comentario']
    usuario = User.objects.get(id=request.user.id)
    aula_referente = Aulas.objects.get(id=request.user.aula_atual.id)

    try:
        Comentarios.objects.create(
            comentario=comentario,
            aula_referente=aula_referente,
            user=usuario
        )
    except NameError:
        print('erro ao postar comentário')


@login_required
def delete_comentario(request, id):
    comentario = get_object_or_404(Comentarios, pk=id)

    if request.user.id == comentario.user.id:
        comentario.delete()
        return redirect('base:aula')
    else:
        return redirect('base:aula')
