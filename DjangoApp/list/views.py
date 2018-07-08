from django.shortcuts import render
from .models import Users


def index(request):
    users = Users.objects.all()

    context = {'users': users}

    return render(request, 'list/index.html', context)
