from authentication.service.serializers import UserLoginSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

class UserLoginView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_data = serializer.validated_data
        return Response(user_data)