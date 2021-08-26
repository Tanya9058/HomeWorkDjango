from django.contrib import admin
from .models import New, Rubric


@admin.register(New)
class AdminNew(admin.ModelAdmin):
    list_display = ['id', 'title', 'rubric']


@admin.register(Rubric)
class AdminRubric(admin.ModelAdmin):
    list_display = ['id', 'name']

