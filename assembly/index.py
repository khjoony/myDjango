"""
test
"""
#from django.shortcuts import render
from django.views.generic import ListView
from .models import Member

MAIN = ListView.as_view(model=Member)
