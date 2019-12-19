from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.
@login_required
def aula(request):
    return render(request, 'aula.html',{'usuario': request.user})