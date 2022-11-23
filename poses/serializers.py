from rest_framework import serializers

from .models import PosRegister


class PosRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = PosRegister
        fields = ('id','first_name', 'last_name','father_name', 'birth','national_code','national_card_series','birthcertificate_number','birthcertificate_serial','birthcertificate_series','issued','state','city','store_address','zipcode_pos','store_phone','business_license_number','tax_code','senf','mobile','substrate','ownership','leaseterm_from','leaseterm_to','introducer_name','introducer_lastname','introducer_phone','introducer_address','first_account_number','first_bank_name','first_shaba_number','second_account_number','second_bank_name','second_shaba_number','paziresh','businesslicense','leaseterm','ownership_document','birthcertificate','front_nationalcard','back_nationalcard','signatureseal','sabin_form_first','sabin_form_second','cerated_time','status')


# class ParentSerializer(serializers.ModelSerializer):
#     posregisters = PosRegisterSerializer(many=True)
#     # foo = serializers.SerializerMethodField()
#
#     class Meta:
#         model = Parent
#         fields = ('id','national_code', 'posregisters')
#

