from django.shortcuts import get_object_or_404
from django.db.models import Q
from rest_framework.renderers import JSONRenderer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.renderers import TemplateHTMLRenderer

from .models import PosRegister, Cheque
from .serializers import PosRegisterSerializer


# PosRegister
class PosRegisterView(APIView):
    permission_classes = [IsAuthenticated]

    # renderer_classes = [TemplateHTMLRenderer]
    # template_name = '.html'
    def post(self, request):
        store_name = request.data.get('store_name')
        store_phone = request.data.get('store_phone')
        ownership = request.data.get('ownership')
        store_address = request.data.get('store_address')
        store_zipcode = request.data.get('store_zipcode')
        business_license_number = request.data.get('business_license_number')
        tax_code = request.data.get('tax_code')
        senf = request.data.get('senf')
        leaseterm_from = request.data.get('leaseterm_from')
        leaseterm_to = request.data.get('leaseterm_to')

        '''personal-info Section'''
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        father_name = request.data.get('father_name')
        birth = request.data.get('birth')
        national_code = request.data.get('national_code')
        birthcertificate_number = request.data.get('birthcertificate_number')
        birthcertificate_serial = request.data.get('birthcertificate_serial')
        birthcertificate_series = request.data.get('birthcertificate_series')
        issued = request.data.get('issued')
        mobile = request.data.get('mobile')
        home_phone = request.data.get('home_phone')
        email = request.data.get('email')
        state = request.data.get('state')
        city = request.data.get('city')
        home_address = request.data.get('home_address')
        home_zipcode = request.data.get('home_zipcode')

        '''introduce-info Section'''
        first_introducer_name = request.data.get('first_introducer_name')
        first_introducer_lastname = request.data.get('first_introducer_lastname')
        first_introducer_phone = request.data.get('first_introducer_phone')
        first_introducer_address = request.data.get('first_introducer_address')
        second_introducer_name = request.data.get('second_introducer_name')
        second_introducer_lastname = request.data.get('second_introducer_lastname')
        second_introducer_phone = request.data.get('second_introducer_phone')
        second_introducer_address = request.data.get('second_introducer_address')

        '''substrate-type Section'''
        substrate = request.data.get('substrate')

        '''account-bank-info Section '''
        first_bank_name = request.data.get('first_bank_name')
        branch_bank_name = request.data.get('branch_bank_name')
        branch_bank_number = request.data.get('branch_bank_number')
        account_number = request.data.get('account_number')
        shaba_number = request.data.get('shaba_number')
        paziresh = request.data.get('paziresh')

        '''psp Section'''
        psp = request.data.get('psp')

        '''upload-documents Section'''
        permission_document = request.data.get('permission_document')
        birthcertificate_document = request.data.get('birthcertificate_document')
        nationalcard_document = request.data.get('nationalcard_document')
        signatureseal = request.data.get('signatureseal')
        acceptance_form = request.data.get('acceptance_form')

        description = request.data.get('description')

        protected_cheque = request.data.get('protected_cheque')
        date_cheque = request.data.get('date_cheque')
        bankName_cheque = request.data.get('bankName_cheque')
        amount_number_cheque = request.data.get('amount_number_cheque')
        amount_letter_cheque = request.data.get('amount_letter_cheque')
        account_owner_cheque = request.data.get('account_owner_cheque')
        iban_cheque = request.data.get('iban_cheque')
        cheque_document = request.data.get('cheque_document')

        try:
            pos = PosRegister.objects.create(
                user=request.user,
                store_name=store_name,
                store_phone=store_phone,
                ownership=ownership,
                store_address=store_address,
                store_zipcode=store_zipcode,
                business_license_number=business_license_number,
                tax_code=tax_code,
                senf=senf,
                leaseterm_from=leaseterm_from,
                leaseterm_to=leaseterm_to,

                first_name=first_name,
                last_name=last_name,
                father_name=father_name,
                birth=birth,
                national_code=national_code,
                birthcertificate_number=birthcertificate_number,
                birthcertificate_serial=birthcertificate_serial,
                birthcertificate_series=birthcertificate_series,
                issued=issued,
                mobile=mobile,
                home_phone=home_phone,
                email=email,
                state=state,
                city=city,
                home_address=home_address,
                home_zipcode=home_zipcode,

                first_introducer_name=first_introducer_name,
                first_introducer_lastname=first_introducer_lastname,
                first_introducer_phone=first_introducer_phone,
                first_introducer_address=first_introducer_address,
                second_introducer_name=second_introducer_name,
                second_introducer_lastname=second_introducer_lastname,
                second_introducer_phone=second_introducer_phone,
                second_introducer_address=second_introducer_address,

                substrate=substrate,

                first_bank_name=first_bank_name,
                branch_bank_name=branch_bank_name,
                branch_bank_number=branch_bank_number,
                account_number=account_number,
                shaba_number=shaba_number,
                paziresh=paziresh,

                psp=psp,

                permission_document=permission_document,
                birthcertificate_document=birthcertificate_document,
                nationalcard_document=nationalcard_document,
                signatureseal=signatureseal,
                acceptance_form=acceptance_form,

                description=description,
            )
        except PosRegister.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        if pos.substrate == 'pos سیار':
            try:
                Cheque.objects.create(
                    posregister=pos,
                    protected_cheque=protected_cheque,
                    date_cheque=date_cheque,
                    bankName_cheque=bankName_cheque,
                    amount_number_cheque=amount_number_cheque,
                    amount_letter_cheque=amount_letter_cheque,
                    account_owner_cheque=account_owner_cheque,
                    iban_cheque=iban_cheque,
                    cheque_document=cheque_document
                )
            except Cheque.DoesNotExist:
             return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response({'detail': 'درخواست باموفقیت ثبت شد'}, status=status.HTTP_201_CREATED)

    # posregister = PosRegister.objects.get(pk=posregister_id)
    #


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
