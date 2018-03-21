from django.shortcuts import render
from .models import Tarea
# Create your views here.


def index(request):
    list_tarea = Tarea.objects.all()
    context = {'list_tarea': list_tarea}

    return render(request, 'index.html', context)