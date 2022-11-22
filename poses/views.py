# from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from .models import PosRegister, Parent
from .serializers import PosRegisterSerializer, ParentSerializer



# PosRegister
class PosRegisterView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request):
        PosRegister.objects.create(
           user=request.user,
           first_name=request.first_name,
           last_name=request.last_name,
           birth=request.birth,
           national_code=request.national_code,
           birthcertificate_number=request.birthcertificate_number,
           birthcertificate_serial=request.birthcertificate_serial,
           birthcertificate_series=request.birthcertificate_series,
           issued=request.issued,
           state=request.state,
           city=request.city,
           store_address=request.store_address,
           zipcode_pos=request.zipcode_pos,
           store_phone=request.store_phone,
           business_license_number=request.business_license_number,
           tax_code=request.tax_code,
           senf=request.senf,
           mobile=request.mobile,
           substrate=request.substrate,
           ownership=request.ownership,
           leaseterm_from=request.leaseterm_from,
           leaseterm_to=request.leaseterm_to,
           introducer_name=request.introducer_name,
           introducer_lastname=request.introducer_lastname,
           introducer_phone=request.introducer_phone,
           introducer_address=request.introducer_address,
           first_account_number=request.first_account_number,
           first_bank_name=request.first_bank_name,
           first_shaba_number=request.first_shaba_number,
           second_account_number=request.second_account_number,
           second_bank_name=request.second_bank_name,
           second_shaba_number=request.second_shaba_number,
           paziresh=request.paziresh,
           businesslicense=request.businesslicense,
           leaseterm=request.leaseterm,
           ownership_document=request.ownership_document,
           birthcertificate=request.birthcertificate,
           front_nationalcard=request.front_nationalcard,
           back_nationalcard=request.back_nationalcard,
           signatureseal=request.signatureseal,
           sabin_form_first=request.sabin_form_first,
           sabin_form_second=request.sabin_form_second,
        )

    def get(self, request):
        posregisters = PosRegister.objects.filter(user=request.user)
        serializer = PosRegisterSerializer(posregisters, many=True, context={'request': request})
        return Response(serializer.data)


class PosRegisterDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            posregister = PosRegister.objects.get(pk=pk)
        except PosRegister.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = PosRegisterSerializer(posregister, context={'request': request})
        return Response(serializer.data)


# Parent
# class ParentListView(APIView):
#
#     def get(self, request):
#         parents = Parent.objects.all()
#         serializer = ParentSerializer(parents, many=True, context={'request': request})
#         return Response(serializer.data)
#
# class ParentDetailView(APIView):
#
#     def get(self, request, pk):
#         try:
#             parent = Parent.objects.get(pk=pk)
#         except Parent.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#
#         serializer = ParentSerializer(parent, context={'request': request})
#         return Response(serializer.data)
