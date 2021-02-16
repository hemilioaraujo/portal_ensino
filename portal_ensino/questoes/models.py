from django.db import models

# Create your models here.
from portal_ensino.aulas.models import Aulas


class Questoes(models.Model):
    questao = models.TextField(blank=False, null=False)
    alt1 = models.TextField(blank=False, null=False)
    alt2 = models.TextField(blank=False, null=False)
    alt3 = models.TextField(blank=False, null=False)
    alt4 = models.TextField(blank=False, null=False)
    resposta_correta = models.TextField(blank=False, null=False)
    aula_referente = models.ForeignKey(Aulas, default=None, blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Questão"
        verbose_name_plural = "Questões"

    def __str__(self):
        return f'Aula: {self.aula_referente} Resposta: {self.resposta_correta}'
