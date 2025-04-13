from payme.views import PaymeWebHookAPIView
from .serializers import PaymentSerializer, CheckModulePayment
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .models import Payment
from payme import Payme
from django.conf import settings
from content.models import Module

payme = Payme(payme_id=settings.PAYME_ID)

class PaymeCallBackAPIView(PaymeWebHookAPIView):
    def handle_created_payment(self, params, result, *args, **kwargs):
        """
        Handle the successful payment. You can override this method
        """
        print(f"Transaction created for this params: {params} and cr_result: {result}")

    def handle_successfully_payment(self, params, result, *args, **kwargs):
        """
        Handle the successful payment. You can override this method
        """
        print(f"Transaction successfully performed for this params: {params} and performed_result: {result}")

    def handle_cancelled_payment(self, params, result, *args, **kwargs):
        """
        Handle the cancelled payment. You can override this method
        """
        print(f"Transaction cancelled for this params: {params} and cancelled_result: {result}")


class PaymentCreate(APIView):
    def post(self, request):
        serializer = PaymentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        result = {
            "data": serializer.data,
        }
        
        if serializer.data['method'] == 'payme':
            payment_link = payme.initializer.generate_pay_link(
                id = serializer.data['module'],
                amount = Module.objects.get(id=serializer.data['module']).price,
                return_url = f'{settings.SUCCESSFUL_CODE_URL}/courses/',
            )
            result["payment_link"] = payment_link
        return Response(result, status=status.HTTP_201_CREATED)



class CheckPaymentStatus(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request, module_id, user_id):
        try:
            payment = Payment.objects.get(module=module_id, user=user_id)
            serializer = CheckModulePayment(payment)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Payment.DoesNotExist:
            return Response({"message": "Payment does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
        