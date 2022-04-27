from django.contrib import admin
from table.models import Table

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('date', 'name', 'count','distance','id')
