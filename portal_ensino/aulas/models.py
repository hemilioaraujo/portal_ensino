from django.db import models


class Aulas(models.Model):
    titulo = models.TextField(blank=False, null=False)
    link = models.TextField(blank=False, null=False)

    def __str__(self):
        return f'{self.id} - {self.titulo}'