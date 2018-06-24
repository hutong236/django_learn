from django.contrib import admin
from .models import ActicleColumn

# Register your models here.

class ActicleColumnAdmin(admin.ModelAdmin):
    list_display = ('column','create','user')
    list_filter = ['column']
admin.site.register(ActicleColumn, ActicleColumnAdmin)