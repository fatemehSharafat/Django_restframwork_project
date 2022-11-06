from django.db import models
from django.utils.translation import ugettext_lazy as _


class User(models.Model):
    national_code = models.CharField(_('national code'),max_length=10, unique=True)
    password = models.CharField(_('password'),max_length=30)

    class Meta:
        db_table= 'user'
        verbose_name = _('user')
        verbose_name_plural= _('users')


class PosRegister(models.Model):
    parent= models.ForeignKey('self',verbose_name=_('parent'),blank=True,null=True,on_delete=models.CASCADE)
    first_name = models.CharField(_('name'),max_length=20)
    last_name = models.CharField(_('last name'),max_length=25)
    father_name = models.CharField(_('father name'),max_length=20)
    birthday = models.CharField(_('date of birth'),max_length=15)
    national_code = models.ForeignKey('User',verbose_name=_('national code'), on_delete=models.CASCADE, to_field='national_code')
    national_card_series = models.CharField(_('National card series'),max_length=10, blank=True)
    birthcertificate_number = models.CharField(_('birth certificate number'),max_length=10)
    birthcertificate_serial = models.CharField(_('birth certificate serial'),max_length=6)
    birthcertificate_series = models.CharField(_('birth certificate series'),max_length=3)
    issued = models.CharField(_('issued'),max_length=50)
    State = models.CharField(_('state'),max_length=50)
    city = models.CharField(_('city'),max_length=50)
    store_address = models.CharField(_('store address'),max_length=300)
    zipcode_pos = models.CharField(_('zip code pos'),max_length=10)
    store_phone = models.CharField(_('store phone'),max_length=8)
    business_license_number = models.CharField(_('business license number'),max_length=50)
    tax_code = models.CharField(_('tax tracking code'),max_length=50)
    senf = models.CharField(_('senf'),max_length=25)
    Mobile = models.CharField(_('Mobile'),max_length=11)
    substrate_type = [
        ('Dialup', 'Dialup Type'),
        ('GPRS', 'GPRS Type'),
        ('Combo', 'Combo Type'),
        ('WIFI', 'WIFI Type'),
    ]
    substrate = models.CharField(_(' substrate type'),max_length=6, choices=substrate_type, default='Dialup')  # Dialup, GPRS, Combo, WIFI
    ownership_type = [
        ('ملکی', 'نوع ملکی'),
        ('سرقفلی', 'نوع سرقفلی'),
        ('استیجاری', 'نوع استیجاری'),
    ]
    ownership = models.CharField(_('ownership type'),max_length=8, choices=ownership_type, default='ملکی')  # ملکی، سرقفلی، استیجاری
    leaseterm_from = models.CharField(_('leaseterm from'),max_length=15, blank=True)
    leaseterm_to = models.CharField(_('leaseterm to'),max_length=15, blank=True)
    introducer_name = models.CharField(_('introducer name'),max_length=20)
    introducer_lastname = models.CharField(_('introducer last name'),max_length=25)
    introducer_phone = models.CharField(_('introducer phone'),max_length=11)
    introducer_address = models.CharField(_('introducer address'),max_length=300, blank=True)
    first_account_number = models.CharField(_('first account number'),max_length=20)
    first_bank_name= models.CharField(_('first bank name'),max_length=50)
    first_shaba_number = models.CharField(_('first shaba number'),max_length=16)
    second_account_number = models.CharField(_('second account number'),max_length=20, blank=True)
    second_bank_name = models.CharField(_('second bank name'),max_length=50, blank=True)
    second_shaba_number = models.CharField(_('second shaba number'),max_length=16, blank=True)
    paziresh = models.BooleanField(_('paziresh'),default=False)
    businesslicense = models.FileField(_('businesslicense'),upload_to='posdocuments/%Y/%m/%d/:id/')
    leaseterm = models.FileField(_('leaseterm'),upload_to='posdocuments/%Y/%m/%d/:id/', blank=True)
    ownership_document = models.FileField(_('ownership document'),upload_to='posdocuments/%Y/%m/%d/:id/', blank=True)
    birthcertificate = models.FileField(_('birth certificate'),upload_to='posdocuments/%Y/%m/%d/:id/')
    front_nationalcard = models.FileField(_('front national card'),upload_to='posdocuments/%Y/%m/%d/:id/')
    back_nationalcard = models.FileField(_('front national card'),upload_to='posdocuments/%Y/%m/%d/:id/')
    signatureseal = models.FileField(_('signature seal'),upload_to='posdocuments/%Y/%m/%d/:id/')
    sabin_form_first = models.FileField(_('sabin form first'),upload_to='posdocuments/%Y/%m/%d/:id/')
    sabin_form_second = models.FileField(_('sabin form second'),upload_to='posdocuments/%Y/%m/%d/:id/')

    #Fields outside the form
    nameFamilyKarshenas = models.CharField(_('fullname Karshenas'),max_length=100, blank=True)
    cerated_time = models.DateTimeField(_('cerated time'),auto_now_add=True)
    updated_time= models.DateTimeField(_('updated time'),auto_now=True)

    class Meta:
        db_table='posdocuments'
        verbose_name=_('Pos Request')
        verbose_name_plural=_('Pos Requests')

