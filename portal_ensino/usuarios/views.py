from django.shortcuts import render, redirect
from .models import Usuario
from .forms import UsuarioForm

# Create your views here.

def usuarios_list(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios.html', {'usuarios': usuarios})

def usuarios_novo(request):
    form = UsuarioForm(request.POST, request.FILES, None)

    if form.is_valid():
        form.save()
        return redirect('lista_usuarios')
    return render(request, 'usuarios.html', {'form': form})