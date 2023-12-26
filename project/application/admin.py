from django.contrib import admin
from . import models


@admin.register(models.Profile)
class WordAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name']
    list_display_links = ['id', 'full_name']

@admin.register(models.Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ['id', 'profile']
    list_display_links = ['id', 'profile']
# Register your models here.
