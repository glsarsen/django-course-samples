from django.contrib import admin
from .models import Page

# Register your models here.

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'update_date', 'permalink')
    ordering = ('title',)
    search_fields = ('title', 'permalink')


# admin.site.register(Page)