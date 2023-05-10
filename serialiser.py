from rest_framework import serializers
from .models import customer
from .models import products

class customerSerializer(serializers.ModelSerializer):

    class Meta:
        model=customer
        fields=('firstname','lastname')
        #fields ='__all__'

class productSerializer(serializers.ModelSerializer):

    class Meta:
        model=products
        fields='__all__'