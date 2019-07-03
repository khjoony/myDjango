"""
from django.shortcuts import render
from django.views.generic import ListView
from .models import Member


index = ListView.as_view(model = Member)
"""
from django.http import HttpResponse
#from .models import Member

def index(request):
    """
    test
    """
    return HttpResponse("Hello , World. You're at the assembly index!")
    