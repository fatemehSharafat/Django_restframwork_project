from django.contrib import admin

from .models import PosRegister, Parent

@admin.register(PosRegister)
class PosRegisterAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'national_code', 'cerated_time', 'updated_time']
    list_filter = ['id', 'first_name', 'last_name', 'national_code']
    search_fields = ['id', 'first_name', 'last_name', 'national_code']

class PosRegisterInlineAdmin(admin.StackedInline):
    model = PosRegister
    fields = ['id', 'first_name', 'last_name', 'national_code']
    extra = 0

@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    list_display = ['id','national_code']
    list_filter = ['national_code']
    search_fields = ['national_code']
    inlines = [PosRegisterInlineAdmin]

