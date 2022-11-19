# from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import PosRegister, Parent
from .serializers import PosRegisterSerializer, ParentSerializer


# PosRegister
class PosRegisterListView(APIView):

    def get(self, request, Parent_id):
        posregisters = PosRegister.objects.filter(Parent_id=Parent_id)
        serializer = PosRegisterSerializer(posregisters, many=True, context={'request': request})
        return Response(serializer.data)


class PosRegisterDetailView(APIView):

    def get(self, request, pk, Parent_id):
        try:
            posregister = PosRegister.objects.get(pk=pk,Parent_id=Parent_id)
        except PosRegister.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = PosRegisterSerializer(posregister, context={'request': request})
        return Response(serializer.data)


# Parent
class ParentListView(APIView):

    def get(self, request):
        parents = Parent.objects.all()
        serializer = ParentSerializer(parents, many=True, context={'request': request})
        return Response(serializer.data)

class ParentDetailView(APIView):

    def get(self, request, pk):
        try:
            parent = Parent.objects.get(pk=pk)
        except Parent.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ParentSerializer(parent, context={'request': request})
        return Response(serializer.data)
