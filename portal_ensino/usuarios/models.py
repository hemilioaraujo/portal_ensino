from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import os


def renomear_imagem(instance, filename):
    upload_to = 'fotos/profile/'
    ext = filename.split('.')[-1]

    filename = f'{instance.user}.{ext}'

    return os.path.join(upload_to, filename)


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
