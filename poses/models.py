from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from users.models import User
from utils.validators import (
    validate_phone_number, validate_postal_code,
    validate_id_number, validate_iban_number,
    validate_bank_account_number
)

class PosRegister(models.Model):

    def get_media_file_name(self, request):
        """
            #The first mode:
                return "posRegister_documents/user_%s/request_%s/%s" % (str(self.user.national_code), str(self.id), str(request))
            #//  posRegister_documents/user_national_code/request_id/file_nam
        """
        return "posRegister_documents/request_%s/%s" % (str(self.id), str(request))

        # Defining different types
    """
        FILE_AUDIO = 1
        FILE_VIDEO = 2
        FILE_PDF = 3
        FILE_TYPES = (
            (FILE_AUDIO,_('audio')),
            (FILE_VIDEO,_('video')),
            (FILE_PDF,_('pdf')),
        )
        file_type =models.PositveSmallIntegerField(_('file type'), choices=FILE_TYPES, default=FILE_AUDIO)
    """
    SUBSTRATE_TYPES = [
        ('Dialup', 'Dialup Type'),
        ('GPRS', 'GPRS Type'),
        ('Combo', 'Combo Type'),
        ('WIFI', 'WIFI Type'),
    ]
    OWNERSHIP_TYPES = [
        ('ملکی', 'نوع ملکی'),
        ('سرقفلی', 'نوع سرقفلی'),
        ('استیجاری', 'نوع استیجاری'),
    ]
    BANK_NAME_TYPES = [
        ('ایران زمین', 'نوع ایران زمین'),
        ('آینده', 'نوع آینده'),
        ('پست بانک', 'نوع پست بانک'),
        ('خاورمیانه', 'نوع خاورمیانه'),
        ('دی', 'نوع دی'),
        ('رفاه', 'نوع رفاه'),
        ('سامان', 'نوع سامان'),
        ('شهر', 'نوع شهر'),
        ('صادرات', 'نوع صادرات'),
        ('کشاورزی', 'نوع کشاورزی'),
        ('گردشگری', 'نوع گردشگری'),
        ('مسکن', 'نوع مسکن'),
        ('ملی', 'نوع ملی'),
        ('اقتصاد نوین', 'نوع اقتصاد نوین'),
        ('پارسیان', 'نوع پارسیان'),
        ('تجارت', 'نوع تجارت'),
        ('توسعه تعاون', 'نوع توسعه تعاون'),
        ('سپه', 'نوع سپه'),
        ('سرمایه', 'نوع سرمایه'),
        ('سینا', 'نوع سینا'),
        ('صنعت و معدن', 'صنعت و معدن'),
        ('کار آفرین', 'کار آفرین'),
    ]
    STATUS_TYPES = [
        ('ثبت درخواست ', 'ثبت درخواست'),
        ('مشاهده شد', 'مشاهده شد'),
        ('درحال بررسی', 'درحال بررسی'),
        ('رد درخواست (نامرتبط بودن صنف)', 'رد از طرف شرکت (نامرتبط بودن صنف)'),
        ('ثبت شاپرک', 'ثبت شاپرک'),
        ('رد به علت نقص مدارک', 'رد به علت نقص مدارک'),
        ('اختصاص ترمینال', 'اختصاص ترمینال'),
        ('نصب شد', 'نصب شد'),
    ]
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name=_('کارشناس فروش'), related_name='%(class)s',on_delete=models.CASCADE, blank=True)
    first_name = models.CharField(_('نام'), max_length=20)
    last_name = models.CharField(_('نام خانوادگی'), max_length=25)
    father_name = models.CharField(_('نام پدر'), max_length=20)
    birth = models.DateField(_('تاریخ تولد'))
    mobile = models.CharField(_('تلفن همراه'), max_length=11, validators=[validate_phone_number])
    # national_code = models.ForeignKey('Login',verbose_name=_('national code'), on_delete=models.CASCADE, to_field='national_code')
    national_code = models.CharField(_('کدملی'), max_length=10, validators=[validate_id_number])
    national_card_series = models.CharField(_('سریال پشت کارت ملی'), max_length=10, blank=True)
    birthcertificate_number = models.CharField(_('شماره شناسنامه/کدثبتی'), max_length=10)
    birthcertificate_serial = models.CharField(_('سریال شناسنامه'), max_length=6)
    birthcertificate_series = models.CharField(_('سری شناسنامه'), max_length=3)
    issued = models.CharField(_('صادره از/ثبت شده در'), max_length=50)
    state = models.CharField(_('استان'), max_length=50)
    city = models.CharField(_('شهر'), max_length=50)
    store_name = models.CharField(_('نام فروشگاه/شرکت'), max_length=60)
    store_address = models.CharField(_('نشانی فروشگاه/شرکت'), max_length=300)
    zipcode_pos = models.CharField(_('کدپستی محل نصب'), max_length=10, validators=[validate_postal_code])
    store_phone = models.CharField(_('تلفن فروشگاه'), max_length=12, validators=[validate_phone_number])
    business_license_number = models.CharField(_('شماره پروانه کسب/شماره صنفی اجاره نامه'), max_length=50)
    tax_code = models.CharField(_('کد رهگیری مالیاتی'), max_length=50)
    senf = models.CharField(_('صنف'), max_length=25)
    substrate = models.CharField(_(' بستر ارتباطی'), max_length=6, choices=SUBSTRATE_TYPES,default='Dialup')  # Dialup, GPRS, Combo, WIFI
    ownership = models.CharField(_('نوع مالکیت محل نصب'), max_length=8, choices= OWNERSHIP_TYPES,default='ملکی')  # ملکی، سرقفلی، استیجاری
    leaseterm_from = models.DateField(_('مهلت اجاره نامه از تاریخ'), blank=True)
    leaseterm_to = models.DateField(_('مهلت اجاره نامه تا تاریخ'), blank=True)
    first_introducer_name = models.CharField(_('نام معرف اول'), max_length=20)
    first_introducer_lastname = models.CharField(_('نام خانوادگی  معرف اول'), max_length=25)
    first_introducer_phone = models.CharField(_('تلفن همراه  معرف اول '), max_length=12, validators=[validate_phone_number])
    first_introducer_address = models.CharField(_('نشانی محل سکونت  معرف اول '), max_length=300, blank=True)
    second_introducer_name = models.CharField(_('نام  معرف دوم'), max_length=20, blank=True,null=True)
    second_introducer_lastname = models.CharField(_('نام خانوادگی  معرف دوم'), max_length=25,blank=True,null=True)
    second_introducer_phone = models.CharField(_('تلفن همراه  معرف دوم '), max_length=12, validators=[validate_phone_number], blank=True,null=True)
    second_introducer_address = models.CharField(_('نشانی محل سکونت  معرف دوم '), max_length=300, blank=True,null=True)
    first_account_number = models.CharField(_('شماره حساب اول'), max_length=13,validators=[validate_bank_account_number])
    first_bank_name = models.CharField(_('نام بانک اول'), max_length=50, choices= BANK_NAME_TYPES, default='ایران زمین')
    first_shaba_number = models.CharField(_('شماره شبا اول'), max_length=26, validators=[validate_iban_number])
    second_account_number = models.CharField(_('شماره حساب دوم'), max_length=13,validators=[validate_bank_account_number], blank=True)
    second_bank_name = models.CharField(_('نام بانک دوم'), max_length=50, choices= BANK_NAME_TYPES, default='ایران زمین', blank=True)
    second_shaba_number = models.CharField(_('شماره شبا دوم'), max_length=36, validators=[validate_iban_number], blank=True)
    paziresh = models.BooleanField(_('پذیرش صحت اطلاعات'), default=False)
    businesslicense = models.FileField(_('جواز کسب'), upload_to=get_media_file_name)
    leaseterm = models.FileField(_('اجاره نامه'), upload_to=get_media_file_name, blank=True)
    ownership_document = models.FileField(_('سند مالکیت'), upload_to=get_media_file_name, blank=True)
    birthcertificate = models.FileField(_('تصویر دو صفحه اول شناسنامه'), upload_to=get_media_file_name)
    front_nationalcard = models.FileField(_('تصویر رو کارت ملی'), upload_to=get_media_file_name)
    back_nationalcard = models.FileField(_('تصویر پشت کارت ملی'), upload_to=get_media_file_name)
    signatureseal = models.FileField(_('تصویر مهر و امضا'), upload_to=get_media_file_name)
    sabin_form_first = models.FileField(_('تصویر صفحه اول فرم سابین'), upload_to=get_media_file_name)
    sabin_form_second = models.FileField(_('تصویر صفحه دوم فرم سابین'), upload_to=get_media_file_name)

    # Fields outside the form
    cerated_time = models.DateTimeField(_('زمان ثبت درخواست'), auto_now_add=True)
    updated_time = models.DateTimeField(_('زمان بروزرسانی'), auto_now=True)
    status = models.CharField(_('وضعیت'), max_length=60, choices= STATUS_TYPES, default='ثبت درخواست', blank=True)

    class Meta:
        db_table = 'posdocuments'
        verbose_name = _('درخواست کارتخوان')
        verbose_name_plural = _('درخواست های کارتخوان')

    def __str__(self):
        return " %s کارشناس فروش" % (self.user.get_full_name() + self.user.national_code)

    def get_object_number(self):
        return PosRegister.objects.filter(user=self.user_id).count()
