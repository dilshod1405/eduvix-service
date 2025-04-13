from authentication.service.serializers import RegisterUserSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

class RegisterUserView(generics.GenericAPIView):
    serializer_class = RegisterUserSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "message": "User registered successfully. Please check your email for verification.",
            "user": {
                "username": user.username,
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "id": user.id,
                "role": user.role,
            }
    })
    