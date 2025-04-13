from django.core.mail import send_mail
from django.conf import settings


def send_update_profile_email(user):
    send_mail(
        subject=f'{settings.SERVER_NAME} - Shaxsiy kabinet ma\'lumotlaringiz o\'zgartirildi',
        message=f"Assalomu alaykum {user.first_name} {user.last_name},\n\n{settings.SERVER_NAME} shaxsiy kabinet ma'lumotlaringiz muvaffaqiyatli o'zgartirildi.\n\nXizmatlarimizdan foydalanayotganingiz uchun raxmat!",
        from_email=f'{settings.EMAIL_HOST_USER}',
        recipient_list=[user.email],
    )