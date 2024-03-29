from django.contrib import admin

from .models import GrantYears


class GrantYearsAdmin(admin.ModelAdmin):
    fields = ['year', 'desc']
    list_display = ('year', 'desc')

admin.site.register(GrantYears, GrantYearsAdmin)
