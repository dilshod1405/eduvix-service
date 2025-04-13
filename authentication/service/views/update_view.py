from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from authentication.service.serializers import UserUpdateSerializer
from authentication.service.permissions import IsOwner
from django.views.decorators.csrf import csrf_exempt
from authentication.models import User
from rest_framework import status
from rest_framework.exceptions import ValidationError
from authentication.service.send_delete_profile_email import send_delete_profile_email


class UserUpdateView(generics.UpdateAPIView):
    serializer_class = UserUpdateSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_object(self):
        try:
            return User.objects.get(pk=self.request.user.id)
        except User.DoesNotExist:
            raise ValidationError("User not found")
        except Exception as e:
            raise ValidationError(f"An error occurred: {str(e)}")
    def put(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        user.delete()
        send_delete_profile_email(user)
        return Response({"message": "User deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    def patch(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
from django.utils.decorators import method_decorator
@method_decorator(csrf_exempt, name='dispatch')
class CSRFExemptUserUpdateView(UserUpdateView):
    pass