from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from PIL import Image
import os


def renomear_imagem(instance, filename):
    upload_to = 'fotos/profile/'
    ext = filename.split('.')[-1]

    filename = f'{instance.user}.{ext}'

    return os.path.join(upload_to, filename)


def email_unico(value):
    exists = User.objects.filter(email=value)
    if exists:
        raise ValidationError(f'O e-mail {value} já está cadastrado!')


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    instituicao = models.CharField(max_length=30)
    data_nascimento = models.DateField(default='1970-01-01')
    bio = models.TextField(blank=True)
    foto = models.ImageField(upload_to=renomear_imagem, default='fotos/profile/default.jpeg', null=True, blank=True)

    def __str__(self):
        return f'Usuário: {self.user.username} Email: {self.user.email}'

    def save(self):
        super().save()

        img = Image.open(self.foto.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.foto.path)


# ELIMINA A IMAGEM DE PROFILE QUANDO O MESMO É EXCLUIDO
@receiver(post_delete, sender=Profile)
def deletar_imagem_profile(sender, instance, **kwargs):
    if instance.foto.url == '/media/fotos/profile/default.jpeg':
        pass
    else:
        instance.foto.delete(False)