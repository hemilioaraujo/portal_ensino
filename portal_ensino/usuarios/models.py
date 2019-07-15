from django.db import models

# Create your models here.
class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    instituicao = models.CharField(max_length=30)
    data_nascimento = models.DateField(default='1970-01-01')
    bio = models.TextField(blank=True)
    foto = models.ImageField(upload_to='fotos/profile', null=True, blank=True)


    def __str__(self):
        return self.nome + " " + self.sobrenome

    def get_id(self):
        return f'profile-{self.id}'