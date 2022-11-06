from django.contrib import admin

from .models import PosRegister, Login

@admin.register(PosRegister)
class PosRegisterAdmin(admin.ModelAdmin):
    list_display = ['id','first_name', 'last_name','national_code' , 'created_time', 'updated_time']
    list_filter = ['id', 'first_name', 'last_name', 'national_code']
    search_fields = ['id', 'first_name', 'last_name', 'national_code']

.3.....