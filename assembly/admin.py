"""
test
"""
from django.contrib import admin

# Register your models here.
from .models import Member, Question, Choice

admin.site.register(Member)
admin.site.register(Question)
admin.site.register(Choice)
