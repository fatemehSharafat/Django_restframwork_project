from django.contrib.auth import get_user_model

from rest_framework import serializers

from poses.serializers import PosRegisterSerializer

User= get_user_model()

class UserSerializer(serializers.ModelSerializer):
    posregisters = PosRegisterSerializer()
    class Meta:
        model = User
        fields = ('id','posregisters','first_name', 'last_name','email', 'birth','national_code','phone_number','date_joined','last_seen')


# class ParentSerializer(serializers.ModelSerializer):
#     posregisters = PosRegisterSerializer(many=True)
#     # foo = serializers.SerializerMethodField()
#
#     class Meta:
#         model = Parent
#         fields = ('id','national_code', 'posregisters')
#

