from django.shortcuts import render
from django.views import generic

from list.models import Tag


def index(request):
    return render(request, 'list/index.html')
