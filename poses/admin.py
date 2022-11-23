from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from .models import PosRegister

@admin.register(PosRegister)
class PosRegisterAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'national_code', 'cerated_time', 'updated_time']
    list_filter = ['id', 'first_name', 'last_name', 'national_code']
    search_fields = ['id', 'first_name', 'last_name', 'national_code']

# class PosRegisterInlineAdmin(admin.StackedInline):
#     model = PosRegister
#     fields = ['id', 'first_name', 'last_name', 'national_code']
#     extra = 0

# @admin.register(Parent)
# class ParentAdmin(admin.ModelAdmin):
#     list_display = ['id','national_code']
#     list_filter = ['national_code']
#     search_fields = ['national_code']
#     # inlines = []
#
