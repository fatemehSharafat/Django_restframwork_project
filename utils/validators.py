from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _


class PhonNumberValidator(RegexValidator):
    regex = '^(98|0)(9[0-3,9]\d{8}|[1-9]\d{9}$)'
    message =_('یک شماره تلفن معتبر وارد کنید. (تلفن های ثابت با کد شهر وارد شود)')
    code = 'invalid_phone_number'


class SKUValidator(RegexValidator):
    regex = '^[a-zA-Z0-9\-\_]{6,20}$'
    message = 'مقدار SKU باید حروف عددی با 6 تا 20 کاراکتر باشد'
    code = 'invalid_sku'


class UsernameValidator(RegexValidator):
    regex = '^[a-zA-Z][a-zA-Z0-9_\.]+$'
    message = _('Enter a valid username starting with a-z.'
                'This value may contain only letters, numbers and underscores charecters.')
    code = 'invalid_username'


class PostalCodeValidator(RegexValidator):
    regex = '^[0-9]{10}$'
    # message = _('Enter a valid postal code')
    message = _('یک کد پستی معتبر وارد کنید')
    code = 'invalid_postal_code'


class IDNumberValidator(RegexValidator):
    regex = '^[0-9]{10}$'
    # message = _('Enter a valid ID number')
    message = _('یک کد ملی  معتبر وارد کنید')
    code = 'invalid_id_number'


# International Bank Account Number(Shba)
class IBanNumberValidator(RegexValidator):
    regex = '^[a-zA-Z]{2}[0-9]{2}[a-zA-Z0-9]{4}[0-9]{7}([a-zA-Z0-9]?){0,16}$'
    # message = _('Enter a valid iban number.')
    message = _('شماره شبا باید با IR شروع 24 رقم بعد آن وارد شود.')
    code = 'invalid_iban_number'


class BankCardNumberValidator(RegexValidator):
    regex = '^[0-9]{16}$'
    # message = _('Enter a valid card number.')
    message = _('یک شماره کارت معتبر وارد کنید.')
    code = 'invalid_bank_card_number'


class BankAccountNumberValidator(RegexValidator):
    regex = '^[0-9]{0,13}$'
    # message = _('Enter a valid bank account number.')
    message = _('یک شماره حساب معتبر وارد کنید.')


validate_phone_number = PhonNumberValidator()
validate_sku = SKUValidator()
validate_username = UsernameValidator()
validate_postal_code = PostalCodeValidator()
validate_id_number = IDNumberValidator()
validate_iban_number = IBanNumberValidator()
validate_bank_card_number = BankCardNumberValidator()
validate_bank_account_number = BankAccountNumberValidator()
