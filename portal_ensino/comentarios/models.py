from django.db import models
from portal_ensino.aulas.models import Aulas
from portal_ensino.base.models import User


# Create your models here.
class Comentarios(models.Model):
    aula_referente = models.ForeignKey(Aulas, default=None, blank=False, null=False, on_delete=models.CASCADE)
    user = models.ForeignKey(User, default=None, blank=False, null=False, on_delete=models.CASCADE)
    comentario = models.TextField(default=None, blank=False, null=False)
    data = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Comentário"
        verbose_name_plural = "Comentários"

    def __str__(self):
        return f'Aula: {self.aula_referente.id} User: {self.user} Comentário: {self.data}'
