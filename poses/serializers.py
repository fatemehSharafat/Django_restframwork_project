from rest_framework import serializers

from .models import PosRegister, Cheque

# class LoginSerializer(serializers.Serializer):
#     email = serializers.CharField(
#         max_length=100,
#         style={'placeholder': 'national_code', 'autofocus': True}
#     )
#     password = serializers.CharField(
#         max_length=100,
#         style={'input_type': 'password', 'placeholder': 'Password'}
#     )
#     remember_me = serializers.BooleanField()


class ChequeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cheque
        fields = ('posregister','protected_cheque', 'date_cheque', 'bankName_cheque', 'amount_number_cheque', 'amount_letter_cheque',
              'account_owner_cheque', 'iban_cheque', 'cheque_document')


class PosRegisterSerializer(serializers.ModelSerializer):
    cheque = ChequeSerializer(many=False)
    class Meta:
        model = PosRegister
        fields ='__all__'

# class ParentSerializer(serializers.ModelSerializer):
#     posregisters = PosRegisterSerializer(many=True)
#     # foo = serializers.SerializerMethodField()
#
#     class Meta:
#         model = Parent
#         fields = ('id','national_code', 'posregisters')
#
