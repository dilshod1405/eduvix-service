from django.urls import path
from authentication.service.views.register_view import RegisterUserView
from authentication.service.views.login_view import UserLoginView
from authentication.service.views.update_view import UserUpdateView
from authentication.service.views.request_reset_password import RequestPasswordResetView
from authentication.service.views.confirm_reset_password import PasswordResetConfirmView
from authentication.service.views.GoogleAuthView import GoogleAuthView
from authentication.service.views.verify_email import verify_email

urlpatterns = [
    path('verify-email/<uuid:verification_code>/', verify_email, name='verify_email'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('update/<int:pk>/', UserUpdateView.as_view(), name='update_user'),
    path('update/<int:pk>/partial/', UserUpdateView.as_view(), name='partial_update_user'),
    path('password-reset/', RequestPasswordResetView.as_view(), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('auth/google/', GoogleAuthView.as_view(), name='google-auth'),
]
