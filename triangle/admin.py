from django.contrib import admin

from .models import Logs


@admin.register(Logs)
class LogAdmin(admin.ModelAdmin):
    list_display = ('path', 'method', 'data', 'timestamp', )
    search_fields = ('data',)
    list_filter = ('timestamp', )
    date_hierarchy = 'timestamp'
    list_per_page = 15
    ordering = ('-timestamp',)
    list_editable = ('method', )
    readonly_fields = ('timestamp',)
