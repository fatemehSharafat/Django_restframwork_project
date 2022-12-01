from django.shortcuts import get_object_or_404
from django.db.models import Q
from rest_framework.renderers import JSONRenderer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.renderers import TemplateHTMLRenderer

from .models import PosRegister
from .serializers import PosRegisterSerializer


# PosRegister
class PosRegisterView(APIView):
    permission_classes = [IsAuthenticated]

    # renderer_classes = [TemplateHTMLRenderer]
    # template_name = '.html'
    def post(self, request):
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        birth = request.data.get('birth')
        national_code = request.data.get('national_code')
        birthcertificate_number = request.data.get('birthcertificate_number')
        birthcertificate_serial = request.data.get('birthcertificate_serial')
        birthcertificate_series = request.data.get('birthcertificate_series')
        issued = request.data.get('issued')
        state = request.data.get('state')
        city = request.data.get('city')
        store_address = request.data.get('store_address')
        zipcode_pos = request.data.get('zipcode_pos')
        store_phone = request.data.get('store_phone')
        business_license_number = request.data.get('business_license_number')
        tax_code = request.data.get('tax_code')
        senf = request.data.get('senf')
        mobile = request.data.get('mobile')
        substrate = request.data.get('substrate')
        ownership = request.data.get('ownership')
        leaseterm_from = request.data.get('leaseterm_from')
        leaseterm_to = request.data.get('leaseterm_to')
        first_introducer_name = request.data.get('first_introducer_name')
        first_introducer_lastname = request.data.get('first_introducer_lastname')
        first_introducer_phone = request.data.get('first_introducer_phone')
        first_introducer_address = request.data.get('first_introducer_address')
        second_introducer_name = request.data.get('second_introducer_name')
        second_introducer_lastname = request.data.get('second_introducer_lastname')
        second_introducer_phone = request.data.get('second_introducer_phone')
        second_introducer_address = request.data.get('second_introducer_address')
        first_account_number = request.data.get('first_account_number')
        first_bank_name = request.data.get('first_bank_name')
        first_shaba_number = request.data.get('first_shaba_number')
        second_account_number = request.data.get('second_account_number')
        second_bank_name = request.data.get('second_bank_name')
        second_shaba_number = request.data.get('second_shaba_number')
        paziresh = request.data.get('paziresh')
        businesslicense = request.data.get('businesslicense')
        leaseterm = request.data.get('leaseterm')
        ownership_document = request.data.get('ownership_document')
        birthcertificate = request.data.get('birthcertificate')
        front_nationalcard = request.data.get('front_nationalcard')
        back_nationalcard = request.data.get('back_nationalcard')
        signatureseal = request.data.get('signatureseal')
        sabin_form_first = request.data.get('sabin_form_first')
        sabin_form_second = request.data.get('sabin_form_second')

        try:
            PosRegister.objects.create(
                user=request.user,
                first_name=first_name,
                last_name=last_name,
                birth=birth,
                national_code=national_code,
                birthcertificate_number=birthcertificate_number,
                birthcertificate_serial=birthcertificate_serial,
                birthcertificate_series=birthcertificate_series,
                issued=issued,
                state=state,
                city=city,
                store_address=store_address,
                zipcode_pos=zipcode_pos,
                store_phone=store_phone,
                business_license_number=business_license_number,
                tax_code=tax_code,
                senf=senf,
                mobile=mobile,
                substrate=substrate,
                ownership=ownership,
                leaseterm_from=leaseterm_from,
                leaseterm_to=leaseterm_to,
                first_introducer_name=first_introducer_name,
                first_introducer_lastname=first_introducer_lastname,
                first_introducer_phone=first_introducer_phone,
                first_introducer_address=first_introducer_address,
                second_introducer_name=second_introducer_name,
                second_introducer_lastname=second_introducer_lastname,
                second_introducer_phone=second_introducer_phone,
                second_introducer_address=second_introducer_address,
                first_account_number=first_account_number,
                first_bank_name=first_bank_name,
                first_shaba_number=first_shaba_number,
                second_account_number=second_account_number,
                second_bank_name=second_bank_name,
                second_shaba_number=second_shaba_number,
                paziresh=paziresh,
                businesslicense=businesslicense,
                leaseterm=leaseterm,
                ownership_document=ownership_document,
                birthcertificate=birthcertificate,
                front_nationalcard=front_nationalcard,
                back_nationalcard=back_nationalcard,
                signatureseal=signatureseal,
                sabin_form_first=sabin_form_first,
                sabin_form_second=sabin_form_second,
            )
        except PosRegister.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response({'detail': 'درخواست باموفقیت ثبت شد'}, status=status.HTTP_201_CREATED)


class PosRegisterListView(APIView):
    permission_classes = [IsAuthenticated]
    queryset = PosRegister.objects.all()

    # renderer_classes = [TemplateHTMLRenderer]
    # template_name = 'profile_detail.html'
    def get(self, request):
        # search = request.query_params.get('search')
        search = request.data.get('search')

        if search:
            posregisters = PosRegister.objects.filter(
                Q(first_name__icontains=search) | Q(last_name__icontains=search) | Q(national_code__icontains=search)
                | Q(status__icontains=search) | Q(mobile__icontains=search) | Q(city__icontains=search) |
                Q(state__icontains=search)
                | Q(id__icontains=search),
                user=request.user,
            )
        else:
            posregisters = PosRegister.objects.filter(user=request.user)
        serializer = PosRegisterSerializer(posregisters, many=True, context={'request': request})
        return Response(serializer.data)


class PosRegisterDetailView(APIView):
    permission_classes = [IsAuthenticated]

    # renderer_classes = [TemplateHTMLRenderer]
    # template_name = 'profile_detail.html'

    def get(self, request, pk):
        try:
            posregister = PosRegister.objects.get(pk=pk, user=request.user)
        except PosRegister.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = PosRegisterSerializer(posregister, context={'request': request})
        return Response(serializer.data)

    def post(self, request, pk):
        posregister = get_object_or_404(PosRegister, pk=pk)
        serializer = PosRegisterSerializer(posregister, data=request.data, context={'request': request})
        if not serializer.is_valid():
            return Response(serializer.errors)
        serializer.save()
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
