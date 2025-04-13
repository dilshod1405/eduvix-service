from .models import Payment
from rest_framework import serializers
from content.serializers import ModuleSerializer


class PaymentSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    class Meta:
        model = Payment
        fields = ['id', 'user', 'module', 'total_amount', 'status', 'created_at', 'method']


class CheckModulePayment(serializers.ModelSerializer):
    module = ModuleSerializer(read_only=True)
    
    class Meta:
        model = Payment
        fields = ['id', 'user', 'module', 'status', 'method']