from django.contrib import admin

# Register your models here.

from . import models

admin.site.register(models.Nata)
admin.site.register(models.Tipo)
admin.site.register(models.Position)
