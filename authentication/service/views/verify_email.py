from django.conf import settings
from django.shortcuts import redirect
from django.core.mail import send_mail
from rest_framework.decorators import api_view
from rest_framework.response import Response
from authentication.models import EmailVerification

@api_view(['GET'])
def verify_email(request, verification_code):
    try:
        verification_record = EmailVerification.objects.get(verification_code=verification_code)
        user = verification_record.user
        user.is_verified = True
        user.save()
        send_mail(
                    subject=f'{settings.SERVER_NAME} - Elektron pochtani tasdiqlash',
                    message=(
                        f"Hurmatli {user.first_name} {user.last_name} siz muvaffaqiyatli ro'yxatdan o'tdingiz! \n\n"
                    ),
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[user.email],
                    fail_silently=False,
                )
        verification_record.delete()
        return redirect(f'{settings.SUCCESSFUL_CODE_URL}')
    except EmailVerification.DoesNotExist:
        return Response({"error": "Invalid verification code."}, status=400)