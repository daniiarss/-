from django.contrib import admin
from .models import Movie

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'director', 'duration', 'is_active', 'created', 'updated')
    list_filter = ('is_active', 'created', 'updated')
    search_fields = ('name', 'director')
    readonly_fields = ('created', 'updated')

    fieldsets = (
        (None, {
            'fields': ('name', 'director', 'duration', 'is_active')
        }),
        ('Дата', {
            'fields': ('created', 'updated'),
            'classes': ('collapse',)
        }),
    )

