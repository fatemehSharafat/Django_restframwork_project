import random

from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.core import validators
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, send_mail

from utils.validators import validate_phone_number, validate_id_number


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _created_user(self, national_code, phone_number, email, password, is_superuser, is_staff, is_active,
                      **extra_fields):
        """
        Creates and saves a User with the given national_code, email and password.
        """
        now = timezone.now()
        if not national_code:
            raise ValueError('کد ملی خود را وارد کنید.')
        email = self.normalize_email(email)
        user = self.model(
            phone_number=phone_number,
            national_code=national_code,
            email=email,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            date_joined=now,
            **extra_fields)

        if not extra_fields.get('no_password'):
            user.set_password(password)

        user.save(using=self._db)
        return user

    def create_user(self, national_code=None, phone_number=None, email=None, password=None, **extra_fields):
        return self._created_user(national_code, phone_number, email, password, False, False, extra_fields)

    def create_superuser(self, national_code, phone_number, email, password, **extra_fields):
        return self._created_user(national_code, phone_number, email, password, True, True, extra_fields)

    def get_by_phone_number(self, phone_number):
        return self.get(**{'phone_number': phone_number})


class User(AbstractBaseUser, PermissionsMixin):
    """
    َAn abstract base class implementing a fully featured user model with admin-compliant permissions.

    National Code, password and email are required. Other fields are optional.
    """

    national_code = models.CharField(_('کد ملی'), max_length=32, unique=True, help_text='کد ملی خود را وارد کنید:\n',
                                     validators=[validate_id_number],
                                     error_messages={'unique': _('یک کاربر با این کد ملی قبلا ثبت شده است')}
                                     )

    first_name = models.CharField(_('نام'), max_length=30, blank=True)
    last_name = models.CharField(_('نام خانوادگی'), max_length=50, blank=True)
    email = models.EmailField(_('email'), unique=True, null=True, blank=True)
    phone_number = models.CharField(_('تلفن همراه'), max_length=17, unique=True, null=True, blank=True,
                                    validators=[validate_phone_number],
                                    error_messages={'unique': _('شماره وارد شده قبلا ثبت شده است!')}
                                    )
    # user penal admin
    is_staff = models.BooleanField(_('کاربر پنل مدیریت'), default=False,
                                   help_text=_(
                                       'با فعال کردن این گزینه این کاربر میتواند به پنل مدیریت دسترسی داشته باشد')
                                   )
    # activate user in app
    is_active = models.BooleanField(_('فعال'), default=True,
                                    help_text=_(
                                        'فعال بودن این گزینه نشان دهنده آن است که عضویت کار بر در سیستم فعال است.')
                                    )
    date_joined = models.DateTimeField(_('تاریخ عضویت'), default=timezone.now)
    last_seen = models.DateTimeField(_(' آخرین زمان فعالیت'), null=True)

    objects = UserManager()

    USERNAME_FIELD = 'national_code'
    REQUIRED_FIELDS = ['email', 'phone_number']

    class Meta:
        db_table = 'Users'
        verbose_name = _('کاربر')
        verbose_name_plural = _('کاربران')

    def get_full_name(self):
        """
        :return:
            the first_name plus the last_name, with a space in between
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Send an email to the user.
        """
        # if from_email is None:
        #     from_email = settings.DEFAULT_FROM_EMAIL
        send_mail(subject, message, from_email, [self.email], **kwargs)

    @property
    def is_loggedin_user(self):
        """
        :return:
            True if the user has actually logged in with valid credentials.
        """
        return self.phone_number is not None or self.email is not None

    def save(self, *args, **kwargs):
        if self.email is not None and self.email.strip() == '':
            self.email = None
        super().save(*args, **kwargs)


class UserProfile(models.Model):
    user = models.OneToOneField(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nick_name = models.CharField(_('نام مستعار'), max_length=150, blank=True)
    birthday = models.DateField(_('تاریخ تولد'), null=True, blank=True)
    gender = models.BooleanField(_('جنسیت'), help_text=_('جنسیت میتوان مرد، زن، یا خالی باشد.'), null=True)

    class Meta:
        db_table = 'UserProfiles'
        verbose_name = _('پروفایل')
        verbose_name_plural = _('پروفایل ها')

    @property
    def get_first_name(self):
        return self.user.first_name

    @property
    def get_last_name(self):
        return self.user.last_name

    def get_nick_name(self):
        return self.nick_name if self.nick_name else self.user.national_code


class Device(models.Model):
    WEB = 1
    IOS = 2
    ANDROID = 3
    DEVICE_TYPE_CHOICES = (
        (WEB, 'web'),
        (IOS, 'ios'),
        (ANDROID, 'android'),
    )

    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='%(class)s', on_delete=models.CASCADE)
    device_uuid = models.UUIDField(_('Device UUID'), null=True)
    # notify_token = models.CharField(_('توکن های اعلانات'), max_length=200, blank=True, validators=[validators.RegexValidator(r'([a-z][A-Z][0-9])\w+',_('Notify token is not valid'), 'invalid')])
    last_login = models.DateTimeField(_('آخرین زمان ورود'), null=True)
    device_type = models.PositiveSmallIntegerField(choices=DEVICE_TYPE_CHOICES, default=WEB)
    device_os = models.CharField(_('نوع سیستم عامل'), max_length=20, blank=True)
    device_model = models.CharField(_('مدل device'), max_length=50, blank=True)
    app_version = models.CharField(_('app version'), max_length=20, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'user_devices'
        verbose_name = _('device')
        verbose_name_plural = _('devices')
        unique_together = ('user', 'device_uuid')
