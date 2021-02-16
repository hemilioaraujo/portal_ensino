from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from portal_ensino.questoes.models import Questoes


@login_required
def exercicio(request):
    if request.method == 'POST':
        if 'aplicar' in request.POST:
            resposta = request.POST
            questoes = Questoes.objects.filter(aula_referente=request.user.aula_atual)
            quantidade_de_questoes = len(questoes)
            acertos = 0

            for questao in questoes:
                if questao.resposta_correta == resposta[str(questao.id)]:
                    acertos += 1
                    porcentagem_de_acertos = (acertos * 100) / quantidade_de_questoes

                    if porcentagem_de_acertos > 60.0:
                        return redirect('base:proxima_aula')

            return redirect('base:reprovado')
        else:
            resposta = request.POST
            return redirect('base:aula')
    else:
        questoes = Questoes.objects.filter(aula_referente=request.user.aula_atual)

        if len(questoes) == 0:
            return redirect('base:proxima_aula')

        return render(request, 'exercicios.html', {'questoes': questoes})


@login_required
def reprovado(request):
    return render(request, 'reprovado.html', {'usuario': request.user})
