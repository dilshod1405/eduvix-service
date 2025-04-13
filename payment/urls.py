from django.urls import path
from django.urls import include

from .views import PaymeCallBackAPIView, PaymentCreate, CheckPaymentStatus

urlpatterns = [
    path("update/", PaymeCallBackAPIView.as_view()),
    path("payme-create/", PaymentCreate.as_view(), name="payment-create"),
    path("check-payment-status/<int:module_id>/<int:user_id>/", CheckPaymentStatus.as_view(), name="check-payment"),
]