from django.db import models
from django.utils.translation import ugettext_lazy as _


class Parent(models.Model):
    national_code = models.CharField(_('national code'), max_length=10, unique=True)
    password = models.CharField(_('password'), max_length=30)

    class Meta:
        db_table = 'parent'
        verbose_name = _('parent')
        verbose_name_plural = _('parents')

    def __str__(self):
        return self.national_code

class PosRegister(models.Model):
    # Defining different types

    """FILE_AUDIO = 1
    FILE_VIDEO = 2
    FILE_PDF = 3
    FILE_TYPES = (
        (FILE_AUDIO,_('audio')),
        (FILE_VIDEO,_('video')),
        (FILE_PDF,_('pdf')),
    )
    file_type =models.PositveSmallIntegerField(_('file type'), choices=FILE_TYPES, default=FILE_AUDIO)
"""

    # parent= models.ForeignKey('self',verbose_name=_('parent'),blank=True,null=True,on_delete=models.CASCADE)
    parent = models.ForeignKey('parent',verbose_name=_('parent'),related_name='posregisters',on_delete=models.CASCADE,to_field='national_code', blank=True)
    first_name = models.CharField(_('first name'), max_length=20)
    last_name = models.CharField(_('last name'), max_length=25)
    father_name = models.CharField(_('father name'), max_length=20)
    birth = models.DateField(_('date of birth'))
    # national_code = models.ForeignKey('Login',verbose_name=_('national code'), on_delete=models.CASCADE, to_field='national_code')
    national_code = models.CharField(_('national code'), max_length=10)
    national_card_series = models.CharField(_('National card series'), max_length=10, blank=True)
    birthcertificate_number = models.CharField(_('birth certificate number'), max_length=10)
    birthcertificate_serial = models.CharField(_('birth certificate serial'), max_length=6)
    birthcertificate_series = models.CharField(_('birth certificate series'), max_length=3)
    issued = models.CharField(_('issued'), max_length=50)
    state = models.CharField(_('state'), max_length=50)
    city = models.CharField(_('city'), max_length=50)
    store_address = models.CharField(_('store address'), max_length=300)
    zipcode_pos = models.CharField(_('zip code pos'), max_length=10)
    store_phone = models.CharField(_('store phone'), max_length=8)
    business_license_number = models.CharField(_('business license number'), max_length=50)
    tax_code = models.CharField(_('tax tracking code'), max_length=50)
    senf = models.CharField(_('senf'), max_length=25)
    mobile = models.CharField(_('Mobile'), max_length=11)
    substrate_type = [
        ('Dialup', 'Dialup Type'),
        ('GPRS', 'GPRS Type'),
        ('Combo', 'Combo Type'),
        ('WIFI', 'WIFI Type'),
    ]
    substrate = models.CharField(_(' substrate type'), max_length=6, choices=substrate_type,
                                 default='Dialup')  # Dialup, GPRS, Combo, WIFI
    ownership_type = [
        ('ملکی', 'نوع ملکی'),
        ('سرقفلی', 'نوع سرقفلی'),
        ('استیجاری', 'نوع استیجاری'),
    ]
    ownership = models.CharField(_('ownership type'), max_length=8, choices=ownership_type,
                                 default='ملکی')  # ملکی، سرقفلی، استیجاری
    leaseterm_from = models.DateField(_('leaseterm from'), blank=True)
    leaseterm_to = models.DateField(_('leaseterm to'), blank=True)
    introducer_name = models.CharField(_('introducer name'), max_length=20)
    introducer_lastname = models.CharField(_('introducer last name'), max_length=25)
    introducer_phone = models.CharField(_('introducer phone'), max_length=11)
    introducer_address = models.CharField(_('introducer address'), max_length=300, blank=True)
    first_account_number = models.CharField(_('first account number'), max_length=20)
    bank_name = [
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
    first_bank_name = models.CharField(_('first bank name'), max_length=50, choices=bank_name, default='ایران زمین')
    first_shaba_number = models.CharField(_('first shaba number'), max_length=16)
    second_account_number = models.CharField(_('second account number'), max_length=20, choices=bank_name, default='ایران زمین',blank=True)
    second_bank_name = models.CharField(_('second bank name'), max_length=50, blank=True)
    second_shaba_number = models.CharField(_('second shaba number'), max_length=16, blank=True)
    paziresh = models.BooleanField(_('paziresh'), default=False)
    businesslicense = models.FileField(_('businesslicense'), upload_to='posdocuments/%Y/%m/%d/%S/')
    leaseterm = models.FileField(_('leaseterm'), upload_to='posdocuments/%Y/%m/%d/%S/', blank=True)
    ownership_document = models.FileField(_('ownership document'), upload_to='posdocuments/%Y/%m/%d/%S/', blank=True)
    birthcertificate = models.FileField(_('birth certificate'), upload_to='posdocuments/%Y/%m/%d/%S/')
    front_nationalcard = models.FileField(_('front national card'), upload_to='posdocuments/%Y/%m/%d/%S/')
    back_nationalcard = models.FileField(_('front national card'), upload_to='posdocuments/%Y/%m/%d/%S/')
    signatureseal = models.FileField(_('signature seal'), upload_to='posdocuments/%Y/%m/%d/%S/')
    sabin_form_first = models.FileField(_('sabin form first'), upload_to='posdocuments/%Y/%m/%d/%S/')
    sabin_form_second = models.FileField(_('sabin form second'), upload_to='posdocuments/%Y/%m/%d/%S/')

    # Fields outside the form
    nameFamilyKarshenas = models.CharField(_('fullname Karshenas'), max_length=100, blank=True)
    cerated_time = models.DateTimeField(_('cerated time'), auto_now_add=True)
    updated_time = models.DateTimeField(_('updated time'), auto_now=True)
    status_type = [
        ('در انتظار بررسی ', 'در انتظار بررسی'),
        ('مشاهده درخواست', 'مشاهده درخواست'),
        ('درحال بررسی', 'درحال بررسی'),
        ('موافقت با درخواست', 'موافقت با درخواست'),
        ('رد درخواست', 'رد درخواست'),
        ('در حال صدور', 'در حال صدور'),
        ('تکمیل شده', 'تکمیل شده'),
    ]
    status= models.CharField(_('status'),max_length=60,choices=status_type, default='در انتظار بررسی',blank=True)

    class Meta:
        db_table = 'posdocuments'
        verbose_name = _('Card reader request')
        verbose_name_plural = _('Card reader request')

    def __str__(self):
        return  _('request') + self.national_code


