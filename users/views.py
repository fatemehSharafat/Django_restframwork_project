import uuid
import random
from http.client import HTTPResponse

from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import SuccessURLAllowedHostsMixin
from django.core.cache import cache
from django.shortcuts import render

from rest_framework.renderers import TemplateHTMLRenderer , JSONRenderer,StaticHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import User, Device


class LoginView(SuccessURLAllowedHostsMixin,APIView):
    render_classes = [TemplateHTMLRenderer,StaticHTMLRenderer,JSONRenderer]
    template_name = 'khadamatikTeta_backend/login.html'

    def get(self, request):
        return  Response({'template_name': 'khadamatikTeta_backend/login.html'})

    def post(self, request):
        phone_number = request.data.get('phone_number')
        national_code = request.data.get('national_code')

        if not phone_number:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(phone_number=phone_number)
            # return Response({'detail': 'User already registered!'},
            #                 status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            # user = User.objects.create_user(phone_number=phone_number, national_code=national_code)
            # user, created = User.objects.get_or_create(phone_number=phone_number,national_code=national_code)
            return Response({'detail': 'چنین کاربری تعریف نشده!'},status=status.HTTP_404_NOT_FOUND)



        device = Device.objects.create(user=user)

        code = random.randint(10000, 99999)

        # send message (sms or email)
        # cache
        cache.set(str(phone_number), code, 2 * 60)

        return Response(self.template_name,{'code': code})


class GetTokenView(APIView):

    def post(self, request):
        phone_number = request.data.get('phone_number')
        code = request.data.get('code')

        cached_code = cache.get(str(phone_number))

        if int(code) != int(cached_code):
            return Response({'detail': 'code is  nit corest!'},status=status.HTTP_403_FORBIDDEN)


        token = str(uuid.uuid4())

        return Response({'token': token})
