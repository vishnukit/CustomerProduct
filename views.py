from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import customer
from .models import products
from.serialiser import customerSerializer
from .serialiser import productSerializer

class customerlist(APIView):
    def get(self,request):
        cus1 = customer.objects.all()
        serializer=customerSerializer(cus1,many=True)
        return Response(serializer.data)
    def post(self):
        pass

class productlist(APIView):
    def get(self,request):
        pro1 = products.objects.all()
        pserializer=productSerializer(pro1,many=True)
        return Response(pserializer.data)

    def post(self):
        pass
# Create your views here.
