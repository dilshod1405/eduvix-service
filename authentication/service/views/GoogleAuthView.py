import requests
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class GoogleAuthView(APIView):
    def post(self, request):
        token = request.data.get("token")
        if not token:
            return Response({"error": "Token not provided"}, status=400)

        # Validate with Google
        google_resp = requests.get(
            f"https://oauth2.googleapis.com/tokeninfo?id_token={token}"
        )
        if google_resp.status_code != 200:
            return Response({"error": "Invalid token"}, status=400)

        data = google_resp.json()
        email = data.get("email")
        name = data.get("name")

        if not email:
            return Response({"error": "Email not found in token"}, status=400)

        user, created = User.objects.get_or_create(
            email=email,
            defaults={
                "username": email.split('@')[0],
                "first_name": name,
            }
        )
        if not user.is_active or not user.is_verified:
            user.is_active = True
            user.is_verified = True
            user.save()

        # Create JWT token for your frontend
        refresh = RefreshToken.for_user(user)

        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "user": {
                "id": user.id,
                "email": user.email,
                "username": user.username,
                "role": user.role,
            }
        })
