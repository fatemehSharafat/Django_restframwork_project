from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.utils.translation import ugettext_lazy as _

from .models import User

# class MyUserAdmin(UserAdmin):
#     fieldsets = (
#         (None, {'fields': ('national_code', 'password')}),
#         (_('اطلاعات شخصی'),{'fields': ('first_name','last_name','phone_number','email')}),
#         (_('مجوزها'),{'fields': ('is_active','is_staff','is_superuser')}),
#         (_('تاریخ های مهم'),{'fields': ('last_login','date_joined')}),
#     )
