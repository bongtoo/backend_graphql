from django.contrib import admin
from .models import ServiceModel
from import_export.admin import ImportExportModelAdmin 
# Register your models here.

@admin.register(ServiceModel)
class ViewAdmin(ImportExportModelAdmin):
    pass