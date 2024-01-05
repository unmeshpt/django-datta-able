from rest_framework import serializers


try:
    from home.models import *
    from clients.models import *
except:
    pass 

class ProductSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = Product
        except:
            pass    
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        try:
            model = OrderItem
        except:
            pass
        fields='__all__'