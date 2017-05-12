from django.contrib import admin

from .models import Admin, Alumni, Company


class AlumniAdmin(admin.ModelAdmin):
    search_fields = ['name']


class CompanyAdmin(admin.ModelAdmin):
    search_fields = ['name']


admin.site.register(Alumni)
admin.site.register(Company)
