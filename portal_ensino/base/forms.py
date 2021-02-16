from django.forms import ModelForm
from django import forms
from portal_ensino.base.models import User
# from django.contrib.auth.forms import UserCreationForm


class UserUpdateForm(ModelForm):
    username = forms.CharField(max_length=150, label='Usuário:')
    first_name = forms.CharField(required=False, max_length=150, label='Nome:')
    last_name = forms.CharField(required=False, max_length=150, label='Sobrenome:')
    email = forms.EmailField(required=False, label='E-mail:')
    bio = forms.CharField(required=False, label='Bio:')
    instituicao = forms.CharField(required=False, label='Instituição:')
    data_nascimento = forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date', 'class': 'calendario'})
    foto = forms.ImageField()

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'bio',
            'instituicao',
            'data_nascimento',
            'foto',
        ]

        widgets = {
            'data_nascimento': forms.widgets.DateInput(
                  format='%Y-%m-%d', attrs={'type': 'date', 'class': 'calendario'})
        }
