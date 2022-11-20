from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
# from django.contrib.sites.models import Site
from django.utils.translation import ugettext_lazy as _

from .models import User


class MyUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('national_code', 'password')}),
        (_('اطلاعات شخصی'), {'fields': ('first_name', 'last_name', 'phone_number', 'email')}),
        (_('مجوزها'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'group', 'user_permissions')}),
        (_('تاریخ های مهم'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide'),
            'fields': ('national_code', 'phone_number', 'password1', 'password2'),
        }),
    )
    list_display = ('national_code', 'phone_number', 'email', 'is_staff')
    search_fields = ('national_code__exact',)
    ordering = ('-id',)

    def get_search_results(self, request, queryset, search_term):
        queryset, may_have_duplicates = super().get_search_results(
            request, queryset, search_term
        )
        try:
            search_term_as_int = int(search_term)
        except ValueError:
            pass
        else:
            queryset |= self.model.objects.filter(phone_number=search_term_as_int)
        return queryset, may_have_duplicates


admin.site.unregister(Group)
# admin.site.register()
admin.site.register(User, MyUserAdmin)
# admin.site.register(Site)
