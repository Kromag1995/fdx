"""Aca se administran las acciones posibles para admins"""
from django.contrib import admin
from .models import Question
# Register your models here.

admin.site.register(Question)
