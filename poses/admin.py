from django.contrib import admin
from django.contrib.auth import get_user_model

from import_export.admin import ImportExportModelAdmin
from jalali_date import datetime2jalali, date2jalali
from jalali_date.admin import ModelAdminJalaliMixin

from .models import PosRegister



User= get_user_model()

@admin.register(PosRegister)
class PosRegisterAdmin(ImportExportModelAdmin,ModelAdminJalaliMixin, admin.ModelAdmin):
    # fieldsets = (
    #     (None, {'fields': ('user',)}),
    #     (_('اطلاعات شخص متقاضی'), {'fields': ('first_name', 'last_name', 'father_name', 'birth','mobile','national_code','national_card_series','birthcertificate_number','birthcertificate_serial','birthcertificate_series','issued','state', 'city')}),
    #     (_('اطلاعات تکمیلی'), {'fields': ('store_name','store_address', 'zipcode_pos','store_phone', 'business_license_number', 'tax_code','senf','substrate','ownership','leaseterm_from','leaseterm_to')}),
    #     (_('معرفین'), {'fields': ('first_introducer_name','first_introducer_lastname','first_introducer_phone','first_introducer_address','second_introducer_name','second_introducer_lastname','second_introducer_phone', 'second_introducer_address')}),
    #     (_('اطلاعات حساب بانکی'), {'fields': ('first_account_number','first_bank_name','first_shaba_number','second_account_number','second_bank_name','second_shaba_number')}),
    #     (_('پذیرش و مدارک'), {'fields': ('paziresh','businesslicense','leaseterm','ownership_document','birthcertificate', 'birthcertificate','back_nationalcard','signatureseal','sabin_form_first','sabin_form_second' )}),
    #     (_('سایر اطلاعات'), {'fields': ('cerated_time','updated_time','status')})
    #
    # )
    # # add_fieldsets = (
    # #     (None, {
    # #         'classes': ('wide'),
    # #         'fields': ('national_code', 'phone_number', 'password1', 'password2'),
    # #     }),
    # # )
    list_display = ['id', 'first_name', 'last_name', 'national_code','get_birth_jalali','get_updated_time_jalali']
    list_filter = ['id', 'first_name', 'last_name', 'national_code']
    search_fields = ['id', 'first_name', 'last_name', 'national_code']

    def get_updated_time_jalali(self, obj):
        return datetime2jalali(obj.updated_time).strftime('%y/%m/%d _ %H:%M:%S')

    get_updated_time_jalali.short_description = 'زمان بروز رسانی'
    get_updated_time_jalali.admin_order_field = 'updated_time'

    def get_birth_jalali(self, obj):
        return date2jalali(obj.birth).strftime('%y/%m/%d')

    get_birth_jalali.short_description = 'تاریخ تولد'
    get_birth_jalali.admin_order_field = 'birth'


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
