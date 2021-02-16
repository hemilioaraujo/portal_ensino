from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from portal_ensino.questoes.models import Questoes


@login_required
def exercicio(request):
    if request.method == 'POST':
        if 'aplicar' in request.POST:
            # print('flag')
            resposta = request.POST
            # print(resposta)

            questoes = Questoes.objects.filter(aula_referente=request.user.aula_atual)
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
                        return redirect('base:proxima_aula')
            return redirect('reprovado')
        else:
            # print('flag')
            resposta = request.POST
            # print(resposta)
            return redirect('base:aula')
    else:
        questoes = Questoes.objects.filter(aula_referente=request.user.aula_atual)

        if len(questoes) == 0:
            return redirect('base:proxima_aula')

        return render(request, 'exercicios.html', {'questoes': questoes})
