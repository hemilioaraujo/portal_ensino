from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserForm(UserCreationForm):
    email = forms.EmailField(required=True, label='E-mail:')
    first_name = forms.CharField(max_length=30, label='Nome:')
    last_name = forms.CharField(max_length=30, label='Sobrenome:')
    username = forms.CharField(max_length=30, label='Usuário:')

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
        ]

        widgets = {
            'password': forms.PasswordInput(attrs={'maxlength': 30})
        }

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class ProfileForm(ModelForm):


    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields["instituicao"].label = "Instituição:"
        self.fields["data_nascimento"].label = "Data de nascimento:"
        self.fields["bio"].label = "Um pouco sobre você:"
        self.fields["foto"].label = "Seu avatar:"

        # pode fazer isso com todos os campos


    class Meta:
        model = Profile
        fields = [
            'instituicao',
            'data_nascimento',
            'bio',
            'foto'
        ]

