from django.core.mail import send_mail
from django.conf import settings


def send_delete_profile_email(user):
    send_mail(
        subject=f'{settings.SERVER_NAME} - Akkountingiz o`chirildi !',
        message=f"Assalomu alaykum {user.first_name} {user.last_name},\n\n{settings.SERVER_NAME} shaxsiy kabinet akkountingiz muvaffaqiyatli o`chirildi.\n\nXizmatlarimizdan foydalanayotganingiz uchun raxmat!",
        from_email=f'{settings.EMAIL_HOST_USER}',
        recipient_list=[user.email],
    )