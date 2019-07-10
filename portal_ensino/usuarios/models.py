from django.db import models

# Create your models here.
class Usuario(models.Model):
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    instituicao = models.CharField(max_length=30)
    bio = models.TextField()


    def __str__(self):
        return self.nome + " " + self.sobrenome