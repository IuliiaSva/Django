from django.contrib import admin

from .models import Workplaces

@admin.register(Workplaces)
class WorkplacesAdmin(admin.ModelAdmin):
    list_display = ('number', 'other')
    list_editable = ('other',)
    search_fields = ('number',)
    list_display_links = ('number',)

# Register your models here.
