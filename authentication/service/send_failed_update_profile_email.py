from django.core.mail import send_mail
from django.conf import settings


def send_failed_update_profile_email(user):
    send_mail(
        subject=f'{settings.SERVER_NAME} - Xatolik yuz berdi',
        message=f"Assalomu alaykum {user.first_name} {user.last_name},\n\n{settings.SERVER_NAME} shaxsiy kabinet ma'lumotlaringizni o'zgartirishda xatolik yuz berdi.\n\nIltimos, ma'lumotlaringizni tekshirib ko'ring va muammo davom etsa, biz bilan bog'laning.",
        from_email=f'{settings.EMAIL_HOST_USER}',
        recipient_list=[user.email],
    )