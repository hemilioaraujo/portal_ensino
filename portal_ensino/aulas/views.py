from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from portal_ensino.usuarios.models import Profile
from portal_ensino.aulas.models import Aulas, Questoes, Comentarios


@login_required
def aula(request):
    comentarios = Comentarios.objects.filter(aula_referente=request.user.profile.aula_atual.id)

    return render(request, 'aula.html',{'usuario': request.user, 'comentarios': comentarios})


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


@login_required
def exercicio(request):
    if request.method == 'POST':
        if 'aplicar' in request.POST:
            # print('flag')
            resposta = request.POST
            # print(resposta)

            questoes = Questoes.objects.filter(aula_referente=request.user.profile.aula_atual)
            quantidade_de_questoes = len(questoes)
            acertos = 0

            for questao in questoes:
                # print('flag')
                # print(resposta)
                if questao.resposta_correta == resposta[str(questao.id)]:
                    # print('flag')
                    acertos += 1
                    porcentagem_de_acertos = (acertos * 100) / quantidade_de_questoes

                    if porcentagem_de_acertos > 60.0:
                        # print('flag')
                        # print(f'acertos: {porcentagem_de_acertos:.2f}')
                        # print('aprovado!')
                        return redirect('proxima_aula')
            return redirect('reprovado')
        else:
            # print('flag')
            resposta = request.POST
            # print(resposta)
            return redirect('aula')
    else:
        questoes = Questoes.objects.filter(aula_referente=request.user.profile.aula_atual)

        if len(questoes) == 0:
            return redirect('proxima_aula')

        return render(request, 'exercicios.html',{'questoes': questoes})


@login_required
def reprovado(request):
    return render(request, 'reprovado.html',{'usuario': request.user})