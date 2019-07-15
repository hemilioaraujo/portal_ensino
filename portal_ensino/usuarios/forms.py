from django.forms import ModelForm
from .models import Usuario

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'nome',
            'sobrenome',
            'email',
            'instituicao',
            'data_nascimento',
            'bio',
            'foto'
        ]