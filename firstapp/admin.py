from django.contrib import admin
from .models import Client, Project

admin.site.register(Client,admin.ModelAdmin)
admin.site.register(Project,admin.ModelAdmin)